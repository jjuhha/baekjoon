word = input()
def pe(word) :
    for i in range(len(word)) :
        if word[i] != word[len(word)-i-1] :
            print("0")
            return
    print("1")
pe(word)