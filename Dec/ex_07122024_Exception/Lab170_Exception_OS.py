import os

print(os.getcwd())
# Returns the current working directory

# List files in the current directory
files = os.listdir('C:/Users/LINEYSHA SRI/OneDrive/Documents/Onedrive/Documents')
print(f"Files in current directory: {files}")

# Create a new directory
# os.mkdir('Test2')

# Check if a file exists
file_exist = os.path.exists("thiyaga.txt")
print(file_exist)


print(os.name) # posix == mac, nt - windows