bill_amount = float(input())
tip_percentage = float(input())
num_people = int(input())  # number of people splitting the bill.

print('Bill Split Calculator')

total = bill_amount * ((tip_percentage / 100) + 1)
print(f'Total (including tip): {total:.1f}')

amount_per_person = total/num_people
print(f'Each person pays: ${amount_per_person:.1f}')
