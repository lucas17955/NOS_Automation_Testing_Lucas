import sys
import os
print(sys.path)

# Get the current directory
current_dir = os.getcwd()

# Add the current directory to the Python path
sys.path.append(current_dir)
print(sys.path)