def increment_percentage(number, increment_by_percentage, times):
    value = []
    value.append(number)
    for i in range(times-1):
        value.append(number + number * increment_by_percentage / 100)
        number += number * increment_by_percentage / 100
    return value
print(increment_percentage(5, 50, 10))