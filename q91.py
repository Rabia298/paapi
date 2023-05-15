91. Please write a program to print the list after removing even numbers in 
[5,6,77,45,22,12,24].

li = [5,6,77,45,22, 2 ,12,35,57]
for i in li:
    # print(i)
    if (i%2 == 0):
        print(i)
        li.remove(i)
    else:
        pass

print(li)