income=int(input("Enter your income"))
dependent=int(input("enter the number of depends"))
tax_income=income-10000-(dependent*3000)
tax=0.2*tax_income
print("the amount of tax to be paid is $",tax)