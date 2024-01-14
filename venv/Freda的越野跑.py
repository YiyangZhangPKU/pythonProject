n = int(input())
racer = list(map(int,input().split()))
count = 0

def mergeSort(lista):
    global count
    if len(lista) == 2:
        if lista[0] < lista[1]:
            lista[0],lista[1] = lista[1],lista[0]
            count += 1

    if len(lista) >2:
        mid = len(lista)//2
        lefthalf = lista[:mid]
        righthalf = lista[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j<len(righthalf):
            if lefthalf[i]>righthalf[j]:
                lista[k] = lefthalf[i]
                i+=1
            else:
                lista[k] = righthalf[j]
                j+=1
                count += len(lefthalf)-i
            k+=1
        while i<len(lefthalf):
            lista[k]=lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            lista[k]=righthalf[j]
            j+=1
            k+=1

mergeSort(racer)
print(count)
