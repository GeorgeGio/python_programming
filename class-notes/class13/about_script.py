user_name = input("What is your name?:  ")
user_fav_food = input("what is your favourite food? :    ")

with open("about_me.txt","w") as my_file:
    my_file.write(f"the users name is : {user_name} \n his favourite food is :{user_fav_food}")
