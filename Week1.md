### 🌨 0708(MON)
    🛠 Tools 
      Google Colab , sublime.text, Github/Git
      Python, Slack, VSCode

    📖 Study
      ▶ Python 설치 및 개발환경구축
      ▶ Git 설치 및 Github readme.md 꾸미기
          → 추가 수정 필요
          → 마크다운(Markdown) 학습 ( 마크다운 문법을 사용할 땐 파일명 .md 로! )
      ▶ VSCode 설치
          ⓐ Python 확장 팩 설치
          ⓑ Korean Language Pack 설치
          ⓒ Live Server 설치
          ⓓ Live Preview 설치 
      ▶ Google Colab 사용
          → 처음 접해보는 프로그램
            사용법 공부 必
---

### 🌦 0709(TUE)

    🛠 Tools 
        Google Colab으로 교육

    📖 Study
      # 이름을 작성하기 위한 규칙 - 네이밍 컨벤션(convention)
      
      my_documents # snake_case (Python에서 주로 사용)
      
      # 클래스와 일반변수와 구분하기 위해서 변수 첫 글자는 소문자로 시작함
      # 클래스는 첫 글자 대문자로 시작
      MyClass # PascalCase

      # 메모리 주소 확인
        → id(docs) 
    
      # swap : 변수의 값을 교환하기
 ```python
a , b = b , a 
print(a, b)

a, b, *c = 10, 20, 30, 40, 50
a =10 , b = 20, *c에 나머지 값 할당됨
```

      # 변수명 규칙
```python
str = '사과나무' # str이라는 예약어에 값 할당 -> str.find() 사용 시 에러
del str # del명령어로 str 변수 삭제
```
      # 컨테이너 자료형
          ① 순서로 값을 관리하는 시퀀스(Sequence)형
          ② 키-값으로 자료를 관리하는 매핑(Mapping)형
          ③ 키만으로 자료를 관리하는 집합(Set)형


---

### 🌤 0710(WED)

      # 조건문
          ① if문 
          ② match - case문
          
```python
match 변수 or 값:
    case 값:
       실행문
ex)
ask = input('어깨를 돌리셨습니까 ? ')
match ask : # ask에 뭐가 있는지 보자
    case 'Y': # True일 때
        print('Good')
    case _: # False 일 때 나머지 모든 상황 표현
        print('no')
```

       # 사용자에게 입력받을 때는  `input()`  사용!

       # Python Tutor 💡
           : 파이썬의 동작과정을 보는 프로그램 

       # Python의 삼항연산자
            # 삼항연산자 - 아주 간단한 if-else문을 한줄로 작성할 수 있는 문법
            # 결과 = '참일때의 값' if '조건식' else '거짓일 때 값'
            # 결과 출력

```python
ex) 입력한 숫자는 홀수일까? 짝수일까?
while True:
    num = int(input("숫자입력(0은 종료) : "))
    if num == 0:
        break
    print("짝수" if num % 2 == 0 else "홀수")
    print("홀수" if num % 2 != 0 else "짝수")
    print("홀수" if num % 2 else "짝수")
```
            # java의 삼항연산자
                조건식 ? 참일 때 값 : 거짓일 때 값

       # Python의 비트연산자
       # Flag 변수 : True / False로 무언가를 판단할 때 주로 사용

       # Python의 조건문
           ① if문(if문 , if-else문 , if-elif-else문)
           ② match - case문
       
```python
match 변수 or 값:
    case 값:
       실행문
ex)
ask = input('어깨를 돌리셨습니까 ? ')
match ask : # ask에 뭐가 있는지 보자
    case 'Y': # True일 때
        print('Good')
    case _: # False 일 때 나머지 모든 상황 표현
        print('no')
```

---

### 🌥 0711(THU)

      

      
