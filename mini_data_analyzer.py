# mini_data_analyzer.py

def get_numbers():
    """Takes input from user and returns a list of numbers."""
    try:
        data = input("Enter numbers separated by spaces: ")
        numbers = [float(num) for num in data.split()]
        return numbers
    except ValueError:
        print("❌ Invalid input! Please enter only numbers separated by spaces.")
        return None

# [float(num) for num in data.split()]
# This list comprehension does all of the above in one line:
# Iterates over each string number
# Converts it to a float
# Collects all floats into a new list


def calculate_count(numbers):
    """Returns the count of numbers."""
    return len(numbers)


def calculate_max(numbers):
    """Returns the maximum value."""
    return max(numbers)


def calculate_min(numbers):
    """Returns the minimum value."""
    return min(numbers)


def calculate_sum(numbers):
    """Returns the sum of numbers."""
    return sum(numbers)


def calculate_average(numbers):
    """Returns the average of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0


def main():
    numbers = get_numbers()
    if numbers is None or len(numbers) == 0:
        print("⚠️ No valid data to analyze.")
        return

    print("\n📊 Data Analysis Results 📊")
    print(f"Count   : {calculate_count(numbers)}")
    print(f"Maximum : {calculate_max(numbers)}")
    print(f"Minimum : {calculate_min(numbers)}")
    print(f"Sum     : {calculate_sum(numbers)}")
    print(f"Average : {calculate_average(numbers):.2f}")


if __name__ == "__main__":
    main()
