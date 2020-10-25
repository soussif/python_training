#make sure if you open a file  and an error happens it still close it , it does same as try and except

with open("file.txt", "w") as file:
    file.write("hello")

# it's the same or equal in code to the below
# file = open("file.txt", "w")
# try:
#     file.write("hello")
# finally:
#     file.close()