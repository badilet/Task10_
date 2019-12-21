# You are given a string.
# In the first line, print the third character of this string.
# In the second line, print the second to last character of this string.
# In the third line, print the first five characters of this string.
# In the fourth line, print all but the last two characters of this string.
# In the fifth line, print all the characters of this string with even indices
# (remember indexing starts at 0, so the characters are displayed starting with
# the first).
# In the sixth line, print all the characters of this string with odd indices i.e.
# starting with the second character in the string).
# In the seventh line, print all the characters of the string in reverse order.
# In the eighth line, print every second character of the string in reverse order,
# starting from the last one.
# In the ninth line, print the length of the given string.

a = input("Enter here:")
b = list(a)

#Line1
if len(a) <= 2:
    print("Line 1:", " ")
else:
    print("Line 1:", a[2])
#Line2
if len(a) <= 1:
    print("Line 2:", " ")
else:
    print("Line 2:", a[1:])
#Line3
if len(a) < 5:
    print("Line 3:", " ")
else:
    print("Line 3:", a[0:5])
#Line4
if len(a) <= 2:
    print("Line 4:", " ")
else:
    print("Line 4:", a[0:-2])
#Line5
if len(a) < 2:
    print("Line 5:", " ")
else:
    print("Line 5:", a[0:-1:2])
#Line6
if len(a) < 2:
    print("Line 6:", " ")
else:
    print("Line 6:", a[1:-1:2])
#Line7
print("Line 7:", a[::-1])
#Line8
print("Line 8:", a[::-2])
#Line9
print("Line 9:", len(a))







