""" 
You are given a string and your task is to swap cases.
 In other words, convert all lowercase letters to uppercase letters
  and vice versa.

"""
#problem link:
# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):


    newS = ""
    if s:
        for ch in s:
            if ch.isspace():
                newS += ch
            elif not ch.isalpha():
                newS += ch
            elif ch.isupper():
                newS += ch.lower()
            elif ch.islower():
                newS += ch.upper()    
    else:
        print("you should enter Text!")
    
    return newS  
                  
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)          