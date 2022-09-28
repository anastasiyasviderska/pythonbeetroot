# the file shows in the directory where i ran my scripts
# when i ran the script from other directory the file is 
# created in the directory where it was ran not where script was created

with open ('myfile_1.txt') as file_object:
    my_file = file_object.read()
    file_object.close()

print(my_file)