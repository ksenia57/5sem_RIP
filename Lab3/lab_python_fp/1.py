list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list(zip(list1,list2)))
list3 = list(map(lambda x: x+1,list1))
print(list3)