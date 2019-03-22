def sum_array(array):
    """The function returns the sum of items in array
    arg (int):
         array :list containing numerical values

    return:
        sum (int) : sum of items in array
    """
    if array:
        return array[-1] + sum_array(array[:-1])
    else :
        return 0

def fibonacci(n):
    """Return nth term in fibonacci sequence
    arg (int):
         n : nth term in fibonaci to calculate

    returns:
        int : nth term of fibonacci equal to sum of previous two terms
    """
    if n <= 1 :
        return n
    elif n > 1:
        return fibonacci( n - 1) + fibonacci( n -2)

def factorial(n):
     """function returns nth factorial

    arg (int):
         n(int) : nth factorial

    return:
         (int) :  return factorial of n
    """
    if n == 1:
        return n
    elif n > 1:
        return n*factorial(n-1)

def reverse(word):
     """Return word in reverse
    arg (int):
         word (str): word containg letters

    return:
        word (str) : word reversed
    """
    if word:
        return word[-1] + reverse(word[:-1])
    else:
        return word
