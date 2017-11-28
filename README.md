# word-count

An app to count the number of words in a text

Setup
-----

The code is written for python 2.7

This project depends on Flask, so first install with:

    pip install -r requirements.txt

##### Run the app:

    python main.py


Then visit http://127.0.0.1:5000/ in a browser

##### Packages Used:
    Flask
    Flask-wtf for form handling
    pyenchant for identifying valid words

##### Assumptions:

Q. What makes a word?

A. Here are the criteria I have used to identify a string as a word

   1. The driving logic to identify a word is if its followed by a space
   2. Out of those, if a string is just special characters ($,#,! etc), it is ignored (eg. $#@,(){ etc.)
   3. If a string is just numerical characters, it is ignored (eg. 1234)
   4. If a string is a mix of alphabets and numbers, it is counted as a word
   5. If a string has leading or trailing non alpha-numerical characters (special characters, punctuations), it is stripped and the rest is counted as a word (eg. $!hello)' becomes a hello and is counted as hello)
   6. If a string is a mix of alphanumeric characters but has some non alpha-numerical characters in the middle, it is counted as a word (eg. hell0, h3llo, he##0). These are all counted as words

Q. What makes a valid word? Are they the same as word?

A. Out of all the "words", anything that is a dictionary word is a valid word. Hence, valid words will be the subset of words. The program displays the valid word with its count in the result


   
