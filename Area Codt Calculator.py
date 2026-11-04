print("Welcome to Area Cost Calculator")
length =input('please type length ')
width= input('please type width ')
cost_for_one_meter=input('How much for one meter ? ')
area = float(length)*float(width)
print(f'The total area is {area}')
cost = float (cost_for_one_meter)* area
print(f'Give the guy {cost}$')