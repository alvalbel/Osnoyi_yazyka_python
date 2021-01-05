import sys
salary = 0
if 'h' in sys.argv:
    print('Введите выработку в часах, почасовую ставку и премию через пробел')
else:
    script_name, hours, hourly_payment, premium = sys.argv
    salary = (int(hours) * int(hourly_payment)) + int(premium)
    print(f'Заработная плата составит: {salary}')




