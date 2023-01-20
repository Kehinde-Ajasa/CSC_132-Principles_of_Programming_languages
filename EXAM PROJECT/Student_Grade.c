/*This code is used to print out a student's grade based on the score gotten
in a test or exam*/

#include <stdio.h>
int main(void){
    int score; //Initializing the score variable
    
    printf("Enter the score the student got: ");
    scanf("%d", &score); //This line of code helps in reading in user's input
    
    if (score > 100 || score < 0){ // || stands for or, checking between two conditions simultaneously
        printf("The Score you entered is not a valid score:");
    }
    else if (score >= 70){
        printf("Grade A");
    }
    else if(score >= 60){
        printf("Grade B");
    }
    else if(score >= 50){
        printf("Grade C");
    }
    else if(score >= 40){
        printf("Grade D");
    }
    else{
        printf("Failed Grade F");
    }
}
