/*This code is used to input the amount of factors between two set of numbers
there would be a particular range of numbers to check
there would be a specified target*/


#include <stdio.h>
#include <stdlib.h>
int main(void){
    int highestNumber;
    int lowestNumber;
    int target;
    int loopval;
    int count = 0;
    
    printf("Please enter the Highest number: ");
    scanf("%d", &highestNumber);
    printf("Please enter the Lowest number: ");
    scanf("%d", &lowestNumber);
    printf("Please enter the particular Target: ");
    scanf("%d", &target);
    
    
    if (lowestNumber > highestNumber || target > highestNumber){
        printf("Invalid Input entered please try again later");
        exit(0);
    }
    for (loopval = lowestNumber; loopval < highestNumber + 1; loopval += 1){
        int reminder = loopval % target;
        if (reminder == 0){
            count += 1;
        }
        else{
            count += 0;
        }
    }

    printf("The amount of factors of %d that can be found from %d to %d is %d", target, lowestNumber, highestNumber, count);
    
}

