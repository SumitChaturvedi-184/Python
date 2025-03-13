def fibonacci(n):
    fibo_series=[0,1]
    for i in range(2,n):
        fib=fibo_series[i-1]+fibo_series[i-2]
        fibo_series.append(fib)
    return fibo_series
print(fibonacci(8))

def fibonaccci(n):
    fib_series = [0,1]
    prenum = 0
    current_num = 1
    for i in range(0,n):
        prepre=prenum
        prenum=current_num
        current_num=prepre+prenum
        fib_series.append(current_num)
    return fib_series
       
print(fibonaccci(6))
