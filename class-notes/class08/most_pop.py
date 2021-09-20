words = ["hello","water","hello","land","cloud","hello"]



def most_popular_word(item_list):
    word_count= {}
    pop_words = {}

    for item in item_list:
        if item in word_count:
            word_count[item] += 1
        else:
            word_count[item] =1
    print(word_count.key())

    #pop_words = sorted(word_count.item())

    #print(pop_words)






most_popular_word(words)
