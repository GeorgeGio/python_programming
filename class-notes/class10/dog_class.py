class Dog:
  total_dogs = 0
  def __init__(self, name="", age=0):
    self.name = name
    self.age = age
    Dog.total_dogs += 1 #  We can increment this here!
    print(name, "created:")

  def bark_hello(self):
    print("Woof! I am called", self.name, "; I am", self.age, "human-years old.")
    print("There are", Dog.total_dogs, "dogs in this room!")

molly = Dog("Molly", 8)
molly.bark_hello()

sheera = Dog("Sheera", 5)
sheera.bark_hello()
