#! python3

""" Primos em Pi - Matheus Barbosa Souza """


import math
import sys
from sympy import isprime

def insert_prime(number_sequence):
    """Insere todos os primos na lista"""
    numbers = number_sequence[2:]  # Ignore '3.'
    entire_sequence = ''
    list_sequence = []

    i = 0
    while i < len(numbers)-1:
        
        if numbers[i:1+i] == 0:
            i += 1
        elif isprime(int(numbers[i:4+i])):
            entire_sequence += numbers[i:4+i]
            i += 3
        elif isprime(int(numbers[i:3+i])):
            entire_sequence += numbers[i:3+i]
            i += 2
        elif isprime(int(numbers[i:2+i])):
            entire_sequence += numbers[i:2+i]
            i += 1
        elif isprime(int(numbers[i:1+i])):
            entire_sequence += numbers[i:1+i]
            
        elif isprime(int(numbers[i:i+1])) == False:
            if entire_sequence != '':
                list_sequence.append(entire_sequence)
                entire_sequence = ''
            
        i += 1
    print(list_sequence)
    return max(list_sequence, key=float)


PI_FILE = sys.argv[1]
with open(PI_FILE) as file:
    SEQUENCE = file.read()
    print(insert_prime(SEQUENCE))
