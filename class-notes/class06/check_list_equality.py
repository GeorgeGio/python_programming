# check a li of equality
# make a function which will take two listt and return a boolean


def check_list_equality(list_one, list_two):

    #check lists are the same size
    #if not the same size retun False
    #check each element at same index are equal
    #if same size and index retun TRue

    if len(list_one) != len(list_two):
        return False

    for index in range(len(list_one)):
        if list_one[index] != list_two[index]
        retun False

    

a= ['a','b','c','d']
b= ['a','b','c','d']


result = check_list_equality(a,b)
print(result)
