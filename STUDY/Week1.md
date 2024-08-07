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
          
      ▶ Google Colab 💡
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

       # 사용자에게 입력받을 때는  `input()`  사용!

       # Python Tutor 💡
           : 파이썬의 동작과정을 보는 프로그램 

       # Python의 삼항연산자
            - 삼항연산자 - 아주 간단한 if-else문을 한줄로 작성할 수 있는 문법
            - 결과 = '참일때의 값' if '조건식' else '거짓일 때 값'
            - 결과 출력
             
         java의 삼항연산자
              조건식 ? 참일 때 값 : 거짓일 때 값      

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


       # Python의 비트연산자 : 다른 언어와 다른게 동작!
       
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
       # Python의 반복문
           ① while : 반복 조건
                False인 경우가 나올 때까지 실행(False면 종료)
           ② for : 반복 범위 
                범위는 range() 주로 사용
       
       # break, continue
           break : 반복의 횟수를 줄임 (탈출)
           continue : 반복의 횟수를 줄이지 않고 남은 부분을 생략하는 것 
           
       # 이중 for문
```python
for i in [1,2]:
    for j in ['a','b','c']:
        print(j * i, end ='')
=> a b c aa bb cc
```

---

### 🌥 0711(THU)

        💡 """ """ or ''' ''' - 멀티라인으로 감싸주면 원본 스트링을 그대로 저장함
        
        # 문자열의 메소드
            -> 문자열 : 튜플형태, 문자들이 여러개로 줄 서 있는 것!

        >> 자주 사용하는 문자열 메소드
            split()
            replace()
            strip()
            join()
            format()

        # Collections ❗
        # 정규표현식 ❗

        # 출력 문자열 꾸미기
            f-string
            format
            %

        # 함수(function)
            ① 파괴적 함수 : 원본을 바꾸지않는다.
                ex) str, int, Float
            ② 비파괴적 함수 : 원본을 바꾼다.
                ex) list 관련된 함수들
                
        ❔  070-8919-1203(랜덤으로 시를 읽어주는 번호)
            음성 tts 기능? 
            NLP
            글에서 원하는 텍스트 추출
            wordCloud? 
---

### ☁ 0712(FRI)

        시퀀스 타입
            list - mutable 객체(안에 있는 값을 변경시킬 수 있는 객체)
            list : 값 추가, 삭제 가능 []
            tuple - immutable 객체(안에 있는 값을 수정할 수 없음, 문자열)
            tuple : 값 추가, 삭제 불가 () -> 참조만을 위한 값을 다룰 때 주로 사용
            range(범위)
```python
list(range(1,5))
=> 해당 범위를 lsit형태로 반환 [1,2,3,4]

list("Hello")
=> 문자를 다 쪼개서 list로 반환 ['H', 'e', 'l', 'l', 'o']

range(1,10,2) # 1부터 10 이전까지 2씩 증가하는 range
# range 범위 거꾸로 지정하기
range(10,2,-1) # 10부터 1씩 감소하여 3까지 이르는 정수들
```            
            
        딕셔너리
        
        스트링 함수, 포맷형식
        
        함수
            print( ~~ , end = '') # 개행 대신 end=''를 출력
            print( ~~ , sep = ', ') # sep으로 전달된 문자를 ~~ 사이사이에 출력(출력된 결과물을 구분하는 용도)
```python
print(1,2,3, sep = '_', end = ' m^^m')
=> 1_2_3 m^^m
```
        함수의 매개변수 참조 관계 ☆
            => 함수 안에서 값을 변경하면 실제 원본에도 영향을 미친다! (이름표 가져다 붙이기 기억)
        
        
        지역변수 global 키워드
        파이썬 수학 관련 함수(min,max,sum,sorted..)
        데이터 분야 관련된 재귀함수
        익명함수(람다식)
        파이썬 클래스
        리스트 컴프리헨션(List Comprension)
        reduce...?

      
