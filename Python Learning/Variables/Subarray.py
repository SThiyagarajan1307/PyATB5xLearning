# Function to generate and print all continuous subarrays
def continuous_subarrays(arr):
    n = len(arr)
    count = 0
    print("Continuous Subarrays:")
    for start in range(n):  # Start index of the subarray
        for end in range(start, n):  # End index of the subarray
            count = count + 1
            print(arr[start:end + 1])
    print(count)

# Input from the user
user_input =input("Enter elements of the array separated by spaces: ")
array = list(map(int, user_input.split())) # Convert input to a list of integers

# Generate and print all continuous subarrays
continuous_subarrays(array)