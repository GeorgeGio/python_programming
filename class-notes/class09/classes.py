class Dog:

    #consructor function
    def __init__(self,name, age):
        #attributes

        self.name = name
        self.age = age
        print ("Created!!")

    def bark(self,num=1):
        print("woof"*num)


corgi = Dog('Rex',1)

print(corgi.name)
print(corgi.age)

sheepdog = Dog('Marshmallow',9)
print(sheepdog.name , sheepdog.age)

sheepdog.bark(10)
corgi.bark()
