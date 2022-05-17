import datetime as dt


s = '178.154.200.14 - - [01/Apr/2020:06:53:24 +0900] "GET /*/****/*******/****/****/ HTTP/1.1" 200 7819'

#f = s.split(maxsplit=4)[:4]
#print(f)
#t = dt.time(12,00)
#s = s.split(maxsplit=4)[-2].split(':')
#s = dt.time(int(s[1]), int(s[2]))
#print(s > t)

t = dt.time(12,00)
with open('red_apple_2.log') as f:
    all_ip = (line.split(maxsplit=4)[:4] for line in f )
    less_12pm = (l[0] for l in all_ip  if dt.time(int(l[-1].split(":")[1]), int(l[-1].split(":")[2])) < t)
    amount_u_am = (1 for i in set(less_12pm))
    amount_u_am = sum(amount_u_am)
    print(f'Unique ip from 00 to 12: {amount_u_am}')

with open('red_apple_2.log') as f:
    all_ip = (line.split(maxsplit=4)[:4] for line in f )
    less_12pm = (l[0] for l in all_ip  if dt.time(int(l[-1].split(":")[1]), int(l[-1].split(":")[2])) > t)
    amount_u_mp = (1 for i in set(less_12pm))
    amount_u_mp = sum(amount_u_mp)
    print(f'Unique ip from 12 to 00: {amount_u_mp}')

if amount_u_am > amount_u_mp:
    print(f'Людей больше заходит на сайт до 12 раздницa: {amount_u_am - amount_u_mp}')
else:
    print(f'Людей больше заходит на сайт после 12 раздница: {amount_u_mp - amount_u_am}')
