import numpy

temp = [18, 24, 23, 22.5, 17, 26, 16]
average = round(numpy.average(temp),2)
print(f"The average temperature of the week is : {average}")
highest = numpy.max(temp)
lowest = numpy.min(temp)
print(f"The highest temperature in the week is {highest} whereas The lowest temperature is {lowest}")
f = []
indexes = []
for idx,x in enumerate(temp):
    y = x * 9/5 + 32
    f.append(y)
    if(x>20):
        indexes.append(idx + 1)
print(f"All the temperatures to farenheit are {f}")
print(f"The days by index where the temperature are above 20 are {indexes}")