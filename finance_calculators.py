import math
while True:
    print("Choose either 'Investment' or 'Bond' from the menu below to proceed: \n")
    task = input("@ invesment - to calculate the amount of interest you will earn on your investment\n@ bond - to calculate the amount of pay on a home loan: \n")
    task = task.lower()
    if task == 'investment' or task == 'bond' :
        break
    
print(f'Thanks for choosing {task} service')


if task.lower() == 'investment' :

    deposit = float(input('what amount of money you want to deposit: '))
    interest_rate= float(input('what interest rate do you have: ' ))
    year = int(input('Numbers of the year plan of investing:  '))
    interest = input('Type of interest you want: \n Simple or Compound: ')

    new_interest = (interest_rate)/100
    #print(new_interest)

    if interest.lower() ==  'simple' :
        #a = p(1+r*t)
        interest_amount = deposit * (1 + new_interest * year)
        #print(interest_amount)
        print(f"\n Total amount after simple intrest is £ {interest_amount}")
    elif interest.lower() ==  'compound' :
        # a = p(1+r)^t
        # a = p* math.pow((1+r),t)
        interest_amount = deposit*math.pow((1+new_interest),year)
        print(f"\n Total amount after compound intrest is £{interest_amount}")

elif task.lower() == "bond" :
    house_value = float(input('what is your house value: '))
    interest_rate= float(input('what interest rate do you have : ' ))
    months = float(input('Numbers of the months plan to repay loan:  '))
    new_interest = (interest_rate)/100

    #monthly interest rate is interest rate divide by 12
    monthly_interest_rate = new_interest / 12

    # x = (i.p)/(1 - (1+i)^(-n))
    
    amount_repay = (monthly_interest_rate*house_value)/(1-math.pow((1+monthly_interest_rate),(-months)))
    #print(amount_repay)
   
    print(f"\n every month you pay £{amount_repay}")