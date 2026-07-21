#include<stdio.h>

int main() { 
  // Chapter 1 - Variables, Data type , input/output

// Single line comment - 

  /* Multi line comment
  in c langage */ 

  // Output -  
    char name = 'P';     // %c print only one character
    int age = 22; 
    float pi = 3.14;

    printf("Name of person: %c\n",name);                // IF WE WANT TO PRINT CHARACTER VALUE THEN WE USE %c
    printf("Age of the person: %d\n",age);              // IF WE WANT TO PRINT INTEGER VALUE THEN WE USE %d
    printf("The value of pi: %f\n",pi);                 // IF WE WANT TO PRINT FLOAT OR REAL NUMBERS THEN WE USE %f

  printf ("piyush solanki");
  printf("\n");
  printf("Apna college");
  printf("\n");
  
  // Write a program to calc. perimeter of rectangle. Take side L & W from the user.

  int L,W;
  // Perimeter of rectangle P = 2L + 2W.           L = Length.    W = Width
  printf("Enter the length of rectangle:");
  scanf("%d",&L);

  printf("Enter the Width of rectangle:");
  scanf("%d",&W);
  printf("The perimeter of rectangle:%d",2*L+2*W);
  printf("\n");

  // Write the program take a number (n) from user and output its cude (n*n*n).

  int n;
  printf("Enter the number n:");
  scanf("%d",&n);
  printf("The cube of number n is:%d",n*n*n);
  printf("\n");

  // Write the program to calculate area of square.

  int side;
  // Area of a square is (side * side) or (a * a).
  printf("Enter the side of Square:");
  scanf("%d",& side);
  printf("The area of square is:%d",side * side);
  printf("\n");

  // Write the program to calculate area of a circle.         area of circle = ( 3.14 * r * r )

  float radius;
  printf("Enter the radius of circle:");
  scanf("%f",& radius);
  printf("The area of given circle is:%f", 3.14 * radius * radius);
  // Chapter 1 complete here
  
  return 0;
}
 

