class NumbOperations:
    def is_prime(self, numb):
        if numb < 2:
            return False
        for i in range(2, numb):
            if numb % i == 0:
                return False
        return True

    def factorial(self, numb):
        result = 1
        for i in range(1, numb + 1):
            result *= i
        return result

num = int(input("Enter a number: "))
obj = NumbOperations()

print(f"{num} is {'a Prime' if obj.is_prime(num) else 'NOT a Prime'} Number.")
print(f"Factorial of {num} is {obj.factorial(num)}.")
