def vatCalculator(x):
    return x + (x*0.07)
totalprice = float(input("Total price : "))
print(vatCalculator(totalprice))