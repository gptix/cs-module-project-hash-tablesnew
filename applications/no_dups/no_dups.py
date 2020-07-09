def no_dups(string_of_words):

    #stupid case
    if string_of_words == "":
        return ""
    
    #not stupid case
    words = string_of_words.split()
    words_seen = set()
    words_in_order = []
    
    for word in words:
        if word not in words_seen:
            words_seen.add(word)
            words_in_order.append(word)
    
    return " ".join(words_in_order)

    
if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))