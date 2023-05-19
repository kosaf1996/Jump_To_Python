import data_type as dt
import statement as st
import class_test as ct
import built_in as bt 
import lib   
import ext_lib as el


if __name__ == '__main__':
    
    data_type = dt.data_type()
    statment = st.statement()
    built = bt.built_in()
    lib_class = lib.lib()
    ext_lib = el.ext_lib()

    while True:
     print("1. 데이터 타입")
     print("2. 자료형")
     print("3. 클래스, 모듈, 패키지")
     print()
     number = input("번호 선택 :")

     if number == '1':
          print("확인 하고 싶은 데이터 타입")
          print("1. 문자열")
          print("2. 슷자형")
          print("3. 리스트")
          print("4. 딕셔너리")
          print("5. 튜플")
          
          number2 = input("번호 선택 : ")

          if number2 == '1':
               data_type.study_String()
          elif number2 == '2':
               data_type.study_number()
          elif number2 == '3':
               data_type.study_list()
          elif number2 == '4':
               data_type.study_dic()
          elif number2 == '5':
               data_type.study_tuple()


     elif number == '2':
          print("확인 하고 싶은 데이터 타입")
          print("1. if")
          print("2. while")
          print("3. for")
          number3 = input("번호 선택 : ")

          if number3 == '1':
              statment.study_if()
          elif number3 == '2':
              statment.study_while()
          if number3 == '3':
              statment.study_for()

     elif number == '3':
         print("확인 하고 싶은 데이터 타입")
         print("1. 클래스")
         print("2. 예외 처리")
         print("3. 내장 함수")
         print("4. 표준 라이브러리")
         print("5. 외부 라이브러리")

         number4 = input("번호 선택 : ")
         
         if number4 == '1':
               num1 = input("첫 번쨰 값 입력 : ")
               num2 = input("두 번쨰 값 입력 : ")
               class_test = ct.Calculator(num1,num2)

               print("더하기 호출 : " + str(class_test.add()))
               print("뺴기 호출 : " + str(class_test.sub()))
               print("곱하기 호출 : " + str(class_test.mul()))
               print("나누기 호출 : " + str(class_test.div()))
         elif number4 == '2':
               print("== Program Start")
               a = int(input("첫 번쨰 값 입력 : "))
               b = int(input("두 번쨰 값 입력 : "))
               class_test = ct.Calculator(a, b)
               try:
                    print("try : 예외가 발생할 수 있는 코드")
                    class_test.try_div()
                    print("========================================")
               except ZeroDivisionError as e:
                    print("try : 예외가 발생했을때 실행할 코드")
                    print('0으로 나누지 마세요. {0} 에러가 발생 합니다.'.format(e))
                    print("========================================")
               else :
                    print("else : 예외가 발생하지 않았을 때 실행할 코드")
                    print('나눗셈을 정상적으로 실행 되었습니다.')
                    print("========================================")
               finally:
                    print("finally : 예외 발생 여부와 상관없이 무조건 실행할 코드")
                    print('프로그램을 종료 합니다.')
         elif number4 == '3':
              print("1. abs")
              print("2. all")
              print("3. any")
              print("4. chr")
              print("5. dir")
              print("6. divmod")
              print("7. enumerate")
              print("8. eval")
              print("9. filter")
              print("10. hex")
              print("11. id")
              print("12. input")
              print("13. int")
              print("14. ininstance")
              print("15. len")
              print("16. list")
              print("17. map")
              print("18. max")
              print("19. min")
              print("20. oct")
              print("21. open")
              print("22. ord")
              print("23. pow")
              print("24. range")
              print("25. round")
              print("26. sorted")
              print("27. str")
              print("28. sum")
              print("29. tuple")
              print("30. type")
              print("31. zip")

              built_num = input("내장 함수 선택 : ")
               
              if built_num == '1':
                  print("abs는 숫자의 절댓값을 리턴 하는 함수 입니다.")
                  value = float(input("Value 입력 : "))
                  built.study_abs(value)

              elif built_num == '2':
                   print("반복 데이터의 모든 요소가 모두참이면 True, False가 하나라도 있으면 Flase로 값을 리턴")
                   built.study_all()

              elif built_num == '3':
                   print("반복 데이터의 모든 요소중 하나라도 참이면 True, 모두 거짓이면 Flase로 값을 리턴  (all의 반대)")
                   built.study_any()

              elif built_num == '4':
                   print("유니코드 숫자값을 입력받아 그 코드에 해당하는 문자 리턴")
                   built.study_chr()

              elif built_num == '5':
                   print("객체가 지난 변수나 함수를 보여주는 함수")
                   built.study_dir()

              elif built_num == '6':
                   print("두 개의 숫자를 나눈 몫과 나머지를 튜플로 리턴")
                   built.study_divmod()
               
              elif built_num == '7':
                   print("순서가 있는 데이터를 받아(리스트, 튜플 등) 인덱스 값을 포함하는 enumerate 객체 리턴")
                   built.study_enumerate()

              elif built_num == '8':
                   print("문자열로 포함된 표현식을 받아 실행한 결과값 리턴")
                   built.study_eval()

              elif built_num == '9':
                   print("데이터를 걸러낸 값을 리턴")
                   built.study_filter()

              elif built_num == '10':
                   print("정수 값을 hex 값으로 리턴")
                   built.study_hex()

              elif built_num == '11':
                   print("객체를 입력받아 객체의 주소 값을 리턴")
                   built.study_id()

              elif built_num == '12':
                   print("사용자에게 입력 받는 함수")
                   built.study_input()

              elif built_num == '13':
                   print("숫자를 정수형으로 변환")
                   built.study_int()

              elif built_num == '14':
                   print("첫번쨰 인수로 객체, 두번쨰 인수로 클래스를 받아 True, False 반환")
                   built.study_ininstance()

              elif built_num == '15':
                   print("길이(요소의 전체 개수)를 리턴")
                   built.study_len()

              elif built_num == '16':
                   print("반복 가능한 데이터(iterable)를 입력받아 리스트로 만들어 리턴")
                   built.study_list()

              elif built_num == '17':
                   print("map 함수는 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴")
                   built.study_map()

              elif built_num == '18':
                   print("최댓값을 리턴")
                   built.study_max()

              elif built_num == '19':
                   print("최솟값을 리턴")
                   built.study_min()

              elif built_num == '20':
                   print("정수를 8진수 문자열로 바꾸어 리턴")
                   built.study_oct()

              elif built_num == '21':
                   print("파일 이름과 읽기 방법을 입력받아 파일 객체를 리턴")
                   built.study_open()

              elif built_num == '22':
                   print("문자의 유니코드 숫자 값을 리턴")
                   built.study_ord()

              elif built_num == '23':
                   print(" x의 y 제곱한 결괏값을 리턴")
                   built.study_pow()

              elif built_num == '24':
                   print(" 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴")
                   built.study_range()

              elif built_num == '25':
                   print("숫자를 입력받아 반올림해 리턴")
                   built.study_round()

              elif built_num == '26':
                   print("입력 데이터를 정렬한 후 그 결과를 리스트로 리턴")
                   built.study_sorted()

              elif built_num == '27':
                   print("자열 형태로 객체를 변환하여 리턴")
                   built.study_str()

              elif built_num == '28':
                   print("입력 데이터의 합을 리턴")
                   built.study_sum()

              elif built_num == '29':
                   print("반복 가능한 데이터를 튜플로 바꾸어 리턴")
                   built.study_tuple()

              elif built_num == '30':
                   print("입력값의 자료형 리턴")
                   built.study_type()

              elif built_num == '31':
                   print("일한 개수로 이루어진 데이터들을 묶어서 리턴")
                   built.study_zip()

         elif number4 == '4':
              print("1. datetime.date")
              print("2. time")
              print("3. math.gcd")
              print("4. math.lcm")
              print("5. random")
              print("6. itertools.zip_longest")
              print("7. itertools.permutation")
              print("8. itertools.combination")
              print("9. functools.reduce")
              print("10. operator.itemgetter")
              print("11. shutil")
              print("12. glob")
              print("13. pickle")
              print("14. os")
              print("15. zipfile")
              print("16. threading")
              print("17. tempfile")
              print("18. traceback")
              print('19. json')
              print("20. urllib")
              print("21. webbrowser")

              lib_num = input("표준 라이브러리 선택 : ")

              if lib_num == '1':
                   print("datetime.date는 년, 월, 일로 날짜를 표현할 때 사용하는 함수")
                   lib_class.study_date()

              elif lib_num == '2':
                   print("UTC(Universal Time Coordinated 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 리턴하는 함수")
                   lib_class.study_time()
              
              elif lib_num == '3':
                   print("최대공약수(gcd, greatest common divisor)를 구하는 함수")
                   lib_class.study_math_gcd()
             
              elif lib_num == '4':
                   print("최소공배수(lcm, least common multiple)를 구할때 사용하는 함수")
                   lib_class.study_math_lcm()

              elif lib_num == '5':
                   print("난수(규칙이 없는 임의의 수)를 발생시키는 모듈")
                   lib_class.study_random()

              elif lib_num == '6':
                   print("같은 개수의 자료형을 묶는 파이썬 내장 함수인 zip()과 똑같이 동작")
                   lib_class.study_zip_longest()
              
              elif lib_num == '7':
                   print("반복 가능 객체(iterable) 중에서 r개를 선택한 순열을 이터레이터로 리턴하는 함수")
                   lib_class.study_permutation()
              
              elif lib_num == '8':
                   print("반복 가능 객체(iterable) 중에서 r개를 선택한 조합을 이터레이터로 리턴하는 함수")
                   lib_class.study_combination()
          
              elif lib_num == '9':
                   print(" function을 반복 가능한 객체(iterable)의 요소에 차례대로(왼쪽에서 오른쪽으로) 누적 적용하여 이 객체를 하나의 값으로 줄이는 함수")
                   lib_class.study_reduce()
          
              elif lib_num == '10':
                   print("sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬할 수 있도록 도와주는 모듈")
                   lib_class.study_itemgetter()
          
              elif lib_num == '11':
                   print("파일을 복사(copy)하거나 이동(move)할 때 사용하는 모듈")
                   lib_class.study_shutil()

              elif lib_num == '12':
                   print(" 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다. 이럴 때 사용하는 모듈")
                   lib_class.study_glob()

              elif lib_num == '13':
                   print("객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈")
                   lib_class.study_pickle()
          
              elif lib_num == '14':
                   print(" 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈")
                   lib_class.study_os()

              elif lib_num == '15':
                   print("여러 개의 파일을 zip 형식으로 합치거나 이를 해제할 때 사용하는 모듈")
                   lib_class.study_zipfile()

              elif lib_num == '16':
                   print("스레드 객체를 통한 병렬 처리")
                   lib_class.study_threading()
             
              elif lib_num == '17':
                   print("파일을 임시로 만들어서 사용할 때 유용한 모듈")
                   lib_class.study_tempfile()
            
              elif lib_num == '18':
                   print("프로그램 실행 중 발생한 오류를 추적하고자 할 때 사용하는 모듈")
                   lib_class.study_traceback()

              elif lib_num == '19':
                   print("JSON 데이터를 쉽게 처리하고자 사용하는 모듈")
                   lib_class.study_json()

              elif lib_num == '20':
                   print("URL을 읽고 분석할 때 사용하는 모듈")
                   lib_class.study_urllib()

              elif lib_num == '21':
                   print(" 시스템 브라우저를 호출할 때 사용하는 모듈")
                   lib_class.study_webbrowser()

         elif number4 == '5':
              print("1. pip")
              print("2. faker")
              print("3. sympy")


              ext_num = input("외부 라이브러리 선택 : ")

              if ext_num == '1':
                   print("파이썬 모듈이나 패키지를 쉽게 설치")
                   ext_lib.study_pip()
               
              elif ext_num == '2':
                   print("faker는 테스트용 가짜 데이터를 생성할 때 사용하는 라이브러리")
                   ext_lib.study_faker()

              elif ext_num == '3':
                   ext_lib.study_sympy()


     print()
