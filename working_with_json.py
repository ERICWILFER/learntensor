import json
flag = "not done"
while flag != "done":
    with open("intents.json") as file:
        data = json.load(file)

    intent_list = []
    for intent in data["intents"]:
        intent_list.append(intent)

    # print(intent_list)

    intents_template = {
          "tag": "",
          "patterns": [],
          "responses": [],
          "context_set": ""
        }

    getting_pattern = input("enter the question: ")
    getting_response = input("enter the answer for that question: ")
    flag = input("Are you done?, if yes type 'done' ")

    update_tag = {"tag": getting_pattern}
    update_patterns = {"patterns": [str(getting_pattern)]}
    update_responses = {"responses":[str(getting_response)]}

    intents_template.update(update_tag)
    intents_template.update(update_patterns)
    intents_template.update(update_responses)

    print(intents_template)

    # intent_list.append(intents_template)

    # print(intent_list)

    def write_json(new_data, filename='intents.json'):
        with open(filename,'r+') as file:
              # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["intents"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

    write_json(intents_template)





