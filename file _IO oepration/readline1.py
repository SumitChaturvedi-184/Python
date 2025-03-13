i=0
f = open('errortest.txt','r')
while True:
    i+=1
    line = f.readline()
    if not line:
        break
    mark=line.strip().split(" , ")
    try:
        m1 = mark[0]
        m2 = mark[1]
        m3 = mark[2]
        print(f"The marks for student {i} is : {m1}")
        print(f"The marks for student {i} is : {m2}")
        print(f"The marks for student {i} is : {m3}")
        print(line)
    except IndexError as e:
        print(f"Error processing line {i}: {line.strip()}")
        print(f"Error details: {e}")