class FactorialOperations:
    def __init__(self, x: int|str|list[int], y, z):
        self.x = x
        self.y = y
        if(self.y < 0):
           self.y = 0

    def factorial(this) -> int:
        if this.x < 0:
            raise ValueError("Invalid number. Number must be greater than zero.") 
        else:
            result = 1
            for i in range(1, this.x + 1):
                print("Before multiplying:", result)
                result *= i
                print("After multiplying:", result)
            return result


# Using the class
fact_op = FactorialOperations(1, -6, 7)
h = fact_op.factorial()
print(h)