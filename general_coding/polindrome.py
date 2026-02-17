"""
def palindrome_check(element):
    rem =0
    while element>0:
        rem = rem*10 +element%10
        element = element//10
    return rem


_num = 1221
rev_num = palindrome_check(_num)
if _num==rev_num:
    print("polindromic number")
else:
    print("not poolindromic")
"""


def palindrome_check(element):
    if element == element[::-1]:
        return True
    else:
        return False

_string = "madam"
print(palindrome_check(_string))

