def reFun_A(n):
    if n < 0:
        return 'X'
    return str(n) + '-' +reFun_A(n-5)

print(reFun_A(20))

print('**********************\n')

def reFun_B(n):
    if n < 0:
        return 'X'
    return reFun_B(n-5) + '-' + str(n)

print(reFun_B(20))
print('**********************\n')

def reFun_C(st):
    if len(st)==1: return st
    if len(st) == 0: return ''
    return st[1]+reFun_C(st[1:len(st)-1])+st[0]

print(reFun_C("Structure"))
print('**********************\n')

def reFun_D(n, alist):
    if n==0: return
    alist[n-1]+=alist[n]
    reFun_D(n-1, alist)

alist = [2]*10
reFun_D(len(alist)-1, alist)
print(alist)
print('**********************\n')

def reFun_E(alist):
    end = len(alist)-1
    for i in range(len(alist)//2):
        alist[i], alist[end-i] = alist[end-i], alist[i]
alist = list(range(2, 30, 3))
reFun_E(alist)
print(alist)
print('**********************\n')
