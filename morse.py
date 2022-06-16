#creating a class called Node to create the tree's nodes 
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

# inserting into the tree by creating (nodes) objects layer by layer  

node=Node('*')
#first layer
node.dot=Node("E")
node.dash=Node('T')
#second layer
node.dot.dot=Node('I')
node.dot.dash=Node('A')
node.dash.dot=Node("N")
node.dash.dash=Node("M")
#third layer
node.dot.dot.dot=Node('S')
node.dot.dot.dash=Node('U')
node.dot.dash.dot=Node('R')
node.dot.dash.dash=Node('W')
node.dash.dot.dot=Node('D')
node.dash.dot.dash=Node('K')
node.dash.dash.dot=Node('G')
node.dash.dash.dash=Node('O')
# Fourth layer
node.dot.dot.dot.dot=Node('H')
node.dot.dot.dot.dash=Node("V")
node.dot.dot.dash.dot=Node('F')
node.dot.dot.dash.dash=Node("")
node.dot.dash.dot.dot=Node('L')
node.dot.dash.dot.dash=Node("")
node.dot.dash.dash.dot=Node("P")
node.dot.dash.dash.dash=Node("J")
node.dash.dot.dot.dot=Node("B")
node.dash.dot.dot.dash=Node("X")
node.dash.dot.dash.dot=Node("C")
node.dash.dot.dash.dash=Node("Y")
node.dash.dash.dot.dot=Node("Z")
node.dash.dash.dot.dash=Node("Q")
node.dash.dash.dash.dash=Node("")
node.dash.dash.dash.dot=Node("")
#last layer
node.dot.dot.dot.dot.dot=Node('5')
node.dot.dot.dot.dot.dot.dot=Node('')
node.dot.dot.dot.dot.dot.dash=Node('')
node.dot.dot.dot.dot.dot.dash.dot=Node('')
node.dot.dot.dot.dot.dot.dash.dash=Node('')
node.dot.dot.dot.dot.dot.dot.dot=Node('')
node.dot.dot.dot.dot.dot.dot.dash=Node('')
node.dot.dot.dot.dot.dash=Node('4')
node.dot.dot.dot.dot.dash.dot=Node('')
node.dot.dot.dot.dot.dash.dash=Node('')
node.dot.dot.dot.dot.dash.dot.dot=Node('')
node.dot.dot.dot.dot.dash.dot.dash=Node('')
node.dot.dot.dot.dot.dash.dash.dot=Node('')
node.dot.dot.dot.dot.dash.dash.dash=Node('')

node.dot.dot.dot.dash.dot=Node("")
node.dot.dot.dot.dash.dot.dot=Node("")
node.dot.dot.dot.dash.dot.dot.dot=Node('')
node.dot.dot.dot.dash.dot.dot.dash=Node('$')
node.dot.dot.dot.dash.dot.dash=Node("")
node.dot.dot.dot.dash.dot.dash.dot=Node('')
node.dot.dot.dot.dash.dot.dash.dash=Node('')

node.dot.dot.dot.dash.dash=Node("3")
node.dot.dot.dot.dash.dash.dot=Node("")
node.dot.dot.dot.dash.dash.dot.dot=Node('')
node.dot.dot.dot.dash.dash.dot.dash=Node('')
node.dot.dot.dot.dash.dash.dash=Node("")
node.dot.dot.dot.dash.dash.dash.dot=Node('')
node.dot.dot.dot.dash.dash.dash.dash=Node('')

node.dot.dot.dash.dot.dot=Node('')
node.dot.dot.dash.dot.dot.dot=Node('')
node.dot.dot.dash.dot.dot.dot.dot=Node('')
node.dot.dot.dash.dot.dot.dot.dash=Node('')
node.dot.dot.dash.dot.dot.dash=Node('')
node.dot.dot.dash.dot.dot.dash.dot=Node('')
node.dot.dot.dash.dot.dot.dash.dash=Node('')
node.dot.dot.dash.dot.dash=Node('¿')
node.dot.dot.dash.dot.dash.dot=Node('')
node.dot.dot.dash.dot.dash.dot.dot=Node('')
node.dot.dot.dash.dot.dash.dot.dash=Node('')
node.dot.dot.dash.dot.dash.dash=Node('')
node.dot.dot.dash.dot.dash.dash.dot=Node('')
node.dot.dot.dash.dot.dash.dash.dash=Node('')


node.dot.dot.dash.dash.dot=Node("?")
node.dot.dot.dash.dash.dot.dot=Node("")
node.dot.dot.dash.dash.dot.dot.dot=Node("")
node.dot.dot.dash.dash.dot.dot.dash=Node("")
node.dot.dot.dash.dash.dot.dash=Node("_")
node.dot.dot.dash.dash.dot.dash.dot=Node("")
node.dot.dot.dash.dash.dot.dash.dash=Node("")
node.dot.dot.dash.dash.dash=Node("2")
node.dot.dot.dash.dash.dash.dot=Node("")
node.dot.dot.dash.dash.dash.dot.dot=Node("")
node.dot.dot.dash.dash.dash.dot.dash=Node("")
node.dot.dot.dash.dash.dash.dash=Node("")
node.dot.dot.dash.dash.dash.dash.dot=Node("")
node.dot.dot.dash.dash.dash.dash.dash=Node("")

node.dot.dash.dot.dot.dash=Node('')
node.dot.dash.dot.dot.dash.dot=Node('”')
node.dot.dash.dot.dot.dash.dot.dot=Node('')
node.dot.dash.dot.dot.dash.dot.dash=Node('')
node.dot.dash.dot.dot.dash.dash=Node('')
node.dot.dash.dot.dot.dash.dash.dot=Node('')
node.dot.dash.dot.dot.dash.dash.dash=Node('')
node.dot.dash.dot.dot.dot=Node('&')
node.dot.dash.dot.dot.dot.dot=Node('')
node.dot.dash.dot.dot.dot.dot.dot=Node('')
node.dot.dash.dot.dot.dot.dot.dash=Node('')
node.dot.dash.dot.dot.dot.dash=Node('')
node.dot.dash.dot.dot.dot.dash.dot=Node('')
node.dot.dash.dot.dot.dot.dash.dash=Node('')

node.dot.dash.dot.dash.dot=Node("+")
node.dot.dash.dot.dash.dot.dot=Node("")
node.dot.dash.dot.dash.dot.dot.dot=Node("")
node.dot.dash.dot.dash.dot.dot.dash=Node("")
node.dot.dash.dot.dash.dot.dash=Node(".")
node.dot.dash.dot.dash.dot.dash.dot=Node("")
node.dot.dash.dot.dash.dot.dash.dash=Node("")
node.dot.dash.dot.dash.dash=Node("")
node.dot.dash.dot.dash.dash.dot=Node("")
node.dot.dash.dot.dash.dash.dot.dot=Node("")
node.dot.dash.dot.dash.dash.dot.dash=Node("")
node.dot.dash.dot.dash.dash.dash=Node("")
node.dot.dash.dot.dash.dash.dash.dot=Node("")
node.dot.dash.dot.dash.dash.dash.dash=Node("")

node.dot.dash.dash.dot.dot=Node("")
node.dot.dash.dash.dot.dot.dot=Node("")
node.dot.dash.dash.dot.dot.dot.dot=Node("")
node.dot.dash.dash.dot.dot.dot.dash=Node("")
node.dot.dash.dash.dot.dot.dash=Node("")
node.dot.dash.dash.dot.dot.dash.dot=Node("")
node.dot.dash.dash.dot.dot.dash.dash=Node("")
node.dot.dash.dash.dot.dash=Node("")
node.dot.dash.dash.dot.dash.dot=Node("")
node.dot.dash.dash.dot.dash.dot.dot=Node("")
node.dot.dash.dash.dot.dash.dot.dash=Node("")
node.dot.dash.dash.dot.dash.dash=Node("")
node.dot.dash.dash.dot.dash.dash.dot=Node("")
node.dot.dash.dash.dot.dash.dash.dash=Node("")


node.dot.dash.dash.dash.dot=Node("")
node.dot.dash.dash.dash.dot.dot=Node("")
node.dot.dash.dash.dash.dot.dot.dot=Node("")
node.dot.dash.dash.dash.dot.dot.dash=Node("")
node.dot.dash.dash.dash.dot.dash=Node("")
node.dot.dash.dash.dash.dot.dash.dot=Node("")
node.dot.dash.dash.dash.dot.dash.dash=Node("")
node.dot.dash.dash.dash.dash=Node("1")
node.dot.dash.dash.dash.dash.dot=Node("’")
node.dot.dash.dash.dash.dash.dot.dot=Node("")
node.dot.dash.dash.dash.dash.dot.dash=Node("")
node.dot.dash.dash.dash.dash.dash=Node("")
node.dot.dash.dash.dash.dash.dash.dot=Node("")
node.dot.dash.dash.dash.dash.dash.dash=Node("")

node.dash.dot.dot.dot.dot=Node("6")
node.dash.dot.dot.dot.dot.dot=Node("")
node.dash.dot.dot.dot.dot.dot.dot=Node("")
node.dash.dot.dot.dot.dot.dot.dash=Node("")
node.dash.dot.dot.dot.dot.dash=Node("-")
node.dash.dot.dot.dot.dot.dash.dot=Node("")
node.dash.dot.dot.dot.dot.dash.dash=Node("")
node.dash.dot.dot.dot.dash=Node("=")
node.dash.dot.dot.dot.dash.dot=Node("")
node.dash.dot.dot.dot.dash.dot.dot=Node("")
node.dash.dot.dot.dot.dash.dot.dash=Node("")
node.dash.dot.dot.dot.dash.dash=Node("")
node.dash.dot.dot.dot.dash.dash.dot=Node("")
node.dash.dot.dot.dot.dash.dash.dash=Node("")

node.dash.dot.dot.dash.dot=Node("/")
node.dash.dot.dot.dash.dot.dot=Node("")
node.dash.dot.dot.dash.dot.dot.dot=Node("")
node.dash.dot.dot.dash.dot.dot.dash=Node("")
node.dash.dot.dot.dash.dot.dash=Node("")
node.dash.dot.dot.dash.dot.dash.dot=Node("")
node.dash.dot.dot.dash.dot.dash.dash=Node("")
node.dash.dot.dot.dash.dash=Node("")
node.dash.dot.dot.dash.dash.dot=Node("")
node.dash.dot.dot.dash.dash.dot.dot=Node("")
node.dash.dot.dot.dash.dash.dot.dash=Node("")
node.dash.dot.dot.dash.dash.dash=Node("")
node.dash.dot.dot.dash.dash.dash.dot=Node("")
node.dash.dot.dot.dash.dash.dash.dash=Node("")

node.dash.dot.dash.dot.dash=Node("")
node.dash.dot.dash.dot.dash.dot=Node(";")
node.dash.dot.dash.dot.dash.dot.dot=Node("")
node.dash.dot.dash.dot.dash.dot.dash=Node("")
node.dash.dot.dash.dot.dash.dash=Node("!")
node.dash.dot.dash.dot.dash.dash.dot=Node("")
node.dash.dot.dash.dot.dash.dash.dash=Node("")
node.dash.dot.dash.dot.dot=Node("")
node.dash.dot.dash.dot.dot.dot=Node("")
node.dash.dot.dash.dot.dot.dot.dot=Node("")
node.dash.dot.dash.dot.dot.dot.dash=Node("")
node.dash.dot.dash.dot.dot.dash=Node("")
node.dash.dot.dash.dot.dot.dash.dot=Node("")
node.dash.dot.dash.dot.dot.dash.dash=Node("")

node.dash.dot.dash.dash.dot=Node("(")
node.dash.dot.dash.dash.dot.dot=Node("")
node.dash.dot.dash.dash.dot.dot.dot=Node("")
node.dash.dot.dash.dash.dot.dot.dash=Node("")
node.dash.dot.dash.dash.dot.dash=Node(")")
node.dash.dot.dash.dash.dot.dash.dot=Node("")
node.dash.dot.dash.dash.dot.dash.dash=Node("")
node.dash.dot.dash.dash.dash=Node("")
node.dash.dot.dash.dash.dash.dot=Node("")
node.dash.dot.dash.dash.dash.dot.dot=Node("")
node.dash.dot.dash.dash.dash.dot.dash=Node("")
node.dash.dot.dash.dash.dash.dash=Node("")
node.dash.dot.dash.dash.dash.dash.dot=Node("")
node.dash.dot.dash.dash.dash.dash.dash=Node("")

node.dash.dash.dot.dot.dot=Node("7")
node.dash.dash.dot.dot.dot.dot=Node("")
node.dash.dash.dot.dot.dot.dot.dot=Node("")
node.dash.dash.dot.dot.dot.dot.dash=Node("")
node.dash.dash.dot.dot.dot.dash=Node("¡")
node.dash.dash.dot.dot.dot.dash.dot=Node("")
node.dash.dash.dot.dot.dot.dash.dash=Node("")
node.dash.dash.dot.dot.dash=Node("")
node.dash.dash.dot.dot.dash.dot=Node("")
node.dash.dash.dot.dot.dash.dot.dot=Node("")
node.dash.dash.dot.dot.dash.dot.dash=Node("")
node.dash.dash.dot.dot.dash.dash=Node(",")
node.dash.dash.dot.dot.dash.dash.dot=Node("")
node.dash.dash.dot.dot.dash.dash.dash=Node("")

node.dash.dash.dot.dash.dot=Node("")
node.dash.dash.dot.dash.dot.dot=Node("")
node.dash.dash.dot.dash.dot.dot.dot=Node("")
node.dash.dash.dot.dash.dot.dot.dash=Node("")
node.dash.dash.dot.dash.dot.dash=Node("")
node.dash.dash.dot.dash.dot.dash.dot=Node("")
node.dash.dash.dot.dash.dot.dash.dash=Node("")
node.dash.dash.dot.dash.dash=Node("")
node.dash.dash.dot.dash.dash.dot=Node("")
node.dash.dash.dot.dash.dash.dot.dot=Node("")
node.dash.dash.dot.dash.dash.dot.dash=Node("")
node.dash.dash.dot.dash.dash.dash=Node("")
node.dash.dash.dot.dash.dash.dash.dot=Node("")
node.dash.dash.dot.dash.dash.dash.dash=Node("")

node.dash.dash.dash.dot.dot=Node("8")
node.dash.dash.dash.dot.dot.dot=Node(":")
node.dash.dash.dash.dot.dot.dot.dot=Node("")
node.dash.dash.dash.dot.dot.dot.dash=Node("")
node.dash.dash.dash.dot.dot.dash=Node("")
node.dash.dash.dash.dot.dot.dash.dot=Node("")
node.dash.dash.dash.dot.dot.dash.dash=Node("")
node.dash.dash.dash.dot.dash=Node("")
node.dash.dash.dash.dot.dash.dot=Node("")
node.dash.dash.dash.dot.dash.dot.dot=Node("")
node.dash.dash.dash.dot.dash.dot.dash=Node("")
node.dash.dash.dash.dot.dash.dash=Node("")
node.dash.dash.dash.dot.dash.dash.dot=Node("")
node.dash.dash.dash.dot.dash.dash.dash=Node("")

node.dash.dash.dash.dash.dot=Node("9")
node.dash.dash.dash.dash.dot.dot=Node("")
node.dash.dash.dash.dash.dot.dot.dot=Node("")
node.dash.dash.dash.dash.dot.dot.dash=Node("")
node.dash.dash.dash.dash.dot.dash=Node("")
node.dash.dash.dash.dash.dot.dash.dot=Node("")
node.dash.dash.dash.dash.dot.dash.dash=Node("")
node.dash.dash.dash.dash.dash=Node("0")
node.dash.dash.dash.dash.dash.dot=Node("")
node.dash.dash.dash.dash.dash.dot.dot=Node("")
node.dash.dash.dash.dash.dash.dot.dash=Node("")
node.dash.dash.dash.dash.dash.dash=Node("")
node.dash.dash.dash.dash.dash.dash.dot=Node("")
node.dash.dash.dash.dash.dash.dash.dash=Node("")




#function to print all nodes in the tree                
def printLevelOrder(root):
     
    # Base case
    if root is None:
        return
    # Create an empty queue for level order traversal
    q = []
    q.append(root)
    # Enqueue root and initialize height
       
    while q:
     
        # nodeCount (queue size) indicates number
        # of nodes at current level.
        count = len(q)
       
        # Dequeue all nodes of current level and
        # Enqueue all nodes of next level
        while count > 0:
            temp = q.pop(0)
            print(temp.value, end = ' ')
            if temp.dot:
                q.append(temp.dot)
            if temp.dash:
                q.append(temp.dash)
            count -= 1
   
        print(' ')
   
printLevelOrder(node)

#function to get the length of the tree by using recurssion 
def tree_length(root):
    if root is None:
        return 0
    left=tree_length(root.dot)
    right=tree_length(root.dash)
    max_height=left
    if right>max_height:
        max_height=right
    return max_height + 1
print(tree_length(node)) 
        
    


#encoding from letters to morse code
#the first step would be getting the string  then for each character found in the string search throught the tree

def encode(str):
   
    final_morse_code=""
    str=str.upper()
    if len(str)==0:
        x='nothing to encode'
        return x
    else:

        for element in str:
            #creating an empty list that would contain the morse code of one character
            char_code=[]
            #search function implemented inside the encode function to search for specific char 
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
            search(node,element)
           
            code = "".join(char_code)
            final_morse_code=final_morse_code + code + " "
        
        return final_morse_code
# decode function to convert morse code to characters 

def decode(morse):
    #first splitting each of the string characters
    letters=morse.split(' ')
    
    Final_product=''
    #each of the letters corresponds to one or more characters
    for letter in letters:
        
        #validation check in case the morse string does not exist 
        if len(letter)> (tree_length(node))-1:
            x='error'
            return x
        result=[]
       
        if letter == None:
            result.append()
       
        #for each letter we start by pointing at the root node
        current_node=node
        #checking if the first character is a space
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
print(encode('$ ('))
print(decode('.....'))
print(decode('.-..-.'))
# print(decode('...... .'))
#print(decode('----....'))
     
