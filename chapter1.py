"""
Chapter 1 style
"""

# good if
if 4 is not 5:
    print("4 is not 5")
# bad if
if not 4 is 5:
    print("ot 4 is 5")
# good check
KJN = []
if KJN:
    print(KJN)

print("jast use https://www.pylint.org/")
print("explanation: https://www.youtube.com/watch?v=fFY5103p5-c")

"""
str to bits
"""
def to_str(bytes_or_str):
    # to sprawdza czy bytes_or_str to bity
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    # to sprawdza czy bytes_or_str to str
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

"""
helper functions 
"""
