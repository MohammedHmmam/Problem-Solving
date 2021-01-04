"""

The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example

Print the string .

Input Format

The first line contains an integer .

Constraints


Output Format

Print the list of integers from  through  as a string, without spaces.

Sample Input 0

3
Sample Output 0

123
"""
# Link:  https://www.hackerrank.com/challenges/python-print/problem
import sys
n = int(input())
if n >= 1 and n <= 150:
    myList = []
    for x in range(1 , n+1):
       myList.append(x)
    print(*myList, sep='', end='\n', file=sys.stdout)    
