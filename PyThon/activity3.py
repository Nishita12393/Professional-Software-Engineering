def factorial (x):
    if x<0:
        return "cannot be factorized"
    else:
        result = 1
        for i in range(1,x+1):
            print (result)
            result *= i
            print("after:",result)
        return result
print (factorial(5))