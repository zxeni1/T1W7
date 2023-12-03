# Scope - global and local 

fname = "Pat"
lname = "Cummins"

def greet(): 
    fname = "Steven"
    lname = "Smith"
    print("Inside the fuction")
    print(fname)
    print(lname)

print("Outside the function")
print(fname)
print(lname)
greet()

#Outside the function prints first