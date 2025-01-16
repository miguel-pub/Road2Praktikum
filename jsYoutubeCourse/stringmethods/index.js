// manipulate text

// let characterthing = userName.charAt(0) // get character at index 0

// console.log(characterthing)

// console.log(userName.indexOf("M")) // = 0
// console.log(userName.lastIndexOf("l")) // last time the character appears
// console.log(userName.length); // returns length

// userName = userName.trim();


// string slicing

// const fullName = "Miguel E"

// let firstName = fullName.slice(0,7)// excludes last index
// let lastName = fullName.slice(7,8)
// console.log(firstName, lastName)

const email = "migmag@gmail.com";

let username = email.slice(0, email.indexOf("@"));
let extension = email.slice(email.indexOf("@") + 1);
console.log(username, extension)