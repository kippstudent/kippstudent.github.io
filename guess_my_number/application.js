$(document).ready(function(){
  //find a way for the program to choose a random number between 1 and 100, save this as a variable
  var comp_integer = Math.floor(Math.random()*100);
  console.log(comp_integer);
  //when the player clicks on the 'guess' button
  $('button').on('click', function(){
    //save their guess as a variable
    var play_guess = parseInt($('input').val());
    console.log(play_guess);
    //and compare this guess to the random number that the computer picked
    //if the user guessed the correct number...
    if(play_guess===comp_integer){
      //what happens if the guess is correct?
      console.log("Correct!");
    }
    //if the user guessed too high...
    else if(play_guess>comp_integer){
      console.log("number too high");
    }
    else
      //update the 'feedback' paragraph to tell them to guess lower
      
    //otherwise, the user guessed too low...
    console.log("number too low");
      //update the 'feedback' paragraph to tell them to guess higher
    
  });
});
