import socket

my_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# my_socket.connect()




import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number = int(input())
numbers={1:'one',
2:'two',
3:'three',
4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine',
10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen',
20:'twenty',
30:'thirty',
40:'forty',
50:'fifty',
60:'sixty',
70:'seventy',
80:'eighty',
90:'ninty'
}

if (int(number)<=20):
    print(numbers[int(number)])
else:
    if int(number)%10==0 :
        print(number[int(number)%10])
    else:
        print(str(numbers[int(number)-(int(number)%10)])+ '-' + str(numbers[int(number)%10]))