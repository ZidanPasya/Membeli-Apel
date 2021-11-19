apple_price = 3000
money = 50000

input_count = input('Mau berapa apel?: ')
count = int(input_count)
total_price = apple_price * count

print('Anda akan membeli ' + str(count) + ' apel')
print('Harga total adalah Rp.' + str(total_price))

if money > total_price:
    print('Anda telah membeli ' + str(count) + ' apel')
    print('Uang Anda tinggal Rp.' + str(money - total_price))

elif money == total_price:
    print('Anda telah membeli ' + str(count) + ' apel')
    print('Dompet Anda kosong')

else:
    print('Uang Anda tidak mencukupi')
    print('Anda tidak dapat membeli apel sebanyak itu')