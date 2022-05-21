import datetime as dt
import time

def function(func):
    def wrapper(*args, **kwgs):
        start = time.perf_counter()
        func()
        finish = time.perf_counter()
        return finish - start
    return wrapper


@function
def main():
    with open('red_apple_2.log') as f:
        formline = (line.strip().rsplit(maxsplit=2)[2] for line in f)
        all_bytes = (int(i) for i in formline if i.isdigit())
        all_byt = sum(all_bytes)
        print(f'Total all: {all_byt}b')
    
    with open('red_apple_2.log') as f:
        formline1 = (line.strip().rsplit(maxsplit=2)[1:] for line in f)
        bytes_200 = (int(i[1]) for i in formline1 if i[1].isdigit() and i[0].strip() == '200')
        byt_200 = sum(bytes_200)
        print(f'Total 200: {byt_200}b')

    print(f'Difference: {all_byt - byt_200}b')


    # 2 Task

    with open('red_apple_2.log') as f:
        fileline = (line.strip().rsplit(maxsplit=2)[1:] for line in f)
        bytes_404 = (int(i[1]) for i in fileline if i[1].isdigit() and i[0].strip() == '404')
        print(f'Total 404: {sum(bytes_404)}b')

    # 3 Task

    with open('red_apple_2.log') as f:
        fileline = (1 for line in f)
        print(f'Total requests: {sum(fileline)}')

    # 4 Task

    with open('red_apple_2.log') as f:
        fileline = (line.rsplit(maxsplit=2)[1:] for line in f)
        total_line = (1 for i in fileline if i[0].strip() == '200')
        print(f'Total requests 200: {sum(total_line)}')

    with open('red_apple_2.log') as f:
        fileline = (line.rsplit(maxsplit=2)[1:] for line in f if line.rsplit(maxsplit=2)[1:][0] == '200')
        *_, pl, l = fileline
        print(f'Pre-last line 200: {pl[1]}b')

    # 5 Task

    with open('red_apple_2.log') as f:
        fileline = (line.rsplit(maxsplit=2)[1:] for line in f)
        total_line = (1 for i in fileline if i[0].strip() == '404')
        print(f'Total requests 404: {sum(total_line)}')


    with open('red_apple_2.log') as f:
        fileline = (line.rsplit(maxsplit=2)[1:] for line in f if line.rsplit(maxsplit=2)[1] == '404')
        *_, pl, l = fileline
        print(f'Pre-last line 404: {pl[1]}b')

    # 6 Task

    with open('red_apple_2.log') as f:
        fileline = (line.rsplit(maxsplit=2)[1:] for line in f)
        total_line = (int(i[1]) for i in fileline if i[0].strip() == '404' and i[1].isdigit())
        total_byt_404 = sum(total_line)


    with open('red_apple_2.log') as f:
        fileline = (1 for line in f if line.rsplit(maxsplit=2)[1] == '404' and line.rsplit(maxsplit=2)[2].isdigit())
        total_requs_404 = sum(fileline)

    print(f'Middle bytes 404: {(total_byt_404 / total_requs_404):.2f}')

    with open('red_apple_2.log') as f:
        fileline = (line.rsplit(maxsplit=2)[1:] for line in f)
        total_line = (int(i[1]) for i in fileline if i[0].strip() == '200' and i[1].isdigit())
        total_byt_404 = sum(total_line)


    with open('red_apple_2.log') as f:
        fileline = (1 for line in f if line.rsplit(maxsplit=2)[1] == '200' and line.rsplit(maxsplit=2)[2].isdigit())
        total_requs_404 = sum(fileline)

    print(f'Middle bytes 200: {(total_byt_404 / total_requs_404):.2f}')

    # 7 Task

    with open('red_apple_2.log') as f:
        all_ip = (line.split(maxsplit=1)[0] for line in f)
        unique_ip = sorted(set(all_ip), key=lambda x: int(x.split('.',maxsplit=1)[0]))
        print(unique_ip)
        
    # 8 Task

    with open('red_apple_2.log') as f:
        all_ip = (line.split(maxsplit=1)[0] for line in f)
        unique_ip = sorted(set(all_ip), key=lambda x: int(x.split('.',maxsplit=1)[0]))
        amount_u_ip = (1 for i in unique_ip)
        print(f'Total unique ip: {sum(amount_u_ip)}')
        
    # 9 Task

    t = dt.time(12,00)
    with open('red_apple_2.log') as f:
        all_ip = (line.split(maxsplit=4)[:4] for line in f )
        less_12pm = (l[0] for l in all_ip  if dt.time(int(l[-1].split(":")[1]), int(l[-1].split(":")[2])) < t)
        unique_ip = sorted(set(less_12pm), key=lambda x: int(x.split('.',maxsplit=1)[0]))
        print(f'Unique ip from 00 to 12: {unique_ip}')

    # 10 Task

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


print(main())

