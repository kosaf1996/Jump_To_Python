class data_type:
    def __init__(self):
        self.number1 = 7
        self.number2 = 4
        self.string =" String "
        self.list =  ['Life', 'is', 'too', 'short']
        self.tuple = (1, 2, 'a', 'b')
        self.dic = {"김연아":"피겨스케이팅", "류현진":"야구", "손흥민":"축구", "귀도":"파이썬"}

    def study_String(self):
        print("출력 : " + self.string)
        print("문자열 길이 : " + str(len(self.string)))
        print("3번째 문자열 인덱싱 : " + self.string[2])
        print("문자열 슬라이싱 : " + self.string[0:3] )
        print(f"문자열 {self.string} 포맷팅")
        print("문자열 위치 알려주기 : " + str(self.string.index('r')))
        print("문자열 삽입 : " + ",".join(self.string))
        print("대문자 변경 : " + self.string.upper())
        print("소문자 변경 : " + self.string.lower())
        print("왼쪽 공백 지우기 : " + self.string.lstrip())
        print("오른쪽 공백 지우기 : " + self.string.rstrip())
        print("양쪽 공백 지우기 : " + self.string.strip())
        print("문자열 바꾸기 : " + self.string.replace("String", "Replace"))

    def study_list(self):
        for i in range (len(self.list)):
            print(f"출력{i} : " + self.list[i])    

        print("첫 번째 요소 : " + self.list[0])
        print("리스트 슬라이싱 : " + str(self.list[:2]))
        print("리스트 길이 : " + str(len(self.list)))
        print("리스트 반복 : " + str(self.list * 2) )
        del self.list[1]
        print("리스트 요소 삭제 : " + str( self.list))
        self.list.append('test')
        print("리스트 요소 추가 : " + str(self.list))
        print("리스트 인덱스 반환 : " + str(self.list.index('test')))

    def study_number(self):
        print(f"출력 : number1 {self.number1}, number2 {self.number2} ")
        print("제곱 연산자 : " + str((self.number1 ** self.number2)) )
        print("나머지 연산 : " + str((self.number1 / self.number2)) )

    def study_tuple(self):
        print("출력 : " + str(self.tuple))
        print("Tuple 인덱싱 : " + str(self.tuple[3]))
        print("Tuple 슬라이싱 : " + str(self.tuple[1:]))
        print("Tuple 더하기 : " + str(self.tuple + self.tuple))
        print("Tuple 곱하기 : " + str(self.tuple *2))
        print("Tuple 길이 : " + str(len(self.tuple)))

    def study_dic(self):
        print("김연아 키로 value 얻기 : " + str(self.dic['김연아']))
        print("키 리스트 : " + str(self.dic.keys()))
        print("value 리스트 : " + str(self.dic.values()))
        print("키로 값 얻기 : " + self.dic.get('김연아'))
        print("키 검색 : " + str('김연아' in self.dic))