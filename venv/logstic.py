n=int(input())
ans=[]
for i in range(n):
    dic1={}
    xishu=[]
    mi=[]
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for j in range(1,len(a),2):
        if a[j]>=0:
            if a[j] in mi:
                xishu[mi.index(a[j])]+=a[j-1]
            else:
                xishu.append(a[j-1])
                mi.append(a[j])
        else:
            dic1=dict(zip(mi,xishu))
            break
        dic1=dict(zip(mi,xishu))
    xishu=[]
    mi=[]
#    dic2 ={}
    for j in range(1,len(b),2):
        if b[j]>=0:
            if b[j] in mi:
                xishu[mi.index(b[j])]+=b[j-1]
            else:
                xishu.append(b[j-1])
                mi.append(b[j])
        else:
            dic2=dict(zip(mi,xishu))
            break
        dic2=dict(zip(mi,xishu))
    for key1 in dic1.keys():
        if key1 in dic2.keys():
            dic2[key1]=dic2[key1]+dic1[key1]
        else:
            dic2[key1]=dic1[key1]
    if dic2[key1] == 0:
        dic2.pop(key1)
    dict_sort=dict(sorted(dic2.items(),key=lambda x:x[0],reverse=True))
    key_value=[]
    for i,j in dict_sort.items():
        key_value.append("["+" "+str(j)+" "+str(i)+" "+"]")
    ans.append(" ".join(key_value))
for i in range(n):
    print(ans[i])