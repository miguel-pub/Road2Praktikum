
// let day = 2;

// switch(day){
//     case 1:
//         console.log("Monday");
//         break; // need to use break or it executes all cases
//     case 2:
//         console.log("Tuesday");
//         break;
//     default:
//         console.log("No day.");
//         break;
// }

let testScore = 92;
let letterGrade;

switch(true){ // if the condition of the case is true, the code executes
    case testScore >= 90:
        letterGrade = "A";
        break;
    case testScore >= 80:
        letterGrade = "B";
        break;
}
console.log(letterGrade)