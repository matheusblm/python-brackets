#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    # Write your code here 
    newBrackets = brackets
    if(len(brackets) % 2 != 0):
        return 'NO'
    for n in range(len(brackets)):
        newBrackets = newBrackets.replace("[]","").replace("()", "").replace("{" + "}", "")
    return "NO" if len(newBrackets) > 0 else "YES"