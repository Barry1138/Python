from decimal import *

item = Decimal(0.70)
rate = Decimal(1.05)

tax = item * rate
total = item + tax

print('Item:\t', '{:.2f}'.format(item))
print('Tax:\t', '{:.2f}'.format(tax))
print('Total:\t', '{:.2f}'.format(total))
