def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def main():
    numbers_input = input("Enter numbers: ")
    try:
        numbers = [float(n) for n in numbers_input.split()]
        if not numbers:
            print("Invalid input.")
            return
        result = bubble_sort(numbers)
        print("Sorted:", end=" ")
        print(*result)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()