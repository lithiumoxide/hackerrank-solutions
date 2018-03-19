#!/bin/python3

import sys

def designerPdfViewer(h, word):
    # Complete this function
    dictt = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    
    heights = []
    position = []
    
    for letter in word:
        position.append(dictt[letter])
        
    for element in position:
        print(position[element-1])
        print(h[element])
        
    
    print(int(max(heights)))
    return int(max(heights)) * len(word)
    

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)

