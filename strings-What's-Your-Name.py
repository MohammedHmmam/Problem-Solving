"""
You are given the firstname and lastname of a person on two different lines.
 Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last name ≤ .

Output Format

Print the output as mentioned above.

"""
# Probelm Link: https://www.hackerrank.com/challenges/whats-your-name

def print_full_name(a, b):
    if a and b:
        if len(a) <= 10 and len(b) <= 10 : 
            if not a.isspace():
                if not b.isspace():
                    aa = a.strip()
                    bb = b.strip()
                    print(f"Hello {aa} {bb}! You just delved into python.")

                   
       

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)