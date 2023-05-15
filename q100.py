100. With a given list [12,24,35,24,88,120,155,88,120,155], write a program 
to print this list after removing all duplicate values with original order 
reserved


# Python code to remove duplicate elements
def Remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
	
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))
