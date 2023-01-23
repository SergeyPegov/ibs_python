with open('test.txt' , 'r') as f:
    str = f.read()

with open('rev_test.txt' , 'w') as f2:
    rev_str = str[::-1]
    f2.write(rev_str)

with open('test.txt' , 'r') as f:
    print(f.read())
with open('rev_test.txt' , 'r') as f2:
    print(f2.read())



