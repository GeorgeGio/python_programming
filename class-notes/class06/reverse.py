
# function reverse a list

#take in a my_l


def reverse_list(my_list):
    my_new_list = []
    for element in my_list[::-1]:
        my_new_list.append(element)

    return my_new_list




nums= [1,2,3,4,5]
reversed = reverse_list(nums)

print(reversed)
