# To find exactly where that file is:

# import os
# print("File created at:", os.path.abspath("Moss.txt"))


# To open and read file : 

# file_1 = open("Moss.txt")
# print(file_1.read())
# file_1.close()


# To write something in file :                                  Do overwrite 

# file_1 = open("Moss.txt","w")
# file_1.write("")
# file_1.close()


# To write something at the end and show at the same time.       Do not overwrite

# file_1 = open("Moss.txt","a+")
# file_1.write("\nMosses are often the very first organisms to grow on bare rock or sterile soil.")
# file_1.seek(0)
# print(file_1.read())
# file_1.close()

# Open for reading and writing. The (stream / pointer / cursor) is positioned at the beginning of the file.

# file_1 = open("Red Fort.txt","r+")
# file_1.seek(4)                    # But We change pointer by seek function
# # file_1.write("Happy Coding")
# file_1.seek(0)
# print(file_1.read())
# file_1.close

# Open for reading and writing.The file is created if it does not exist, otherwise it is truncated.The stream is positioned at the beginning of the file.

# file_1 = open("Red Fort.txt","w+")
# file_1.write("Constructed from striking red sandstone, its high walls enclose a complex of palaces, halls, and gardens.")
# file_1.seek(0)
# print(file_1.read())
# file_1.close()


