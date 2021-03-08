/*

Task

Declare a constant variable,(PI) , and assign it the value Math.PI. You will not pass this challenge unless the variable is declared as a constant and named PI (uppercase).
Read a number, (r) , denoting the radius of a circle from stdin.
Use (PI) and (r) to calculate the (area) and (perimeter) of a circle having radius .
Print (area) as the first line of output and print (perimeter) as the second line of output.

======================
Input Format

A single integer,(r) , denoting the radius of a circle.

Constraints
0 < (r) <= 100

(r) is a floating-point number scaled to at most  decimal places.
Output Format

Print the following two lines:

On the first line, print the (area) of the circle having radius .
On the second line, print the (perimeter) of the circle having radius .


area = PI * r^2
perimeter = 2 * PI * r
========================================
Link: https://www.hackerrank.com/challenges/js10-let-and-const/problem


*/




let area;
let perimeter
let r ;
r =  prompt("Enter R VAlue :");
if(r > 0 && r <= 100){
    area = PI*(r**2);
    perimeter = 2 * PI * r;
    console.log("The circle area:" , area);
    console.log("The circle Perimeter:" , perimeter);
}
    