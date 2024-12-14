#Series of Changes
def series(a):
    result = []
    for i in range(1, a * 2 + 1, 2):
        result.append(i)
    return result

a = int(input("Enter a number: "))
print(series(a))