import sys

# Manually set sys.argv for testing
sys.argv = ['script.py', 'test_arg1', 'test_arg2']

# Function to print command-line arguments
def print_args():
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")

# Test the function
print_args()