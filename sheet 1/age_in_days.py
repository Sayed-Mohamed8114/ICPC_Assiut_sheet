n=int(input())
remain_months=n%365
years=int(n/365)
remain_days=remain_months%30
months=int(remain_months/30)
days=remain_days

print(f"{years} years")
print(f"{months} months")
print(f"{days} days")