//random num gen

const myButton = document.getElementById("myButton");
const labelOne = document.getElementById("labelOne");
const labelTwo = document.getElementById("labelTwo");
const labelThree = document.getElementById("labelThree");

const min = 1;
const max = 6;

let randomNumOne;
let randomNumTwo;
let randomNumThree;

myButton.onclick = function(){
    randomNumOne = Math.floor(Math.random() * max) + min;
    randomNumTwo = Math.floor(Math.random() * max) + min;
    randomNumThree = Math.floor(Math.random() * max) + min;
    labelOne.textContent = randomNumOne;
    labelTwo.textContent = randomNumTwo;
    labelThree.textContent = randomNumThree;
}