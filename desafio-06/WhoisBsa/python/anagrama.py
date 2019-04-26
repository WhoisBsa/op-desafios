""" Anagrams by WhoisBsa """
from itertools import permutations
import re
import sys


def anagrams(wrd, wrd_line):
    
    a = []
    if wrd == "":
        return [wrd]
    else:
        ans = []
    for w in anagrams(wrd[1:], wrd_line):
        for pos in range(len(w)+1):
            ans.append(w[:pos]+wrd[0]+w[pos:])
            if w[:pos]+wrd[0]+w[pos:] in wrd_line:
                print(w[:pos]+wrd[0]+w[pos:])   
                
        
    return ans


def checkWord(wrd):
    """ Checks whether the word have just chars [A-Z] or not """
    input_is_only_letters = False
    while not input_is_only_letters:
        if wrd.isalpha():
            input_is_only_letters = True
        else:
            wrd = str.upper(input(('Please enter only letters A-Z (not case sensitive): ')))
    return wrd


def main():
    """ Main function """
    with open('words.txt', 'r') as file:
        word_line = list(line.strip('\n') for line in file)
        word = sys.argv[1].upper()
        word = re.sub(r'\s', '', word)
        word = checkWord(word)
        (anagrams(word, word_line))
        

if __name__ == '__main__':
    main()