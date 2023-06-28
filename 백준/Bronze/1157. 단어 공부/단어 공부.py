word = input()
word = word.upper()
alphabet_dic = {}

for i in range(len(word)) :
    if word[i] in alphabet_dic:
        alphabet_dic[word[i]] += 1
    else :
        alphabet_dic[word[i]] = 1

max_key = max(alphabet_dic, key=alphabet_dic.get)
if sum(1 for key in alphabet_dic if alphabet_dic[key] == alphabet_dic[max_key]) >= 2 :
    print("?")
else :
    print(max_key)