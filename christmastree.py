import random
from termcolor import colored
#video = https://youtu.be/DdIFNQ0hQVQ
colours = ['red','green','blue','white','cyan']

def xmas_tree(n):
    print("\n\n")
    k = 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k -1
        for j in range(0,i+1):
            print(colored("* ",random.choice(colours)),end="")
        print("\r")
        amount = 2*n-3
    for i in range(0,3):
        print(" "*amount,colored("#",random.choice(colours)))

xmas_tree(11)
