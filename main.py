try:
    print('Hello Mars')
    f = open("mission_computer_main.log", "r")
    print(f.read())
except Exception as e:
    print("예상치못한 오류 발생");
except FileNotFoundError as e:
    print("파일을 찾을 수 없음 ");
except IOError as e: 
    print("입출력 오류 발생");



