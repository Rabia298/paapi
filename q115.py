115. You are given a string.Your task is to count the frequency of letters of the 
string and print the letters in descending order of frequency.
If the following string is given as input to the program:
aabbbccde
Then, the output of the program should be:
b 3
a 2
c 2

n = int(input())

word_list = []
word_dict = {}

for i in range(n):
    word = input()
    if word not in word_dict:
        word_list.append(word)
    word_dict[word] = word_dict.get(word, 0) + 1

print(len(word_list))
for word in word_list:
    print(word_dict[word], end=' ')