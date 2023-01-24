lst =  ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'ДЯдя', 'брАт', 'Дядя', 'Дядя']

def dublic(q):
    x = 0
    i = 0
    dup = [y for i, y in enumerate(q) if i != q.index(y)]
    for i in range(len(dup)):
        dup[i] = dup[i].lower()
    return dup

def foo(q):
    srt_lst = set()
    index = 0
    x = 0
    for index in range(len(q)):
        if q[index].lower() not in dublic(q):
            srt_lst.add(q[index].lower())
    res = list(srt_lst)
    return res


print(foo(lst))