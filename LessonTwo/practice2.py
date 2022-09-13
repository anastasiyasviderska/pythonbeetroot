dogs = "Dogs like cats"
cats = "Cats like dogs"
partition_var1 = cats.partition ("like")
partition_var2 = dogs.partition ("like")
new1_dogs = " ".join([partition_var2[0],"don't",partition_var1[1],partition_var2[2]])
new1_cats = " ".join([partition_var1[0],"don't",partition_var2[1],partition_var1[2]])
print("".join([partition_var2[0],partition_var2[1],partition_var1[2]]))
print("".join([partition_var1[0],partition_var1[1],partition_var2[2]]))
print("".join([partition_var2[0],"don't ", partition_var1[1],partition_var2[2], ", and",partition_var2[2]," don't ", partition_var1[1], partition_var1[2]]))
quantity_cats= new1_cats.casefold().count("cats")
quantity_dogs=new1_dogs.casefold().count("dogs")
print(f"Word dogs exist in this two sentences: {quantity_dogs} times. Word cats exist in this two sentences: {quantity_cats}" )
# count the number of cats and dogs in both sentences at a time
lower_var = (dogs + cats).lower()
print (f"The number of dogs is {lower_var.count('dogs')}")
print (f"The number of cats is {lower_var.count('cats')}")

# Mix the letters in both sentences according to order solution found on stackoverflow
# https://stackoverflow.com/questions/48403767/merge-two-strings-with-alternate-chars-as-output

print ("".join(map("".join, zip(dogs,cats))))