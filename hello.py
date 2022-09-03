print("Привет мир!")
print("Привет программист!")
print(2+2)
print(10/3)
name="Dmitry"
print(name)
#v=input("Введиите число от 1 до 10: ")
#print(10+int(v))
#name = input('Введите ваше имя: ')
#print(f'Привет, {name}! Как дела?')
print(float('1'))  
#print(int('2.5'))  
print(bool(1))  
print(bool(''))  
print(bool(0))

#Списки
num_list=[3,5,7,9,10.5]
print(num_list)
num_list.append('Python')
print(num_list)
print(num_list[0])
print(num_list[-1])
print(num_list[2:5])
del num_list[-1]

#Словари
dic_les1={"city": "Москва", "temperature": "20"}
print(dic_les1['city'])
dic_les1["temperature"]=int(dic_les1["temperature"])-5
print(dic_les1) # "temperature" в новом словаре int
print(dic_les1.get('country'))
print(dic_les1.get('country','Россия'))
dic_les1["date"]="27.05.2019"
print(len(dic_les1))

#Функции
def fget_summ(one, two, delimiter='&'):
    return f"{one.upper()} {delimiter} {two.upper()}"
p = fget_summ("Learn", "python")
print(p)