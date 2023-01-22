

dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}

new_d = {}
for k in dict.keys():
    if dict[k] >=3:
        new_d[k] = dict[k]

print(new_d)