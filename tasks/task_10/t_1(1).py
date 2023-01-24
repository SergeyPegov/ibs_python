lst =  ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'ДЯдя', 'брАт', 'Дядя', 'Дядя']

x = 0
i = 0
srt_lst = set()

dup = [x for i, x in enumerate(lst) if i != lst.index(x)]
for x in range(len(dup)):
    dup[x] = dup[x].lower()
x = 0
for x in range(len(lst)):
    lst[x] = lst[x].lower()
x = 0
index = 0
for index in range(len(lst)):
    if lst[index] not in dup:
        srt_lst.add(lst[index])

fltr_lst = list(srt_lst)

print(fltr_lst)