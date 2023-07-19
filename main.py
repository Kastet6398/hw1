# Function to select only numbers greater than 500
def is_number_bigger_than_500(element) -> bool:
    # Check if element is a number (int or float), and it's bigger than 500
    return isinstance(element, (int, float)) and element > 500


# Input data
some_data = [501, 'fff', 50, 0, -50.5, 'bat', 600, 358]

# Select only numbers which are bigger than 500 using built-in function filter(function, iterable)
selected_numbers = filter(is_number_bigger_than_500, some_data)

# Convert the result from iterator to list
selected_numbers_as_list = list(selected_numbers)

# Print the result
print(selected_numbers_as_list)
