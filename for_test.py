query = [
 ('Fuits', 0, 'fruits', None),
 ('Vegetables', 0, 'vegetables', None),
 ('Apples', 1, 'apples', 'fruits'),
 ('Mango', 1, 'mango', 'fruits'),
 ('Red apple', 2, 'red_apple', 'apples'),
 ('Green apple', 2, 'green_apple', 'apples')
 ]


branches = []

for tup in query:
    if tup[1] == 0:
        branches.append([tup[2]])
    else:
        print(branches)
        for s in branches:
            if tup[3] in s:
                s.append(tup[2])
                print(branches.index(s))
