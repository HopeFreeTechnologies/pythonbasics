# This file will foucs on operations and operators like =, +, -, <, >, <=, >=, /, //, etc.
# The vast majority if not all of this file will show examples of operations then made to print their results in the form of a boolan output (true or false) as well as a few examples of exceptions that you'll come across. Lol
# I feel like this section will be relatively simple and somewhat self explanatory for myself at least, but in the spirit of completeness! ...
###################

print(" ")

# This isn't anything special next. Its literally just a divider to make the output of this file easier to read.
# Because of this you can feel free to ignore the next block.
# However the info picks up again right after so don't miss it! 

print("_______________________________________#")

print("Starting here.....")

print(" ")

# This isn't anything special next. Its literally just a divider to make the output of this file easier to read.
# Because of this you can feel free to ignore the next block.
# However the info picks up again right after so don't miss it! 

print("_______________________________________#")

print(" ")

print("Below are various results printed out from operations written in the code of this file.")
print("Numerous notes and explanations for almost every operator type and catagories are contained in the code as well...")
print("The easiest way to access this code for reference is to open this file in a text editor, &/or a python IDE. Thanks!")

print(" ")

# This isn't anything special next. Its literally just a divider to make the output of this file easier to read.
# Because of this you can feel free to ignore the next block.
# However the info picks up again right after so don't miss it! 

print("_______________________________________#")

print(" ")

print("Equals Too or rather Assignment Operator")

print(" ")

# In this case please refer to the string that has been assigned to var1. It is your notes here ;)

var1 = "Equals to operator. Better defined as an Assignment Operator as it assigns various values. In this instance it's assigning this halriously long string to var1. var1 is used to print this string to the screen when the program is run ;) - (Used to assign a value to a variable. In this case var1. Written as a single = instead of the logical operator == which compares to see if two values match and if so returns a true boolan value."
print(var1)

# This isn't anything special next. Its literally just a divider to make the output of this file easier to read.
# Because of this you can feel free to ignore the next block.
# However the info picks up again right after so don't miss it! 

print(" ")

print("_______________________________________#")

print(" ")
###################
# Next you'll find "arithmetic operators".
# So called as their most often used to do arithmetic; and even when their not - they are ;P
###################

print("Addition Operator")
print(3 + 3)

# The operation above will return 6

print(" ")

print("Subtraction Operator")
print(9 - 3)

# The operation above will return 6

print(" ")

print("Multiplication Operator")
print(2 * 3)

# The operation above will return 6

print(" ")

print("Division Operator [Returns Floating Value as Defalut]")
print(9 / 3)

# The operation above will return 3
# With just one slash for a division or to return the quotient it automatically returns it in the form of a floating point number (and-or value).
# If for whatever reason you need to avoid this you can instead use a double forward slash and it should return as an interger.

print(" ")

print("Division Operator [Returns Interger Instead of Floating Value]")
print(9 // 3)

# The operation above will return 3 as well but without the decimal.

# The next operator is also considered an arithmetic operator but is unique in that it returns the remainder of a division.

print(" ")

print("Mod Operator")
print(15 % 10)

# This should in theroy return a 5. Im sure we'll see soon enough lol.

# !!! Note that in all the examples above you had to use the print command instead of just once. Ill come back and enter another note below if we find out specifically what we're doing wrong but logic tells me we should be able to use just one print command to encompass all of the operations...)

print(" ")

# This isn't anything special next. Its literally just a divider to make the output of this file easier to read.
# Because of this you can feel free to ignore the next block.
# However the info picks up again right after so don't miss it! 

print("_______________________________________#")


# The next set of examples will focus on relative operators.
# These operators compare one thing to another, in this case numaric values although logic dictates that we should be able to compare other things as well. Im sure that will be covered in a later class though.

print(" ")

print("Equals Too Operator")
print(3 == 3)

# In the above example note two things.
# One, you use a double equals sign to denote an equals too operation as a single one is used to assign a variable or rather it's value.
# Two, you need not worry about doing anything to print true or false for the realative operations as it will do so for you as long as the print command is being implemented. This also leads me to believe that when referring to the out come of an operation for the pourpose of another piece of code that you should be able to refer to which operation you're pointing to and then write the condition being refrenced without doing anything extra to the original operation itself.

print(" ")

# This is the less than operator and will check if the value on the left is less than the one on the right.

print("Less Than Operator")
print(3 < 5)

print(" ")

# This is the greater than operator and checks to see if the value on the left is hreater than that on the right.

print("Greater Than Operator")
print(3 > 1)

print(" ")

# This is the less then or equals too operator. It will first check weather the value on the left is less than that on the right, and if it is not it will then perform a check to see if the two side contain the same value.
# If either operation is found to be true this operation will return a true value in the form of a boolan.

print("Less Than, or Equals Too Operator")
print(3 <= 3)

print(" ")

# This is the greater than or equals too operator. Like the operator directly above this operator will first check to see if the value on the left is greater than that of the right. If this turns out not to be the case it will then check to see if the two sides are of equal value.
# Either one of these operations returning a true result will result in this operation as a whole returning a true value to the program in the form of a boolan.

print("Greater Than, or Equals Too Operator")
print(3 >= 3)

print(" ")

# This isn't anything special next. Its literally just a divider to make the output of this file easier to read.
# Because of this you can feel free to ignore the next block.
# However the info picks up again right after so don't miss it! 

print("_______________________________________#")


# The next set of operators are refereed to as logical operators.
# They differentiate between certain things like, in this case, values and will return a true / false condition based on the results.
# Again im sure they can be used for something other than just numerical values however we have yet to see this done in the tutorial.

print(" ")

# This is the not operator and is checking if the values match or not.
# If they match then it will return false if the second value is literally anything else than the first than it will return true.

print("Not Operator")
print(3 != 6)

print(" ")

# This is the and operator. It allows for you to create chains or many operations together.
# For instance in the example given below your checking that both operations are equal to their respective second value. 
# Because both are infact the same to their second value (3 equals 3 and 6 equals 6) the operation returns true overall.
# Notice however as you used the and operator that when the program is run it prints only one true for this operation not two.
# This is because as stated above the and operator combines the two operations into one (as far as the program is concerned anyways).

print("And Operator")
print((3 == 3) & (6 == 6))
# Note that you can also write this operator as "and" instead of "&".

print(" ")

print("Or Operator")
print(3 < 5 or 3 < 9)

# The Operator above is referred to as the Or Operator
# This operator checks to see if either the left or the right statement or equation is correct.
# If either one ends up being correct it will return a true value in the form of a boolan.

print(" ")
# This isn't anything special next. Its literally just a divider to make the output of this file easier to read.
# Because of this you can feel free to ignore the next block.
# However the info picks up again right after so don't miss it! 

print("_______________________________________#")

print(" ")

print("This is the end of the file. If you haven't already tried it, go ahead and open this file in a text editor &/or python IDE so that you can read the notes and follow along.")
print("There's a surprising amount of information contained within that you simply can't see from just the output here!")

print(" ")

# This isn't anything special next. Its literally just a divider to make the output of this file easier to read.
# Because of this you can feel free to ignore the next block.
# However the info picks up again right after so don't miss it! 

print("_______________________________________#")

print(" ")

print("Have all the fun!")
print("~ Hope C")

# -
# -
# -

# Inside this file we've recoreded examples of all the most basic of operators
# as well as how they work and notes on the particular quirks that they have if any.
# This file is meant to act as a refrence file for the foreseeable future;
# as such any new information pertaining to operations, &/or operators in general are to be added within.
# If this changes in the future due to unforeseen circumstances a addendum shall be added below just above the sign off and seal comment section.
# This addendum shall point to the location of the file that either replaces or continues on the content of this file.
# Oh mayn! Lol

#*** Note: So it would seem that non-ASCII characters throws an error here in spyder.
# So try to keep to the general Asci characters when using the mobile editor less you may want to note what is not ASCI in a note at the top of the file >->
# Sooooooo stupid lol

# Alright to top this off there is basiclly no particularly good IDE for linux it seems especially since I'm having all sorts of trouble with my resolution.
# So just to be able to actually reach all of the code in order to actually affect it in any meaningful way (like fixing errors) I must guess about where the end actually is
# and then proceed to add a absolutly mad amount of carriage return's (the enter key to skip lines) in order to force the remaining code and or comments back onto the screen
# But hey I'll give this. I can affect it now, at least to some effect lmao

# -x-End-x-
# 
# as of 4.3.2020.5
#
# ~ Hope C
#
#
# .











































