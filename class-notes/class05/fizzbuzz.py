def FizzBuzz(number):


    if  ((number % 5 == 0 ) and (number %3 == 0) ):
        print("FizzBuzz")
    #fizz(number)
    elif number % 3 == 0:

        print("Fizz")
    #fizz(number)
    elif number % 5 ==0:
        print("Buzz")
    #fizz(number)
    else:
        print(number)




for number in range(1,102):
    #fizz(number)
    FizzBuzz(number)
