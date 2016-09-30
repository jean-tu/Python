#This is just going to contain the different functions that can be operated on a String

#when you want to print something with an apostrophe you have to use the \
print("Using '\' symbol: He\'s here for the food") #by using the "\", python doesn't get confused with whether or not it's the end of a string

#String arrays
letter_two = "HELLO"[2]
print "Taking a char from a string array: " + letter_two #will print L because array starts at 0
print
print "~~~~~~~String Functions~~~~~~"
#Functions of strings
    #Finding the length of a string
tester_word = "JEANIETWO"
print len(tester_word) #gets the length of the string
print tester_word.lower() #converts all characters to lower case
print "master".upper() #converts all characters to upper case
#converting a number into a string
number = 23
print str(number)

#STRING FORMATTING
print
print "~~~~~~String Printing~~~~~~"
print "You can put percent in place of where a string can go"
string_1 = "String one"
string_2 = "String two"

print "First variable:  %s. 'Second variable:  %s." % (string_1, string_2)
