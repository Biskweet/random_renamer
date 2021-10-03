import os, random, string

path = input("What is your directory path? (WARNING: \n" \
             "1 - You must use slashes `/` for delimiting subfolders\n" \
             "2 - EVERYTHING in the directory will be renamed\n>>> ")

if path[-1] != "/":
    path += "/"

files = os.listdir(path)
used = []
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

for file in files:
    filename, file_extension = os.path.splitext(path + file)

    new_name = ""
    for _ in range(20):
        new_name += random.choice(chars)
    
    os.rename(path + file, path + new_name + file_extension)
    print(f"{file} => {new_name + file_extension}")

print("Done.")
input("Press enter to close the program...")