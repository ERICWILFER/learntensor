
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

