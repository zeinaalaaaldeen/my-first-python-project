name =input("Enter the fist and last name of your friends separated by a comma: ").split(" ,")
abbreviated_names=""
for n in name:
    separated_name = n.split()
    print(separated _name)
    abbreviation=separated _name[0][0]  + "." + separated name[1][0] + "."
    abbreviated_names+=abbreviation 
print ("Abbreviated names are :")
for x in abbreviated_names:
    print(x)
