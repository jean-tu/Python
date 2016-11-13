#how to check if a string is an empty string

notEmpty = "hello"

if len(notEmpty) > 0:
  print "Length of notEmpty is not 0"
else:
  print "Length of notEmpty is 0"

#how to check if input is a string
word = raw_input("please enter a word ")
if word.isalpha(): #checks to see if the whole string is composed of characters
    print "word is a string!!"
else:
    print "word is not a string, if you put a space at the end of the word, it doesn't count as a string"
