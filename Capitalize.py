#-------------------------------------------------------------------------------
# Name:        Capitalize.py
# Purpose: Andela CodeCamp Presentation
#
# Author:      Silas Emali Omurunga
#
# Created:     07/11/2018
# Copyright:   (c) Silas Emali Omurunga 2018
# Licence:     MIT
#-------------------------------------------------------------------------------
"""
Capitalize the first word then sort the string words
"""

Emptylist = []
"""empty List"""
def main():
    """function main"""
    Wordcart = ["cow", "apple", "dancer", "zebra", "tree"]
    #list contain words not organized according to alphabetic order
    Sortedwords = Wordcart.sort()
    #use sort() method to arrange words into order
    for index in range(len(Wordcart)):
    #Loop through wordCart
        Sortedwords = (Wordcart[index].capitalize())
        #capitalize the first word using capitalize() method
        Emptylist.append(Sortedwords)
        #append the looped words into an emptyList[]
        print(Emptylist)
        #output of orderly words.


if __name__ == '__main__':
    main()
