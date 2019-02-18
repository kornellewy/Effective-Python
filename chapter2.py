# 1 way of good return 
def divide1(a,b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None

print("divide1(1,5)" + str(divide1(1,5)))
print("divide1(1,0)" + str(divide1(1,0)))

# 2 way of good return 
def divide2(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ValueError('invalid inputs') from e

try:
    divide2(2,1)
except ValueError:
    print("invalid input")
else:
    print("divide2(2,1)" + str(divide2(2,1)))

