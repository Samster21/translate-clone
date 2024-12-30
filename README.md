Hi there! This is an implementation of the command line tool, translate (tr) present in Unix.

Functionalities achieved so far:
Supports simple substitutions (Replacing occurances of a single letter)
Supports translating between alphabetic character ranges (e.g, can translate from A-Z to b-x, etc...)

Using the tool: 

Currently, translation from one set of letters to another set is supported. The sets can only be a single letter, or span the entire alphabet. 
Supported sets are:
[:upper:] - Upper Case letters
[:lower:] - Lower Case letters and,
Substitutions

*******NEW***********
Character deletion now supported! 

In your terminal, please type the following: python3 cctr.py [set1] [set2]
It will ask for your input, please pass in the desired text to be translated

Future Goals:
Support various other classes of translation present in the tr tool


Support Character Squashing