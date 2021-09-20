def add_two(number):
    total = number + 2
    print(total, 'calculated in function')

    return total



result_1 = add_two(1)
result_2 = add_two(2)

final_result = result_1 + result_2

print("the final result is :", final_result)
