my_file = open("hello.txt")

print(my_file.read())

my_file.close()


my_file = open("hello.txt","w")

my_file.write("this is the second line")
