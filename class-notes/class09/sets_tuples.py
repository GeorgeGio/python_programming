

food_list = ["fish","steak","pasta","soup"]
food_set = {"fish","steak","pasta","soup"}
food_tuple = ("fish","steak","pasta","soup")

#print(food_list)
#print(food_set)
#print(food_tuple)

new_list = set(food_list)

food_set.add("pizza")
food_list.insert(0,"pizza")
food_list.append("eggs")



print(food_list)

food_list.remove("pizza")
food_set.remove("pizza")



print(food_list)

food_list.insert(1,"popcorn")
#food_list[1]= "popcorn"
second_element = food_list.pop(2)
food_list.instert(0,second_element)

print(food_list[0])
print(food_tuple[0])


for food in food_list:
    print(food)
for food in food_set:
    print(food)
for food in food_tuple:
    print(food)





#print(food_set)
#print(food_tuple)
