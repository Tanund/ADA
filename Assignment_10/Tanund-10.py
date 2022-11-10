from collections import Counter

## Huffman

#every node object will have two children, otherwise is a leave
class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def getChild(self):
        return self.left, self.right

def get_code(node, code = ''):
    
    if type(node) is str:
        #stop!!!
        return {node : code}
    
    #get the children
    left, right = node.getChild()
    
    #recursive function
    huffman_code = dict()
    huffman_code.update(get_code(left, code+'0'))
    huffman_code.update(get_code(right, code+'1'))
    
    return huffman_code

def encode(huffman_code, message):
    encoded_message = ''
    for letter in message:
        encoded_message = encoded_message + huffman_code[letter]
    return encoded_message

def decode(huffman_code=dict, encoded_message=str):
    decoded_message = ''
    tmp_bits = ''
    found_code_flag = False
    for bit in encoded_message:
        # if bit is not found in huffman code, join it with next bit
        if not found_code_flag:
            tmp_bits = tmp_bits + bit
        else:
            tmp_bits = bit
            found_code_flag = False
        # for loop huffman code to get similar bit pattern
        for key, value in huffman_code.items():
            if tmp_bits == value:
                decoded_message = decoded_message + key
                found_code_flag = True
                break

    return decoded_message


def calculateTotalCost(huffman_code=dict, encoded_message=str):
    # counter number of bits in the message
    message_bits = len(encoded_message)

    # counter huffman code table bit
    table_bits = 0
    for key, value in huffman_code.items():
        table_bits = table_bits + 8 + len(value) 

    return message_bits + table_bits


def make_the_tree(freqs_sorted):
    
    #as long as freqs_sorted.length > 1
    while len(freqs_sorted) > 1:
        
        #combine the two smallest one
        key1, value1 =  freqs_sorted[0]
        key2, value2 =  freqs_sorted[1]
        
        #delete them
        freqs_sorted = freqs_sorted[2:]
        
        #add the new combination to freqs_sorted
        new_value = value1 + value2
        new_node  = Node(key1, key2)
        
        #add to freqs_sorted
        freqs_sorted.append((new_node, new_value))
                
        #sort again!!
        freqs_sorted = sorted(freqs_sorted, key=lambda item: item[1])
        
    return freqs_sorted[0][0]
    #return root node (so we can use this generating coding....)

#input
message = 'AAABBBBBBEEEDABEEDCC'
print('Message: ' + message)

#count the letters
#use Counter, then convert to dictionary
freqs = dict(Counter(message)) #{'A': 4, 'B': 7, 'E': 5, 'D': 2, 'C': 2}
print('Count letters: ' + str(freqs))

#sort them from smallest to biggest
#{'C': 2, 'D': 2, 'A': 4, 'E': 5, 'A': 7}
freqs_sorted = sorted(freqs.items(), key=lambda item: item[1])

#make the tree by combining the smallest one, and delete those guys
root = make_the_tree(freqs_sorted)

#get the code
huffman_code = get_code(root)

#print the code
print('Huffman code table: ' + str(huffman_code))
#{'A': '01'; 'B': '11'; 'C': '000'; 'D': '001'; 'E': '10'}


# Encode message
encoded_message = encode(huffman_code, message)
print('Encoded: ' + encoded_message)
#task1: decode the encoded message to the original message
original_message = decode(huffman_code, encoded_message)
print('Decoded: ' + original_message)

#task2: calculate the total cost --> message + table
print('Total cost with huffman is ' + str(calculateTotalCost(huffman_code, encoded_message)))