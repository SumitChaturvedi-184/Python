import os       

# renaming the day with tutorial
'''
for i in range(0,50):
  os.rename(f"data/day{i+1}",f"data/Tutorial{i+1}")
              #(source,Destination)

#if i thought to have changes in tutorial like adding space in can do this
'''
for i in range(0,50):
    os.rename(f"data/Tutorial{i+1}",f"data/Tutorial {i+1}")
                                                #space added
