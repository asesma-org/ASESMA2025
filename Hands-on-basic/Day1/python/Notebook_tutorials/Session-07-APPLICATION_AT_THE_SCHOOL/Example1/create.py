""" 
In order to create a newfile or overwrite an existing one use "w"
To add content to an existing file use "a"
"""
# create a new file and add information
with open("createfile.txt", "w") as file: 
    file.write("Information")

# Append information to existing file
# Uncomment the next section then execute
# with open("filename.txt", "a") as file:
#     file.write("\nMore information")