## 함수 선언 부분 ##

year = 0    #윤년을 계산할 연도를 입력받는다.

## 메인 코드 부분 ##

if __name__ == "__main__" :    # 메인 코드를 실행한다.
    year = int(input("윤년을 계산할 연도를 입력해주세요. :"))    #연도를 입력받는다.

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) :
        #4로 나누어 떨어지고, 100으로 나누어 떨어지지 않으며, 400으로 나누어 떨어질 때
        print("입력하신 연도는 윤년입니다.")    #윤년임을 출력

    else :    #4로 나누어 떨어지지 않고, 100으로 나누어 떨어지며, 400으로 나누어 떨어지지 않을 때
        print("입력하신 연도는 윤년이 아닙니다.")    #윤년이 아님을 출력
        
