# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
months = 1

while principal > 0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        pay = payment + extra_payment
    else:
        pay = payment
    if pay > principal * (1+rate/12):
        pay = principal * (1+rate/12)
    principal = principal * (1+rate/12) - pay
    total_paid = total_paid + pay
    print(months, round(total_paid, 2), round(principal, 2))
    months = months + 1

print(f'Total paid {total_paid:0.2f}')