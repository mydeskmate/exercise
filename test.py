def maopao(lists):
    count = len(lists)
    while count > 0:
        i = 0
        while i < count-1:
            if lists[i] > lists[i+1]:
                print(lists)
                lists[i],lists[i+1] = lists[i+1],lists[i]
            i += 1
        count -= 1
    return lists
print(maopao([4,3,2,8,7,5]))
