def word_count(s):

    characters_to_remove = {'\'', '"', ':', ';', ',', '.', '-', '+', "'"
        '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&'}

    nochar = ''

    for c in characters_to_remove:
        s = s.replace(c, nochar)

    words = s.split()
    words_lower = [w.lower() for w in words]

    retval = {}

    for w in words_lower:
        if w not in retval:
            retval[w] = 0 # if an entry does not exist, create one
        retval[w] += 1
    
    return retval









if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))