HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    a = []
    for row in s:
        if row == (round(row ** 0.5)) ** 2:
            a.append(round(row ** 0.5))
    return a       
    
def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n ==3:
        return 3
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n == 1:
        return 1
    elif n ==2:
        return 2
    elif n == 3:
        return 3
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2*b + 3*a
        n = n-1
    return c

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
#############method 1, not using assign function##########
    def pingpong_next(k, num, up):
        if k == n:
            return num
        if up:
            return pingpong_switch(k + 1, num + 1, up)
        else:
            return pingpong_switch(k + 1, num - 1, up)

    def pingpong_switch(k, num, up):
        if has_seven(k) or k % 7 == 0:
            return pingpong_next(k, num, not up)
        else:
            return pingpong_next(k, num, up)
    
    return pingpong_next(1, 1, True)
##########################################################

#############alternative methon###########################
    if n <= 7:
        return n
    else:
        return direction(n) + pingpong(n-1)

def direction(n):
    if n < 7:
        return 1
    if (n - 1) % 7 == 0 or has_seven(n - 1):
        return -direction(n-1)
    else:
        return direction(n - 1)


##########################################################



#############method 2, using assign function##########
    i = 0
    sum = 0
    initial = 1
    while i < n:
        sum = sum + initial
        initial = switch(i + 1, initial)
        i+=1
    return sum

def switch(x, initial):
    if has_seven(x) or x % 7 == 0:
        return -initial
    else:
        return initial
#######################################################

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)



def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    i = count_power(amount)
    def count_total(x, amount):
        if x == 0:
            return 1
        elif 
    
    return count_change(i - 1, amount)    

def count_power(x):
    i = 0
    while 2**i <= x:
        i+=1
    return i-1

print(count_change(7))


###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
