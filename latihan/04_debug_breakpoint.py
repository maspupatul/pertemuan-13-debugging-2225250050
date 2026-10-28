
def rata_rata(data):
    if len(data) == 0:
        return None

    total = sum(data)
    return total / len(data)


print("Test 1:", rata_rata([80, 90, 70]))
print("Test 2:", rata_rata([100, 80]))
print("Test 3:", rata_rata([]))

      
