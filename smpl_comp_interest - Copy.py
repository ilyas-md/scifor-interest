def yash(principal,rate,time):
    print("//SIMPLE INTEREST AMOUNT OF YASH//")
    interest_amt = (principal*rate*time)/100
    print("Interest Amount:",interest_amt)
    total_amt = (interest_amt+principal)
    print("Total Balance Amount for 30 years: ",total_amt)
yash(10000,6,30)

def vishal(principal,rate,time):
    amt = principal * (1 + rate/100)**time
    print("//COMPOUND INTEREST OF VISHAL//")
    print("TOTAL AMOUNT: ",amt)
    print("INTEREST AMOUNT PER YEAR: ",amt/time)
vishal(10000,6,30)