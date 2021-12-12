# Python program to check if a string is palindrome or not
# Solution No. 1
 
x = "madam"
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
    print("Yes")
else:
    print("No")

    
   
# Solution No. 2
# using function 
 
def Palindrome(string):
    return string == string[::-1]
 
# Driver code

string = "malayalam"
res = Palindrome(string)
 
if res:
    print("Yes")
else:
    print("No")