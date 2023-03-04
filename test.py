# Define your original array with the variable containing the code
# original_array = ['1', '2', '3', '4', '5']

# Create an empty dictionary to store the new arrays with their respective variable names
new_arrays = {}

# Loop through the original array and check each element against a condition
# for code in original_array:
#     if code == '2':
        # If the condition is met, create a new array with a variable name containing the code
# userInput = input("Type a number to create an array with said number: ")        
        
new_array = [userInput]
var_name = 'array_' + userInput
new_arrays[var_name] = new_array

# Print the new arrays with their respective variable names
print(new_arrays)

new_arrays[f'array_{userInput}'].append('test1')
# new_arrays[f'array_{userInput}'].append('test2')
# new_arrays[f'array_{userInput}'].append('test3')
new_arrays[f'array_{userInput}'].pop(0)

# print(new_arrays[f'array_{userInput}'])
# for i in range(len(new_arrays[f'array_{userInput}'])):
#     print(new_arrays[f'array_{userInput}'][i])
# # Access and append to array_code3
# new_arrays[f'array_code2'].append('new_code')

# # Print the updated array_code3
# print(new_arrays['array_code2'])