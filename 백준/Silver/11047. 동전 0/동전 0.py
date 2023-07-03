N, K = map(int, input().split())
m_list = []
count = 0
for i in range(N) :
    m_list.append(int(input()))
m_list.sort(reverse=True)
# print(m_list)

for i in range(len(m_list)) :
    if m_list[i] <= K :
        count += K // m_list[i]
        K = K % m_list[i]
print(count)