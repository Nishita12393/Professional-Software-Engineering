
id = [1, 2, 3,4]
name = ["Alice", "Bob", "Cathy", "Mike"]
grades = ["A", "B", "A+", "A"]
 
students = dict(zip(id, zip(name, grades)))
print(students)

def func():

    data = []
    for i in range(4):
        data.append(lambda a, i=i*2: i*a)
    return data

funcs = func()

for f in funcs:
    print(f(5))


def make_multiplier(factor):
    def multiplier(a):
        return factor * a
    return multiplier
data = []
for i in range(5):
    data.append(make_multiplier(i * 2))
print(data[4](5))