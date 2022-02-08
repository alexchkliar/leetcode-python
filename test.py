n = 10
i_count = 0
j_count = 0
k_count = 0
l_count = 0
m_count = 0

for i in range(0,n):
    i_count += 1
    for j in range(i,n):
        j_count += 1
        for k in range(j,n):
            k_count += 1
            for l in range(k,n):
                l_count += 1
                for m in range(l,n):
                    m_count += 1
print(i_count)
print(j_count)
print(k_count)
print(l_count)
print(m_count)
