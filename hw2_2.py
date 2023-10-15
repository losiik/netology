boys = ["Peter", "Alex", "John", "Arthur", "Richard"]
girls = ["Kate", "Liza", "Kira", "Emma", "Trisha"]

if len(boys) != len(girls):
    print('Результат: Внимание, кто-то может остаться без пары.')
    exit()


for i, boy in enumerate(boys):
    print(f'{boy} и {girls[i]}')
