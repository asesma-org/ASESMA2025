"""
Editing files in python
"""
############################
# Read a file using python #
############################
with open("editfile.txt", "r") as file:
    lines = file.readlines() # readlines puts lines in a list

# Insert at line 1 (index 0)
lines.insert(0, "Welcome to the 8th ASESMA.\n")

with open("editfile.txt", "w") as file:
    file.writelines(lines)