# list

subway = [10,20,30]
print(subway)

subway=['Yoo','Jo','Park']
print(subway.index('Jo'))

subway.append('haha')
subway.insert(1,'Jung')
print(subway)
subway.pop()

subway.append('Yoo')
subway.count('Yoo')

num_list = [5,2,4,2,1,3]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
# num_list.clear(); num_list

num_list.extend(subway)
num_list


# dictionary
cabinet={3:'Yoo',100:'Kim'}
print(cabinet[3])