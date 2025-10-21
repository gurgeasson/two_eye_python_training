'''
Instructions

    Define the function to accept a single parameter called num.
    Use a combination of <, > and and to create a contradiction in an if statement.
    If the condition is true, return True, otherwise return False. The trick here is that because we've written a contradiction, the condition should never be true, so we should expect to always return False.
'''

def always_false(num):
  if (num > 10 and num < 10):
      return True
  else:
      return False
  
print(always_false(0))
print(always_false(10))
