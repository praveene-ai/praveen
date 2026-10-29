
def add(a, b):
    return a + b


def average(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")

    return sum(numbers) / len(numbers)
