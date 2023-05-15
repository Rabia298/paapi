110. You are given a string S and width W. Your task is to wrap the string into a 
paragraph of width.
If the following string is given as input to the program:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ


import textwrap

def wrap(string, max_width):
    
    convert = list(string)
    
    lines = []
    line = ""
    
    for i in convert:
        if len(line) < max_width:
            line += i
            
        else:
            lines.append(line)
            line = i
            
    lines.append(line)
    
    return "\n".join(lines)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)