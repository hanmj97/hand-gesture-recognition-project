while True:
    a = int(input("숫자 1을 입력하세요 : "))
    b = int(input("숫자 2을 입력하세요 : "))

    giho = input("연산자를 입력하세요[+, -, *, /]: ")
    if giho in "+":
        print(a + b)
        re = input("다시 실행하시겠습니까?[Y/N] : ")
        if re in "Y":
            print("\n")
            continue
        if re in "N":
            break

    elif giho in "-":
        print(a - b)
        re = input("다시 실행하시겠습니까?[Y/N] : ")
        if re in "Y":
            print("\n")
            continue
        if re in "N":
            break

    elif giho in "*":
        print(a * b)
        re = input("다시 실행하시겠습니까?[Y/N] : ")
        if re in "Y":
            print("\n")
            continue
        if re in "N":
            break

    elif giho in "/":
        print(a / b)
        re = input("다시 실행하시겠습니까?[Y/N] : ")
        if re in "Y":
            print("\n")
            continue
        if re in "N":
            break

    else:
        print("연산자를 잘못 입력하였습니다.\n종료 되었습니다.")