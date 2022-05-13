(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){

const jsonData= require('./intents.json'); 
// console.log(jsonData);
for (var [key, value] of Object.entries(jsonData)) {
    array = (key, value);
    // console.log(array)
        var json = JSON.stringify(array);
    }
    // console.log(json)
    var obj = JSON.parse(json)
    console.log(obj[0].context_set);
    


var img = document.createElement("img");
image= "./hello-g27abaa0ed_1920.jpg"
img.src = image;

var div = document.getElementById("x");
div.appendChild(img);


},{"./intents.json":2}],2:[function(require,module,exports){
module.exports={
    "intents": [
        {
            "tag": "greeting",
            "patterns": [
                "Hi",
                "How are you",
                "Is anyone there?",
                "Hello",
                "Good day",
                "Whats up"
            ],
            "responses": [
                "Hello!",
                "Hi there, how can I help?",
                "nice to meet you",
                "hello there , how can i help"
            ],
            "context_set": "./hello-hi.gif"
        },
        {
            "tag": "goodbye",
            "patterns": [
                "see ya",
                "See you later",
                "Goodbye",
                "I am Leaving",
                "Have a Good day",
                "bye"
            ],
            "responses": [
                "Sad to see you go :(",
                "Talk to you later",
                "Goodbye!"
            ],
            "context_set": ""
        },
        {
            "tag": "location",
            "patterns": [
                "where is canteen located",
                "where can i find canteen",
                "college canteen"
            ],
            "responses": [
                "Back of the UCEN college",
                "Behind College"
            ],
            "context_set": ""
        },
        {
            "tag": "name",
            "patterns": [
                "what is your name",
                "what should I call you",
                "whats your name?"
            ],
            "responses": [
                "You can call me CHAT BOT.",
                "I'm BOT!",
                "I'm BOT."
            ],
            "context_set": ""
        },
        {
            "tag": "hours",
            "patterns": [
                "when are you guys open",
                "what are your hours",
                "hours of operation",
                "operating hours",
                "what are the working hours of canteen"
            ],
            "responses": [
                "We are open 9am to 5pm College hours!"
            ],
            "context_set": ""
        },
        {
            "tag": "who is cse hod",
            "patterns": [
                "who is cse hod"
            ],
            "responses": [
                "Muthuselvi"
            ],
            "context_set": ""
        },
        {
            "tag": "who is the dean of ucen",
            "patterns": [
                "who is the dean of ucen"
            ],
            "responses": [
                "nagarajan"
            ],
            "context_set": ""
        }
    ]
}
},{}]},{},[1]);
