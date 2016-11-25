def array_left_rotation(a, n, k):
    a = list(a)
    i = 0
    save = k
    while(k!=0):
        a.append(a[i])
        i = i+1
        k = k-1
    return a[save:]
n, k = map(int, input().strip().split(' '))
a = map(int, input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

