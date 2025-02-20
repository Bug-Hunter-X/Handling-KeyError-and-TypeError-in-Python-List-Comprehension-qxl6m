def function_with_uncommon_error(data):
    try:
        # Assume 'data' is a list of dictionaries
        result = [item['value'] for item in data if 'value' in item]
        return result
    except (KeyError, TypeError) as e:
        # Handle KeyError if 'value' key is missing and TypeError if data is not a list of dictionaries
        print(f"An error occurred: {e}")
        return []  # Return empty list on error

data = [{'value': 1}, {'key': 2}, {'value': 3}]
result = function_with_uncommon_error(data)
print(result)  # Output: [1, 3]

data = [{'value': 1}, {'value': 'a'}, {'value': 3}]
result = function_with_uncommon_error(data)
print(result) # Output: [1, 'a', 3]

data = None
result = function_with_uncommon_error(data)
print(result) # Output: An error occurred: 'NoneType' object is not iterable
[]
