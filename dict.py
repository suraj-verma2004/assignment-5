students={
    "Alice":90,
    "Mark":91,
    "Alexander":87,
    "Tom":67
}
name=input("Enter Student Name")
if name in students:
    print("{} got {} marks".format(name,students[name]))
else:
    print("{} not found in students list".format(name))