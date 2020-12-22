
def quicksort(list):
    if len(list)<=1:
        return list
    else:
        p = list.pop()
    l=[]
    u=[]
    for i in list:
        if i<p:
            l.append(i)
        else:
            u.append(i)
    return quicksort(l)+[p]+quicksort(u)
list=[9,8,7,5,6,2,1,4,3,5]
print(quicksort(list))
