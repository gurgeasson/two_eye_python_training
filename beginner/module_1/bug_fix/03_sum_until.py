'''
Define a function called sum_until.
Accept a number called limit.
Use a while loop to add numbers from 1 through the limit.
Return the total.
Fix 4 bugs.
Optional: Improve the code using simple best practices.
'''

def sum_until(limit):
    total = 0
    i = 1

    while i <= limit:
        total += i
        i = i + 1
    
    return total


if __name__ == "__main__":
    print(sum_until(10))
    print(sum_until(2))

'''
bugs found:
def sum_until(limit):
    total = 0
    i = 1
​
    while i < limit         #add ':' at the end of line and to contain the limit, the comparator must be 
        total += limit      #add i and not limit
        i = i - 1           # +
​
    return total
'''