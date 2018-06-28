"""
You have already seen exceptions in previous code. 
They occur when something goes wrong, due to incorrect code or input. 
When an exception occurs, the program immediately stops.
The following code produces the ZeroDivisionError 
exception by trying to divide 7 by 0.
"""

num1 = 5
num2 = 0
print(num1/num2)

"""
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly; 
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.

Python has several other built-in exceptions, such as ZeroDivisionError and OSError. Third-party libraries also often define their own exceptions.

"""

"""
To handle exceptions and to call the code when an exception
occues, you can use try/except block

try block contains the code that might throw an exception
.If an exception occurs, the code in the try block
stops being executed,and the code in the except block
is run.If no error occurs, the code in the except block
does not run

"""

try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("Done calculation")
except ZeroDivisionError:
    print('An error occured')
    print('Due to zero division')


"""

A try statement can have multiple different except blocks to handle different exceptions.
Multiple exceptions can also be put into a single except block using parentheses, 
to have the except block handle all of them.

"""

try:
    variable = 10
    print(variable+"hello") #TypeError
    print(variable/2)
except ZeroDivisionError:
    print('Division by zero error')
except (ValueError,ImportError):
    print('Error occured')

"""

An except statement without any exception specified will catch all errors. These should be used sparingly,
as they can catch unexpected errors and hide programming mistakes.

"""

try:
    word="spam"
    print(word/0)
except:
    print('An error occured')

""" finally 
No matter whether an exception is raised or not raised
whether caught or not caught,finally block will
always run irrespective of the execution of the try or
except block
"""

try:
    print('Hello')
    print(1/0)
except ZeroDivisionError:
    print('Division by zero')
finally:
    print('This code will run no matter what!')

"""
Code in the finally will also run even if an 
uncaught exception occurs in one of the preceding
blocks
 """

try:
    print(1)
    print(10/0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed the last")


"""
You can raise the exceptions by using the raise statement
"""
print(1)
raise ValueError
print(2)

"""
Exceptions can be raised with args that give detail about them
"""
name = "123"
raise NameError("Invalid name!")

"""
In except blocks, the raise statement can be 
used without arguments to re-raise whatever exception 
occurred.
"""
try:
    num = 5/0
except:
    print('An error occured')
    raise


"""

An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
An expression is tested, and if the result comes up false, an exception is raised.
Assertions are carried out through use of the assert statement.
"""

print(1)
assert 2+2 == 4
print(2)
assert 1+1 ==3
print(3)


"""
Opening the files in Python
You can use Python to read and write the contents of files.
Text files are the easiest to manipulate. Before a file can be edited, 
it must be opened, using the open function.

"""

myfile = open('filename.txt')


"""

You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default. 
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

Once a file has been opened and used, you should close it.
This is done with the close method of the file object.

file = open('filename','r+')
file.close()

The content of the file that has been opened in the text mode
can be read using the read method

file = open('filename','r+')
cont = file.read()
print(cont)
file.close()

To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read. 
You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, read returns the rest of the file.

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

After all contents in a file have been read, any attempts to read further from that file will return an empty string, because you are trying to read from the end of the file.

file = open("filename.txt", "r")
cont = file.read()
print('Re-reading")
print(file.read())
print('Finished')
file.close()


To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.

file = open('filename.txt','r')
print(file.readlines())
file.close()

Using a for loop you can iterate over the lines in the file

file = open('filename.txt','r')
for line in cont:
    print(line)
file.close()

"""


"""
Writing files Session
To write to files you use the write method, which writes a string to the file.

file = open('filename.txt','w')
file.write('This has been written to a file')
file.close()

file = open('newfile.txt','r')
print(file.read())
file.close()

When the file is opened in the write mode,
its existing content is deleted.

file = open('a.txt',r)
print('Reading initial contents')
print(file.read())
print('Finished')
file.close()

file = open('newfile.txt','w')
file.write('Some new text')
file.close()

file = open('newfile.txt','r')
print('Reading the new contents')
print(file.read())
print('Finished')
file.close()

The write method returns the number of bytes written to a file, if successful.
msg = 'Hello World'
file = open('filename.txt','w')
bytes_written = file.write(msg)
print(bytes_written)
file.close()

It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. 
One way of doing this is to use try and finally.

try:
    file = open('filename.txt')
    print(file.read())
finally:
    file.close()



An alternative way of doing this is using with statements. 
This creates a temporary variable (often called f), which is 
only accessible in the indented block of the with statement.

with open('filename.txt') as f:
    print(f.read())

The file is automatically closed at the end of the if
statement,even if an exception occurs within it.

"""
