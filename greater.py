def find_greatest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Example usage
a = 45
b = 22
c = 78

greatest = find_greatest(a, b, c)
print(f"The greatest number among {a}, {b}, and {c} is {greatest}.")
