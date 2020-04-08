import os
path=os.getcwd()

#print(path)
os.chdir(r"C:\Users\user\Dropbox\Eric\Vrep_python_working_folder\b1")

path=os.getcwd()
print(path)

f = open("B1_texto1.txt", "r")
print(f.read())
