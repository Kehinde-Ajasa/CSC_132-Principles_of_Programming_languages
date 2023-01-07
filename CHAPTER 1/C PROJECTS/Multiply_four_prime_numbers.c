// This code helps in multiplying 4 prime numbers together

#include <stdio.h>

int main(void){
    int firstnumber;
    int secondnumber;
    int thirdnumber;
    int fourthnumber;
    int looper;
    int product;
    
    
    printf("Enter your first number: ");
    scanf("%d", &firstnumber);
    for (looper = 2; looper < firstnumber; looper += 1){
        while (firstnumber % looper == 0){
            printf("The number you entered is not a prime number, please try again:: ");
            scanf("%d", &firstnumber);
        }
    }
    printf("Enter your second number: ");
    scanf("%d", &secondnumber);
    for (looper = 2; looper < secondnumber; looper++){
        while (secondnumber % looper == 0){
            printf("The number you entered is not a prime number, please try again:: ");
            scanf("%d", &secondnumber);
        }
    }
    printf("Enter your third number: ");
    scanf("%d", &thirdnumber);
    for (looper = 2; looper < thirdnumber; looper++){
        while (thirdnumber % looper == 0){
            printf("The number you entered is not a prime number, please try again:: ");
            scanf("%d", &thirdnumber);
        }
    }
    printf("Enter your fourth number: ");
    scanf("%d", &fourthnumber);
    for (looper = 2; looper < fourthnumber; looper++){
        while (fourthnumber % looper == 0){
            printf("The number you entered is not a prime number, please try again:: ");
            scanf("%d", &fourthnumber);
        }
    }
    
    
    product = firstnumber * secondnumber * thirdnumber * fourthnumber;
    printf("The product of the four prime numbers %d, %d, %d, %d, is %d",firstnumber, secondnumber, thirdnumber, fourthnumber, product);
}

