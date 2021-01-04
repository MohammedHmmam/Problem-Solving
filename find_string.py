"""

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
Concept

Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where  is the string.
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])
A range function is used to loop over some length:

range (0, 5)
Here, the range loops over  to .  is excluded.

"""
#Link: https://www.hackerrank.com/challenges/find-a-string/
"""
                    for x in range(0 , len(string)):
                        pos = string.find(sub_string , x , len(sub_string) + 1)
                        if pos == -1:
                            continue
                        else:
                            count += 1

"""
def count_substring(string, sub_string):
    count = 0
    y = []
    if string and sub_string :
        if not string.isspace():
            if len(string) >= 1 and len(string) <= 200 :
                if all(ord(char) < 128 for char in string):
                    for x in range(0 , len(string)):
                        pos = string.find(sub_string , x , len(sub_string) + x)
                        if pos == -1:
                           continue
                        else:
                            count += 1
                    return count

                            
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)