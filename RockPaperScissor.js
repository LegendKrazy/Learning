/*
1. What if a user makes an inappropriate choice like 'dog'? How can we extend the function to handle that?
2. What if players in the game could also choose Rope in this game?
3. In this version, if both players make the same choice, the game returns a tie. What if the game didn't end there but instead asked both players for new choices?
*/


"use strict";
var userChoice = prompt("Do you choose rock, paper or scissors?");
var computerChoice = Math.random();
if (computerChoice < 0.34) {
    computerChoice = "rock";
} else if (computerChoice <= 0.67) {
    computerChoice = "paper";
} else {
    computerChoice = "scissors";
}
console.log("Computer: " + computerChoice);
var compare = function(choice1, choice2) {
    if(!choice1 || !choice2) {
        console.log("That choice is invalid! Pick again.");
        var useChoice = prompt("rock, paper or scissors");
            if(useChoice != "rock" || "paper" || "scissors"){
                console.log("Sorry, you do not possess the IQ to play this game.");
            }
    }
        if (choice1 === choice2) {
            return "The result is a tie!";
        } 
        else if (choice1 === "rock") {
            if (choice2 === "scissors") {
                return "rock wins!"
            } else {
                return "paper wins!"
            }
        } else if (choice1 === "paper") {
            if (choice2 === "rock") {
                return "paper wins"
            } else {
                return "scissors wins!"
            }
        } else if (choice1 === "scissors") {
            if (choice2 === "rock") {
                return "rock wins!"
            } else {
                return "scissors wins"
            }
        }
        };
     
compare(userChoice, computerChoice)
