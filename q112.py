112. You are given a date. Your task is to find what the day is on that date.
Input
A single line of input containing the space separated month, day and year, 
respectively, in MM DD YYYY format.
08 05 2015
Output
Output the correct day in capital letters.
WEDNESDAY

# Calendar Module in Python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Calendar Module in Python - Hacker Rank Solution START
import calendar

m, d, y = map(int, input().strip().split())

print(calendar.day_name[calendar.weekday(y, m, d)].upper())
# Calendar Module in Python - Hacker Rank Solution END
