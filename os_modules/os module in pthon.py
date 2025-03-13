import os 

'''

if (not os.path.exists("os_modules/data")):
    os.mkdir("data")

for i in range(0,50):
    os.mkdir(f"data/Day{i+1}")

'''

print(os.getcwd())
os.chdir("/Users")
print(os.getcwd())

