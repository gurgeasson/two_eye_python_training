'''
Define a function called count_positives.
Accept a list of integers called numbers.
Count how many values are greater than 0.
Return the count.
Fix 4 bugs.
Optional: Improve the code using simple best practices.
'''

def count_positives(numbers):
    count = 0
    
    for n in numbers:
        if n > 0:
            count =+ 1
    
    return count


if __name__ == "__main__":
    print(count_positives([2, -1]))
    print(count_positives([0, 0, -1, 6.9, 7, 10]))

'''
bugs found:
def count_positives(numbers):
    count = 0
    
    for n in number:            #numbers - typo
        if n > "0":             #'0' is string
            count =+ 1
​                                #invalid char???
    return "count"              #sting
'''