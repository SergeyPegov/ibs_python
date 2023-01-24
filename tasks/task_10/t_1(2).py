lst =  ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'ДЯдя', 'брАт', 'Дядя', 'Дядя']

def duplic(x):
    y = 0
    i = 0
    dup = [y for i, y in enumerate(x) if i != x.index(y)]
    return dup

def foo(x):
    srt_lst = set()
    for i in range(len(duplic.dup)):
        duplic.dup[i] = duplic.dup[i].lower()
    index = 0
    for index in range(len(x)):
        if x[index] not in duplic.dup:
            srt_lst.add(x[index])
    res = list(srt_lst)
    return res

test = filter(lst, foo)
print(test)