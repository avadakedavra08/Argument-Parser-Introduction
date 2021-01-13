'''

vars() function : The vars() function returns the __dic__ attribute of an object.

The __dict__ attribute is a dictionary containing the object's changeable attributes.
 calling the vars() function without parameters will return a dictionary containing the local symbol table.

'''

class TestFunction :
    name = "Harry"
    charac = "Potter"

    def func(self):
        var = 3
        print(self.name,self.charac)

# Testing the vars() function
print("vars() with no argument -> Local Symbol Table")
x = vars()
print(x,"\n")


x = vars(TestFunction)
print(x,"\n")

# Accessing the class object
obj = TestFunction()
obj.func()

# vars() can access the attributes in the form of a dictionary and not th local
# function directory. So, below code throws an error, as there is no __dict__ attribute
# to display.
# p = vars(obj.func())
# print(p)

'''
cv2.imread() : 



'''