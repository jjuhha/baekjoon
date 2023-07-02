word = input()
forbidden = 'CAMBRIDGE'
result = []

for i in range(len(word)) :
    if word[i] not in forbidden :
        result.append(word[i])
print(''.join(result))