
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'i': 6}
 
merged_dict = {**{k: v for k, v in dict1.items() if v==3},
               **{k: v for k, v in dict2.items() if k in 'aeiou'}}
 
print(merged_dict)

x, _, y = (1, "ignored",3)
print(_)

names =["Nishita", "Ram", "Sam","Mark"]
ages = [20, 40, 30, 60]

paired = list(zip(names, ages))
print(paired)

ids = [1, 2, 3, 4]
names = ['Alice','Bob','Cathy','Mike']
grades = ['A', 'B', 'A+', 'A']

students = list(zip(ids, names, grades))
print(students)