# Define the input and output file paths
input_file_path = '1.txt'
output_file_path = '2.txt'

# Open the input file in read mode
with open(input_file_path, 'r') as input_file:
    # Read all lines from the input file
    lines = input_file.readlines()

# Modify each line by adding a '+' character in front
modified_lines = ['+' + line.strip() for line in lines]

# Open the output file in write mode
with open(output_file_path, 'w') as output_file:
    # Write the modified lines to the output file
    output_file.write('\n'.join(modified_lines))

print("File has been modified and saved successfully!")
