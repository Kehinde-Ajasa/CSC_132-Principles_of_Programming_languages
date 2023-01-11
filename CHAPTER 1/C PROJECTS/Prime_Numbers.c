/* This program helps in checking if a number is Prime number or not */


#include <stdio.h>

int main(void){
    //At this stage,we are tying to initialize all variables we would be using
    //By doing this, we are statically declaring the data type of all variables to be used
    int number;
    int counter;
    int looper;
    
    counter = 0; 
    printf("Enter the number you want to check: ");
    scanf("%d", &number); //Scanf keyword here, is used to get the user's input
    
    for (looper = 2; looper < number; looper++){
        //This is a for loop in C it takes in 3 parameters start, stop, step 
        //This means that it takes in where to start, where to stop and how much should it jump
        if (number % looper == 0){
            //each number gotten from the loop is divided by the user's input
            //if there is no remainder, counter increases by 1
            counter = counter + 1;
        }
        else{
            //When there is remainder counter increases by 0
            counter = counter + 0;
        }
    }
    if (counter > 0){
        //If the counter increased it means that a number in all the loop was a factor
        //This breaks the law for prime numbers (that they must have no remainder)
        printf("The number is not a Prime Number");
    }
    else{
        printf("The number is a Prime Number");
    }
}

