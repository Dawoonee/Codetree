N = int(input())

def func(num):
    if num == 0:
        return
        
    print(num,end=' ')
    func(num - 1)
    print(num,end=' ')

func(N)