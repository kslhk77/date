import datetime

def date():
    y = int(input("년도를 입력하세요 : "))
    m = int(input("월을 입력하세요 : "))
    d = int(input("일을 입력하세요 : "))

    return y,m,d

def cal(num):
    if(num%4) == 0:
        if(num%400) == 0:
            return True
        
        elif(num%100) == 0:
            return False

        else:
            return True

    else:
        return False

def ymd(year, month, day):
    dt = datetime.datetime(year,month,day)
    dt = int(dt.strftime("%j"))
    count = 0
    for i in range(year):
        if cal(i):
            count += 366

        else:
            count += 365

    day = (count + dt - 366) % 7

    return {0:'일요일', 1:'월요일', 2:'화요일', 3:'수요일', 4:'목요일', 5:'금요일', 6:'토요일'}[day]

if __name__ == "__main__":
    year,month,day = date()
    day_name = ymd(year,month,day)

    print(year,'년',month,'월',day,'일은',day_name,'입니다.')