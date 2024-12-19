def invest(amount, rate, years):
    c=amount*(1+rate/100)
    for i in range(1,years+1):
        print(f"year {i}: ${c:.2f}")
        c=c*(1+rate/100)
invest(100, 5, 4)