import os 
folders = os.listdir("data")

print(folders)

# ye hame saari directories ke under se file
# btayega example maine Tutorial 2 me ek file 
#bana kar save ki hai example.py ke naam se


print(os.getcwd())
os.chdir("/python")
print(os.getcwd())

'''
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
    '''

#for folder in folders:
#    print(os.listdir(f"data/{folder}"))