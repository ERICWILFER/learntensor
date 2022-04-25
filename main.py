import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow as tf

import json
import pickle
import datetime
import random
import pyttsx3
import speech_recognition as sr

with open("intents.json") as file:
    data = json.load(file)

try:
    # we_are_training
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tf.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    # we_are_training
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


listener = sr.Recognizer()  # object creation for listening
engine = pyttsx3.init()  # object creation for text to speech

engine.setProperty('rate', 130)  # rate of speaking
voices = engine.getProperty('voices')
# 1 for female voice and 0 for male voice
engine.setProperty('voice', voices[1].id)

# my device index is 1, you have to put your device index
my_mic = sr.Microphone(device_index=1)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def response(inp):
    results = model.predict([bag_of_words(inp, words)])[0]
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    if results[results_index] > 0.7:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        rresponse = random.choice(responses)
        print(rresponse)
        talk(rresponse)
    else:
        print("I didn't really get that")
        talk("I didn't really get that")


print("1 for chat with bot")
print("2 for talk with bot")
tr = input("Enter no: ")

if tr == "1":
    def chatbot():
        print("Start chatting with the bot (type quit to stop)!")
        while True:
            inp = input("You: ")
            if inp.lower() == "quit":
                break

            response(inp)

    chatbot()

else:
    # print("not yet prepared")
    def daytime():  # finding day time right now function
        times = datetime.datetime.now().strftime('%H')

        if "12" <= times < "05":
            return 'midnight'
        elif "05" <= times < "07":
            return 'dawn'
        elif "07" <= times < "11":
            return 'morning'
        elif "11" <= times < "13":
            return 'noon'
        elif "13" <= times < "17":
            return 'afternoon'
        elif "17" <= times < "19":
            return 'dusk'
        elif "19" <= times < "21":
            return 'evening'
        else:
            return 'night'


    greeting_1 = "Hi, how can i help you"
    greeting_2 = "welcome, i'm at you service"
    greeting_3 = "good " + daytime() + ", how can i help you"
    greeting_4 = "hey, how you doing , how can i help you"
    greeting_5 = "good " + daytime() + ", i hope, i can be helpful"
    greeting_list = [greeting_1, greeting_2, greeting_3, greeting_4, greeting_5]
    talk(random.choice(greeting_list))


    def take_command():
        try:
            command = ""
            with my_mic as source:

                print('listening...')

                # listener.adjust_for_ambient_noise(source)  # reduce noise but may take more time
                # take voice input from the microphone
                audio = listener.listen(source)
            command = listener.recognize_google(audio)  # to print voice into text
            command = command.lower()
            print(command)
        except Exception as e:
            print("Exception: " + str(e))
        return command

    def talkbot():
        print("say stop to quit")
        while True:
            command = take_command()
            if command == "stop":
                break
            response(command)

    talkbot()
