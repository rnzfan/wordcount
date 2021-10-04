#! usr/bin/env python
"""
This is word count tool. 
Import it as a module: wc(file_object)
or run it as a script: python roywordcount.py -f FILENAME"""

import argparse
import sys
#import os



def wc(infile):
    count = {"linecount": 0, "wordcount": 0, "charcount": 0}

    for line in infile:
        count["linecount"] += 1
        words = line.split()
        #print(words)
        count["wordcount"] = count["wordcount"] + len(words)
        count["charcount"] = count["charcount"] + len(line.strip("\n"))
    #infile.close()
    return count
    #print("File has", linecount, "lines", wordcount, "words", charcount, "characters")

def test():
    infiletest = sys.stdin   # infiletest is a file_object, taking input from interactive shell
    result = wc(infiletest)
    print(f'There is {result["wordcount"]} words, {result["linecount"]}\'s lines and {result["charcount"]}\'s characters)')
    
def main():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("-f", "--file", dest="filename", 
                        help="the file your want to count")
    parser.add_argument("-l", "--line", dest="line", action="store_true", 
                        default=False, help="print the line count only")
    parser.add_argument("-w", "--word", dest="word", action="store_true", 
                        default=False, help="print the word count only")
    parser.add_argument("-c", "--char", dest="character", action="store_true", 
                        default=False, help="print the character count only")
    args = parser.parse_args()
    #print("arguments:", args)
    

    if args.filename == None:
        test()
        return

    with open(args.filename, 'r') as fileobj:
        result = wc(fileobj)

    #print(result)

    #print(result["linecount"])

    if (not args.line) & (not args.word) & (not args.character):
        #print("line&word&char")
        return print(f'There is {result["wordcount"]} words, {result["linecount"]}\'s lines and {result["charcount"]}\'s characters)')
    else:
        if args.line:
            #print("line")
            print("\t", result["wordcount"], end="")
        if args.word:
            #print("word")
            print("\t", result["linecount"], end="")
        if args.character:
            #print("char")
            return print("\t" ,result["charcount"])
  


if __name__ == "__main__":
    main()
else:
    print("roywordcount loaded as a module")

