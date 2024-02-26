x = "aditya"

for x in "ADITYA":
    print(f"Values of x : {x} , {ord(x)}")


first = "Aditya"
last = "Sharma"

print(f"REsult is : {first} {last}")
print(first+" "+last) #concat
print(f'MY name is {first  +" "+ last}')

hers = "aditya's"
print(hers)


s1 = chr(72)
s2 = chr(105)

print(s1 + s2)

print(chr(8710))


print("This will be on\nNew line")





quote = "Then he said \"Hello\" to me"

print(quote)


name = "Aditya"
age = 21
# print(name + " " + age) # throws error
print(f"{name} {age}")

# one more of writing above 

print("My name is %s and i am %i year old " %(name,age))

# MORE STRING OPERATIONS 

testString = "Adi,tya"

print(len(testString)) #Return length

print(testString * 2) #Repeat
print(testString.replace("tya","Bro")) #Replace
print(testString.split(",")) #Split string based on ,
print(testString.startswith("A")) #Case sensitive
print(testString.endswith('a')) #Case Sensitive
print(testString.upper())
print(testString.lower())



# SLICING THE STRING 

s = "ThisisTest"

print(s[0:4])
print(s[1:])
print(s[-6:])
print(s[2:7])