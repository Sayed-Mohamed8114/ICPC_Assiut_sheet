discount,price_after=map(int,input().split())
price=(price_after/(1-(discount/100)))
print(f"{price:.2f}")