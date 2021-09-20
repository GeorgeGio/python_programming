


def addition(x,y):
    return x+y



#print(addition(2,4))



def addition_n(*args):
    return sum(args)

#print(addition_n(2,4,6,8))


tuples_list= [(1,2),(2,3),(3,4)]

def addition_tuple(list_variable):

    total = 0

    for item in list_variable:

        total  += sum(item)


    return total





#print(addition_tuple(tuples_list))



def strip_vowel(some_string):
    new_stri = ""
    for char in some_string:
        if char not in "aeiou":
            new_stri += char
    return new_stri





#result = strip_vowel("hello world")
