input_string = "Hola"
print(len(input_string))
Slicing_input = input_string[1:3]
print(('1)') , Slicing_input)
print(('2)') , input_string[-3:-1]) # Converted negative Corresponding slicing
print(('3)') , input_string[:4]) # is same as [0:4]
print(('4)') , input_string[:4:1])  # Increment After putting slicing in input_string
print(('5)') , input_string[:4:-1]) 

print(('6)') , input_string.startswith("Hol")) # startswith return true or false based on Starting character
print(('7)') , input_string.endswith("ola")) # endsswith return true or false based on Ending character
print(('8)') , input_string.capitalize()) # Only give captial to first character in a string
print(('9)') , input_string.find("o")) # returns the index number of entered Character
print(('10)') , input_string.replace("o","w")) #replace the old character to new character

print(input_string)
