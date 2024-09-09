class Math:
    def addNumbers(num1,num2):
        return num1 + num2

    def subtractNumbers(num1, num2):
        return num1 - num2

    def multiplyNumbers(num1, num2):
        return num1 * num2

    def divideNumbers(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error"

print(Math.addNumbers(5,8))
print(Math.subtractNumbers(7,2))
print(Math.multiplyNumbers(9,1))
print(Math.divideNumbers(6,2))
