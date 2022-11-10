let ledStatus = document.getElementById('led-status');
let ledButton = document.getElementById('switch-led');


const url = "http://172.16.101.218/"
var brightness_slider = document.getElementById("brightness");
var brightness = brightness_slider.value;

var effect_speed_slider = document.getElementById("effect_speed");
var effect_speed = effect_speed_slider.value;

var color_picker_primary = document.getElementById("primary_led_color");
var primary_color = color_picker_primary.value.toString();

var color_picker_secondary = document.getElementById("secondary_led_color");
var secondary_color = color_picker_secondary.value.toString();


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
    {"" : "Choose a pattern"},
    {"0" : "Coil figure"},
    {"1" : "Star"},
    {"2" : "Spiral"}
]

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


function turnLedOn(){
    const new_url = url + "win&T=1";
    axios.get(new_url);
}

function turnLedOff(){
    const new_url = url + "win&T=0";
    axios.get(new_url);
}

brightness_slider.oninput = function setBrightness(){
    brightness = brightness_slider.value;
    const new_url = url + "win&A=" + brightness.toString() + "&T=1";
    console.log("brightness = " + brightness);
    axios.get(new_url);
}

brightness_slider.onchange = function setBrightness(){
    brightness = brightness_slider.value;
    const new_url = url + "win&A=" + brightness.toString() + "&T=1";
    console.log("brightness = " + brightness);
    axios.get(new_url);
}

color_picker_primary.oninput = function changePrimaryColor(){
    color = color_picker_primary.value.toString().substring(1);
    const new_url = url + "win&CL=h" + color + "&A=" + brightness.toString() +"&T=1"
    console.log(new_url)
    axios.get(new_url);
}

color_picker_secondary.oninput = function changeSecondaryColor(){
    color = color_picker_secondary.value.toString().substring(1);
    const new_url = url + "win&C2=h" + color + "&A=" + brightness.toString() +"&T=1"
    console.log(new_url)
    axios.get(new_url);
}

function changeEffect(){
    var effect = document.getElementById("options").value;
    console.log("effect index = " + effect);
    const new_url = url + "win&FX=" + effect.toString()+ "&T=1";
    axios.get(new_url);
}

effect_speed_slider.oninput = function setEffectSpeed(){
    effect_speed = effect_speed_slider.value;
    const new_url = url + "win&A=" + brightness.toString() + "&T=1&SX=" + effect_speed.toString();
    console.log(new_url);
    axios.get(new_url);
}

function changeSandPattern(){
    // function to call API to change pattern
}