a_file = open("new_text.txt")
file_contents = a_file.read()

second_file = open("new_file2.txt","w")
second_file.write(file_contents)

a_file.read()
