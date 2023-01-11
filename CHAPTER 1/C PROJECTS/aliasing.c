/*Aliasing is a loop hole in programming that treatens the reliability of codes
when written. It is a concept used to explain the phenomenon that exists
when two different memory location contains the same data*/

#include <stdio.h>
int main(void){
    int first_number;
    int second_number;
    
    first_number = 80;
    second_number = first_number;
    
    second_number = 100;
    /*The assignment of the second_number to the first number is termed aliasing
    and the main disadvantage is that if the second_number is edited or deleted, it
    affects the first number value of 80, which makes the code no longer safe
    or reliable.*/
    printf("%d", second_number);
}