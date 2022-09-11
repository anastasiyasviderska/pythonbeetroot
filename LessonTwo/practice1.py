string = "Once in a while, in a far-far kingdom"
dots = "..."
partition_var = string.partition("kingdom")
translation = string.maketrans("k", "K")
print (string.count(" in "))
print (string.replace(", ", " "))
print (string + "...")
print ("".join([string, dots]))
print (string, end= "...\n")
print (string.replace("kingdom", "Kingdom"))
print ("".join ([partition_var[0],partition_var[1].capitalize()]))
print(string.translate(translation))