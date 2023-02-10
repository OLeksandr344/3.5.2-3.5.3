import math

txxt='Героям Слава'               #1
print(txxt)

print('---------------------------------------------------------------------------------------------------------')

user_name='Олександр'             #2
print("Привіт,",user_name)

print('---------------------------------------------------------------------------------------------------------')

famous_person='Albert Einstein'   #3
message=" once said, a person who never made a mistake never tried anything new."
print(famous_person + message)

print('---------------------------------------------------------------------------------------------------------')

name="  \t Arnold \n   "           #4
print(name)
x=name.lstrip()
print(x)
y=name.rstrip()
print(y)
z=name.strip()
print(z)

print('---------------------------------------------------------------------------------------------------------')

print("Олександр Кукул \n Україна \n 48000 \n Чернівці \n проспект Незалежності \n 114А ")   #5

print('---------------------------------------------------------------------------------------------------------')

# конвертація n метрів в інші величини       #6 і #11 input
meters = float(input("any number "))
print(meters)
feet_to1m = 3.28
inches_to1m = 39.37 
miles_to1m = 0.00062137
feets = meters * feet_to1m
inches = meters * inches_to1m
miles = meters * miles_to1m
print(feets)
print(inches)
print(miles)
                    
print('---------------------------------------------------------------------------------------------------------')

# В учнів були канікули n днів, вони відпочивали -         #7 і #11 input
your_days = int(input("enter any number "))
print(your_days)

seconds=your_days*24*60*60
print(seconds)
min=your_days*24*60
print(min)
hours=your_days*24
print(hours)

secondsfor = format(seconds, "10")
print(secondsfor)
minsfor = format(min, "10")
print(minsfor)
hoursfor = format(hours, "10")
print(hoursfor)

print('---------------------------------------------------------------------------------------------------------')

#температура на вулиці n градусів Цельсія                      #8 і #11 input
your_degrees = int(input("enter any number "))
c = your_degrees
f = your_degrees * 32 + 9/5
k = c + 273.15
formatc = format(c,"14,.2f")
print(formatc)
formatf = format(f,"14,.2f")
print(formatf)
formatk = format(k,"14,.2f")
print(formatk)

print('---------------------------------------------------------------------------------------------------------')

#розкладання довільного цілого числа і виведення на екран суму цифр у числі   #9 і #11 input
digit = input("any an arbitrary integer")
sum_digits = [int(x) for x in digit if x.isnumeric()]
print(sum_digits)
total = sum(sum_digits)
print(total)


print('---------------------------------------------------------------------------------------------------------')
                                             #10 

x1=39.9075000
x2=116.3972300
y1=50.4546600
y2=30.5238000
x11= math.radians(x1)
x22= math.radians(x2)
y11= math.radians(y1)
y22= math.radians(y2)
                                              

distancee=6371.032*math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11 - y22))
print(distancee) #km

print('---------------------------------------------------------------------------------------------------------')

                                       #10 і #11 input
xr1=int(input("x1 coordinate"))
yr1=int(input("y1 coordinate"))
xr2=int(input("x2 coordinate"))
yr2=int(input("y2 coordinate"))

xra11= math.radians(xr1)
yra11= math.radians(yr1)
xra22= math.radians(xr2)
yra22= math.radians(yr2)

distancee=6371.032*math.acos(math.sin(xra11) * math.sin(xra22) + math.cos(xra11) * math.cos(xra22) * math.cos(yra11 - yra22))
print(distancee) #km

print('---------------------------------------------------------------------------------------------------------')
