class FactorialOperations:
    def factorial(self, x):
        if x < 0:
            return "Cannot be factorized"
        else:
            result = 1
            for i in range(1, x + 1):
                print("Before multiplying:", result)
                result *= i
                print("After multiplying:", result)
            return result

# Using the class
fact_op = FactorialOperations()
print(fact_op.factorial(5))