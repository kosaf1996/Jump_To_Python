import datetime
import time
import math
import random
import itertools
import functools
from operator import itemgetter
import shutil
import os
import glob
import pickle
import tempfile
import traceback 
import json
import urllib.request
import webbrowser



class lib:
    def __init__(self):
        pass

    def study_date(self):
        print("day1 = datetime.date(2019, 12, 14)")
        print("day2 = datetime.date(2021, 6, 5)")
        day1 = datetime.date(2019, 12, 14)
        day2 = datetime.date(2021, 6, 5)
        print(day1, day2)

        print("두날짜의 차이 diff = day2 - day1")
        diff = day2 - day1

        print(diff.days)

    def study_time(self):
        print(f"time 출력 :{time.time()} ")
        print(f"time.localtime : {time.localtime(time.time())}")
        print(f"time.asctime : {time.asctime(time.localtime(time.time()))}")
        print(f"time.ctime : {time.ctime()}")
        print(f"time.strftime : {time.strftime('%x', time.localtime(time.time()))}")

    def study_math_gcd(self):
        print("math.gcd(60, 100, 80)")
        print(math.gcd(60, 100, 80))

    def study_math_lcm(self):
        print("math.lcm(15, 25)")
        print(math.lcm(15, 25))

    def study_random(self):
        print("random 모듈은 random.random(1,10) 일 경우 1~10사이 랜덤 값을 돌려준다.")
        print(random.random())

    def study_zip_longest(self):
        students = ['한민서', '황지민', '이영철', '이광수', '김승민']
        snacks = ['사탕', '초컬릿', '젤리']
        result = itertools.zip_longest(students, snacks, fillvalue='새우깡')

        print("students = ['한민서', '황지민', '이영철', '이광수', '김승민']")
        print("snacks = ['사탕', '초컬릿', '젤리']")
        print("result = itertools.zip_longest(students, snacks, fillvalue='새우깡')")
        print(list(result))

    def study_permutation(self):
        print("1, 2, 3 숫자가 적힌 3장의 카드에서 두 장의 카드를 꺼내 만들 수 있는 2자리 숫자를 모두 구할때")
        print("list(itertools.combinations(['1', '2', '3'], 2))")
        print(list(itertools.combinations(['1', '2', '3'], 2)))

    def study_combination(self):
        print("1~45 중 서로 다른 숫자 6개를 뽑는 로또 번호의 모든 경우의 수(조합)를 구하고 그 개수를 출력")
        print("itertools.combinations(range(1, 46), 6)")
        print(len(list(itertools.combinations(range(1, 46), 6))))

    def study_reduce(self):
        data = [1, 2, 3, 4, 5]
        result = functools.reduce(lambda x, y: x + y, data)

        print("입력 인수 data의 요소를 모두 더하여 리턴")
        print("data = [1, 2, 3, 4, 5]")
        print("result = functools.reduce(lambda x, y: x + y, data)")
        print(result)
        

    def study_itemgetter(self):
        students = [
            ("jane", 22, 'A'),
            ("dave", 32, 'B'),
            ("sally", 17, 'B'),
        ]
        result = sorted(students, key=itemgetter(1))

        print("""students = [
            ("jane", 22, 'A'),
            ("dave", 32, 'B'),
            ("sally", 17, 'B'),
        ]""")
        print("result = sorted(students, key=itemgetter(1))")
        print(result)


    def study_shutil(self):
        print("main.py 복사")
        print("""shutil.copy("study\main.py", "study\main.py.bak")""")
        shutil.copy("study\main.py", "study\main.py.bak")
        
    def study_glob(self):
        print("""glob.glob(f"{os.getcwd()}\*")""")
        print(glob.glob(f"{os.getcwd()}\*"))

    def study_pickle(self):
        print("데이터 파일 저장")
        f = open("test.txt", 'wb')
        data = {1: 'python', 2: 'you need'}
        pickle.dump(data, f)
        f.close()

        print("데이터 파일 불러오기")
        f = open("test.txt", 'rb')
        data = pickle.load(f)
        print(data)

    def study_os(self):
        print("환경 변수 확인 : os.environ")
        print(os.environ)

        print("현재 디렉터리 위치 : os.getcwd")
        print(os.getcwd)

    def study_zipfile(self):
        pass

    def study_threading(self):
        pass

    def study_tempfile(self):
        print("임시 파일의 이름을 무작위로 만들어서 리턴")
        filename = tempfile.mkstemp()
        print(filename)

    def study_traceback(self):
            try:
                lib.b()
            except:
                print("오류가 발생했습니다.")
                print(traceback.format_exc())

    def a():
        return 1/0

    def b():
        lib.a()

    def study_json(self):
        with open('myinfo.json', encoding='UTF8') as f:
            data = json.load(f)
        print(data)

    def study_urllib(self):
        print("구글 페이지 호출")
        response = urllib.request.urlopen('http://www.google.co.kr')
        print(response.status)

    def study_webbrowser(self):
        print("webbrowser.open('http://python.org')")
        webbrowser.open('http://python.org')
