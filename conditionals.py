'''Learning how to use conditionals'''

def condition_function(condition):
    if condition == True:
        print "The condition is true" #this is the statement that should be printed
    else:
        print "The condition is false"
    return "You have reached the end of the condition_function"

def ifelse_function(number):
    if number < 0:
        return "The number is negative"
    elif number < 1000:
        return "The number is less than 1000 but greater than 0"
    else:
        return "The number is bigger than 1000"

print condition_function(True)
print ifelse_function(123)
