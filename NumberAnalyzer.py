nums = []
while True:
    num_input = input("Enter a number (type 'done' to finish): ")
    if num_input.lower() == "done":
        break
    try:
        nums.append(int(num_input))
    except ValueError:
        print("Please enter a valid integer.")


def calculate_length_of_nums(lis):
    return len(lis)


def calculate_sum_of_nums(lis):
    return sum(lis)


def calculate_avg_of_nums(lis):
    return sum(lis) / len(lis)


def calculate_min_of_nums(lis):
    return min(lis)


def calculate_max_of_nums(lis):
    return max(lis)


print("Amount of numbers you inserted : " + str(calculate_length_of_nums(nums)))
print("Sum of numbers you inserted : " + str(calculate_sum_of_nums(nums)))
print("Average of numbers you inserted : " + str(calculate_avg_of_nums(nums)))
print("Maximum of numbers you inserted : " + str(calculate_max_of_nums(nums)))
print("Minimum of numbers you inserted : " + str(calculate_min_of_nums(nums)))
