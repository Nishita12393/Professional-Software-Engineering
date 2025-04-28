class NumberOperations:
    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

# Main program
num = int(input("Enter a number: "))
obj = NumberOperations()

if obj.is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")