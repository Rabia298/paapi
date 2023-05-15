103. Please write a program which count and print the numbers of each 
character in a string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1

string=input("Enter the string !!")

newstr=list(string)

newlist=[]

for j in newstr:

    if j not in newlist:

        newlist.append(j)

        count=0

        for i in range(len(newstr)):

            if j==newstr[i]:

                count+=1

        print("{},{}".format(j,count))
