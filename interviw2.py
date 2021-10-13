country_code=input("enter the country name::")
product_code=input("enter the product:")
weight_in_kg=float(input("enter the weight::"))
if country_code=="UK" or country_code=="uk":
    if product_code[0:3]=="123" :
        if weight_in_kg<5:
            print(5*1.2*(1+0.18))
        elif weight_in_kg>=5:
            shiffting_cost=15
            print(15*1.2*(1+0.18))
        else:
            print("no cvhange")
    elif country_code=="Uk" or country_code=="uk":
        if product_code[0:3]=="234" :
            if weight_in_kg<5:
                shiffting_cost=5
                print(5*1.5*(1+0.18))
            elif weight_in_kg>=5:
                shiffting_cost=15
                print(15*1.5*(1+0.18))
            else:
                print("no change")
        else:
            print(5*(1+0.18))
elif country_code=="US" or country_code=="us":
    if product_code[0:3]=="123":
        if weight_in_kg<10:
            print(5*1.2*(1+0.18))
        elif weight_in_kg>=10:
            shiffting_cost=15
            print(15*1.2*(1+0.18))
        else:
            print("no change")
    elif country_code=="US" or country_code=="us":
        if product_code[0:3]=="234" :
            if weight_in_kg<10:
                shiffting_cost=5
                print(5*1.5*(1+0.18))
            elif weight_in_kg>=10:
                shiffting_cost=15
                print(15*1.5*(1+0.18))
            else:
                print("no change")
        else:
            print(5*(1+0.18))
else:
    print("no change")




