109. Given the participants' score sheet for your University Sports Day, you are 
required to find the runner-up score. You are given scores. Store them in a 
list and find the score of the runner-up.
If the following string is given as input to the program:
5
2 3 6 6 5
Then, the output of the program should be:
5


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    sc = None

    for num in arr:
        if num == mx:
            pass
        elif sc == None:
            sc = num
        elif num > sc:
            sc = num

    print(sc)