def option_two():
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] =1
    current_popular_word = None
    max = 0
    for w in word_count:
        # print(w)
        # print(word_count[w])
        if word_count[w]>max:
            current_popular_word = w
            max = word_count[w]
            print(current_popular_word)
    print(word_count)
    return current_popular_word
cpw =  option_two()
print(cpw)

words = ["hello","water","hello","land","cloud","hello"]
