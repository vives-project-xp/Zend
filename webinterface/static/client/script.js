// start client side server with "http-server"
//const { default: axios } = require("axios");

let ledStatus = document.getElementById('led-status');
let ledButton = document.getElementById('switch-led');

const url = "http://172.16.103.132/"
var brightness_slider = document.getElementById("brightness");
var brightness = brightness_slider.value;

var effect_speed_slider = document.getElementById("effect_speed");
var effect_speed = effect_speed_slider.value;

var color_picker_primary = document.getElementById("primary_led_color");
var primary_color = color_picker_primary.value.toString();

var color_picker_secondary = document.getElementById("secondary_led_color");
var secondary_color = color_picker_secondary.value.toString();

var selected_pattern = document.getElementById("sand-pattern-options").value;

var effectIndices = [
    {"" : "Choose an effect"},
    {"0": "Solid"},
    {"2": "Breathe"},
    {"3": "Wipe"},
    {"6": "Sweep"},
    {"8": "Rainbow"},
    {"12": "Fade"}
];

var patternOptions = [
    {"0" : "Choose a pattern"},
    {"1" : "Polygon"},
    {"2" : "Star"},
    {"3" : "Spiral"},
    {"4" : "Christmas tree"},
    
];

$.each(effectIndices, function(i){
    $.each(effectIndices[i], function(index, effect) {
        $("#options")
        .append($("<option></option>")
        .attr("value",index)
        .text(effect));
    }) 
});

$.each(patternOptions, function(i){
    $.each(patternOptions[i], function(index, pattern) {
        $("#sand-pattern-options")
        .append($("<option></option>")
        .attr("value",index)
        .text(pattern));
    }) 
});

function setupLed(){
    const setup_url = url + "win&T=1&A=50&CL=hFF0000&C2=h00FF00&FX=0&SX=50&S2=78";
    axios.get(setup_url);

}

function turnLedOn(){
    const new_url = url + "win&T=1&S2=78";
    axios.get(new_url);
}

function turnLedOff(){
    const new_url = url + "win&T=0";
    axios.get(new_url);
}

function setBrightness(){
    brightness = brightness_slider.value;
    const new_url = url + "win&A=" + brightness.toString() + "&T=1";
    console.log("brightness = " + brightness);
    axios.get(new_url);
}

color_picker_primary.oninput = function changePrimaryColor(){
    primary_color = color_picker_primary.value.toString().substring(1);
    const new_url = url + "win&CL=h" + primary_color + "&A=" + brightness.toString() +"&T=1"
    console.log(new_url)
    axios.get(new_url);
}

color_picker_secondary.oninput = function changeSecondaryColor(){
    secondary_color = color_picker_secondary.value.toString().substring(1);
    const new_url = url + "win&C2=h" + secondary_color + "&A=" + brightness.toString() +"&T=1"
    console.log(new_url)
    axios.get(new_url);
}

function changeEffect(){
    var effect = document.getElementById("options").value;
    console.log("effect index = " + effect);
    const new_url = url + "win&FX=" + effect.toString()+ "&T=1&A=" + brightness.toString();
    axios.get(new_url);
}

effect_speed_slider.oninput = function setEffectSpeed(){
    effect_speed = effect_speed_slider.value;
    const new_url = url + "win&A=" + brightness.toString() + "&T=1&SX=" + effect_speed.toString();
    console.log(new_url);
    axios.get(new_url);
}

function getSandPattern(){
    var selected_pattern = document.getElementById("sand-pattern-options").value;
    if (selected_pattern == 4) {
        const new_url = url + "win&CL=hFF0000&C2=h00FF00&FX=1"
        axios.get(new_url);
    } else {
        const new_url = url + "win&CL=h" + primary_color + "&C2=h" + secondary_color + "&FX=" + effect.toString();
        axios.get(new_url);
    }
}

function changePattern(){
    const new_url = "http://127.0.0.1:8000";
    var selected_pattern = document.getElementById("sand-pattern-options").value;
    // axios.get(new_url)
    // .then(function (response) {
    //     console.log(response.data)
    //     console.log("Response from API: " + JSON.stringify(response.data))
    // })
    // const pattern_url = new_url + "/sand-pattern/" + selected_pattern.toString();
    // console.log(pattern_url);
    
    axios.get(new_url + "/sand-pattern/" + selected_pattern.toString())
    .then(function (response){
        console.log("Chosen pattern = " + JSON.stringify(response.data));
    })
} 
