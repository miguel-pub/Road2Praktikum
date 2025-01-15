// if statements

// let age = 13;

// if(age >= 18){
//     console.log("Old")
// }
// else{
//     console.log("young")
// }

// let time = 14;

// if(time < 12){
//     console.log("good morning")
// }
// else{
//     console.log("afternoon")
// }

// let isStudent = false;

// if(isStudent){
//     console.log("student")
// }
// else{
//     console.log("not student")
// }

// let age = 15;
// let hasLicense = false;

// if(age >= 16){
//     console.log("old enough");

//     if(hasLicense){
//         console.log("u have license");
//     }
//     else{
//         console.log("no license");
//     }
// }
// else{
//     console.log("u need to be older");
// }

const myText = document.getElementById("myText")
const mySubmit = document.getElementById("mySubmit")
const resultElement = document.getElementById("resultElement")
let age = 0;

mySubmit.onclick = function(){
    age = myText.value;
    age = Number(age);
    if(age >= 100){
        resultElement.textContent = "You are too old."
    }
    else if(age == 0){
        resultElement.textContent = "You were just born."
    }
    else if(age >= 18){
        resultElement.textContent = "You can enter."
    }
    else if(age < 0){
        resultElement.textContent = "Not valid."
    }
    else{
        resultElement.textContent = "Too young."
    }
}