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