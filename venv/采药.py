Time,m_num = map(int,input().split())
maptable = [[0 for i in range (Time+1)]for j in range(m_num+1)]
casetable = [0]
for i in range(m_num):
    timetemp,valuetemp = map(int,input().split())
    casetable.append((timetemp,valuetemp))
for i in range(Time+1):
    maptable[1][i] = casetable[1][1] if casetable[1][0] <= i else 0
for i in range(2,m_num+1):
    for j in range(Time+1):
        quest = (maptable[i-1][j-(casetable[i][0])]+ casetable[i][1]) if (j-casetable[i][0] >= 0) else 0
        maptable[i][j] = max(maptable[i-1][j],quest)

print(maptable[m_num][Time])



