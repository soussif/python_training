read = open("zmlony0201_old.txt", "r")
print(read.readable())
# print(read.readlines())
# read.close()

append = open("zmlony0201_old.txt", "a")
append.write("\nTest text")
append.close()

overwrite = open("index.html", "w")
overwrite.write("<p>This is a Test HTML</p>")
overwrite.close()