#-*-coding:utf-8-*-
sum  = 0
n = 10
def add_num(n):
    if n ==1:
        return 1
    else:
        return  n+add_num(n-1)

print add_num(10)