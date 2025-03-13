questions = [
    [
        "  Current Railway Minister of India is","A. Mamta Banarjee","B. Ram Vilash","C. Ashwini Vaishnaw ","D. Piyush Goyala",2
    ],
    [
         "  Current Railway Minister of India is","A. Mamta Banarjee","B. Ram Vilash","C. Ashwini Vaishnaw ","D. Piyush Goyala",2
    ],
    [
         "  Current Railway Minister of India is","A. Mamta Banarjee","B. Ram Vilash","C. Ashwini Vaishnaw ","D. Piyush Goyala",2
    ],
    [
         "  Current Railway Minister of India is","A. Mamta Banarjee","B. Ram Vilash","C. Ashwini Vaishnaw ","D. Piyush Goyala",2
    ],
    [
         "  Current Railway Minister of India is","A. Mamta Banarjee","B. Ram Vilash","C. Ashwini Vaishnaw ","D. Piyush Goyala",2
    ],
    [
         "  Current Railway Minister of India is","A. Mamta Banarjee","B. Ram Vilash","C. Ashwini Vaishnaw ","D. Piyush Goyala",2
    ],
    [ 
         "  Current Railway Minister of India is","A. Mamta Banarjee","B. Ram Vilash","C. Ashwini Vaishnaw ","D. Piyush Goyala",2
     ]
]
money=0

level=[1000,2000,3000,4000,10000,12000,16000,18000,20000]

for i in range(0,len(questions)):
    question=questions[i]
    print(f"Queston for Rs.{level[i]}")
    print(f" {question[0]}")
    print(f"  {question[1]}    {question[2]}")
    print(f"  {question[3]}    {question[4]}")
    reply=int(input("Enter the Answer (1-4):"))
    if (reply==question[-1]):
        print(f"Correct Answer , You Have won Rs. {level[i]}")
        if (i==5):
           money=10000
        if (i==7):
            money=16000
        if (i==9):
            money=20000
    else:
     print("Wrong Answer")
     break
print(f"You Have Earned Money {money}")
