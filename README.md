# Worksheet2part1

## Table of content 
* *Introduction*
* *Installation*
* *Tasks*
    + Task 1
    + Task 2
    + Task 3
    + Task 4
## Introduction :
This is the second IOT worksheet , it will mostly focus on the implementation of binary trees to encode and decode morse code.
The programming language used is python 
This projects has 4 different python files as well as 4 Tasks.
The first thing to do would be making sure everything is correctly set up on the device that is going to be used .
## Installation :
Before engaging in this worksheet, the first thing to do is to understand how to get the python files of this project to run correctly on the device used.
A remote server **csctcloud.uwe.ac.uk** was used for this as well as the next IOT worksheets . Accessing the remote server requires installing   Azure CLI and SSH Keys  .Visual studio code needs to be installed on the device and configured for remote development to enable the user to connect to the server as it represents the environment the code will be ran in, for this particular part a UWE email was used to connect.
It’s useful to know that the steps and commands to run might differ depending on the OS of the device, just like any other editor could be used instead of VS .
## Tasks : 
### Task 1 :
This first task did not require any coding the goal behind it was to get familiar with morse code , and that was by simply connecting to the remote server on VS , forwarding the port 10105 and finally accessing the web page from a browser using the URL **://localhost:10105** 
Some encoding/decoding tests were done to get a better understanding on how those operations worked exactly as Task 2 is mainly a python implementation of Task 1 .
###	Task 2 :
The goal of this Task was to implement two functions encode and decode 
Encode (str) : This function takes a string as a parameter and returns the morse code of the given message
Decode (str): this function takes a string (morse code) as a parameter and returns a string of text of the given morse code 
As seen in the python file morse.py
In order to implement those two functions a binary tree was used. Hence why building the tree and inserting the values was implemented first .The Node class is utilized to generate the tree’s nodes , where  each node has a value as well as a parent node (unless it’s the root’s node) as well as right and left children which are represented as a dash and dot consecutively in the Node class  .
Other methods such as **isEmpty()** checks if the binary tree is empty or **tree_length()** method returns the length of the tree using recursion .
The function **printLevelOrder(root)** prints all of the nodes of the tree , layer by layer starting from the root .
```
class Node:
    def __init__(self,value):
        self.value=value
        self.dot=None
        self.dash=None
    def isEmpty(self):   #checks if the tree is empty 
        if self.value== None :
            print('tree is empty')
        else:
            print('tree not empty')
```
**Insertion** when it comes to insertion, an object of the Node class is created every time a character needs to be added to the tree structure. This will also enable the option of inserting new characters at any moment __(more about that in task 4)__.

**Deletion** : a delete function was judged unnecessary for this specific tree , even if it’s usually useful , when it comes to  this kind of implementation , deleting a character would not make sense, as all of them are needed for the encoding and decoding stage .

**Encode(str)** : the encode function , checks if the string it took is empty then  converts that string  to upper case as the tree’s values are in uppercase , it will then go through a for loop where for each element of the input it calls the __search function__ that would recursively check if the element is in the tree , if so it checks if it matches the left or right child and would then insert a dot or dash to an empty list until the element is found and finally returns the complete result of the loop in morse code .
```
def search(node,element):
                if node==None:
                    return False
                elif node.value==element:
                    return True
                else:  
                    if search(node.dot,element)==True:
                        char_code.insert(0,".")
                        return True
                    elif search(node.dash,element)==True:
                        char_code.insert(0,"-")
                        return True
```
**Decode(str)**: decode will first split the morse  code provided , then loop through each sequence of morse , checks its length , makes sure that it’s smaller than the tree’s length , once it passed the validation checks , it starts the tree traversal starting from the root by going through each character of each morse sequence and updating the current_node each time, then appending the result to the  empty list created to get the joined result.
```
for character in letter:
           
            if character ==None:
                Final_product= Final_product + ' '
                #result.append(' ')
               
            elif character =='.':
                current_node=current_node.dot
            elif character=='-':
                current_node=current_node.dash
        result.append(current_node.value)
       
        Result = "".join(result)
        Final_product=Final_product + Result 
    
    return Final_product

```

### Task 3 :
This task represents a sort of introduction to unit testing in python as can be seen in both **assert_test.py** and **main.py** files , where tests were run on both encode and decode functions using the keyword assert .
In the **morseunit.py** file can be found a TestMorse class , in order to use it the unittest python standard library  needs to be imported and  the assertEqual method needs to be called to compare if what is returned matches with the what was expected , in this class were added various tests ,7  for the encode() and 8 tests for decode() some are expected to fail , those  ones are commented out to not interrupt the program running .
```
#testing the decode function 
        self.assertEqual(morse.decode('..- ...'), 'US')
        self.assertEqual(morse.decode('..-'), 'U')
        self.assertEqual(morse.decode('.  .'), 'E*E')
        self.assertEqual(morse.decode('.... . .-.. .-.. ---  .-- --- .-. .-.. -..'), 'HELLO*WORLD')
        #this test is supposed to fail because of the lowercase decode returns the msg in uppercase 
        #running this next line will lead to an error message 
        #self.assertEqual(morse.decode('.... . .-.. .-.. ---  .-- --- .-. .-.. -..'), 'hello*world')
        self.assertEqual(morse.decode(''), '*')
        self.assertEqual(morse.decode('..........'), 'error')
        self.assertEqual(morse.decode('.....'), '5')

```
### Task 4 :

For this last task, the binary tree was expended by adding new characters, but to keep the tree balanced instead of just adding the 17 punctuation symbols, two layers of blank nodes had to be added as well.
The testing of the encode and decode functions after tree expansion can also be found in the **morseunit.py file**.
```
#Task 4 testing :
        self.assertEqual( morse.encode('$'), '...-..- ')
        self.assertEqual( morse.encode('( :'), '-.--.  ---... ')
        self.assertEqual( morse.encode(',.'), '--..-- .-.-.- ')
        self.assertEqual(morse.decode('...-..- .-.-.- --..-- -..-. -.--. -.--.-'), '$.,/()')
        self.assertEqual(morse.decode('...-..-  .-.-.- --..-- -..-.  -.--. -.--.-'), '$*.,/*()')
        self.assertEqual(morse.decode('..--- ----- ...-..-'), '20$')
```


