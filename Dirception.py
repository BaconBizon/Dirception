import os
import fileinput

path = "C:/Users/user/..."

print("How many directories do you want?")

for line in fileinput.input():
    for i in range(int(line)):
        dir = "Dir" + str(i)
        if not os.path.exists(dir):
            os.makedirs(dir)
        
        path += "/" + dir
        try:
            os.chdir(path)
            
        except (OSError):
            pass

    break
