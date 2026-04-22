running_total = 0

num_of_friends = int(input('How many friends are splitting the bill? '))

appetizers = float(input("Enter the cost of appetizers total: "))
main_courses = float(input("Enter the cost of main courses total: "))
desserts = float(input("Enter the cost of desserts total: "))
drinks = float(input("Enter the cost of drinks total: "))

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip_input = input('What percentage tip would you like to give? (e.g., 25 or 25%): ')
tip_input = tip_input.replace('%', '')

tip_percentage = float(tip_input)

tip = running_total * (tip_percentage / 100)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill, 2)
print(f'Each person pays: ${each_pays:.2f}')
