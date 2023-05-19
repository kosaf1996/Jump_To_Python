class built_in:
    def __init__(self):
        pass

    def study_abs(self, value):
        print(abs(value))
        
    def study_all(self):
        print("Case1 : all([1, 2, 3])")
        print(all([1, 2, 3]))
        print("Case2 : all([1, 2, 3, 0])")
        print(all([1, 2, 3, 0]))
        print("Case3 : all([])")
        print(all([]))
        
    def study_any(self):
        print("Case1 : any([1, 2, 3])")
        print(any([1, 2, 3]))
        print("Case2 : any([1, 2, 3, 0])")
        print(any([1, 2, 3, 0]))
        print("Case3 : any([])")
        print(any([]))

    def study_chr(self):
        print("Case1 : chr(97)")
        print(chr(97))
        print("Case2 : chr(44032)")
        print(chr(44032))

    def study_dir(self):
        print("Case1 : dir([1, 2, 3])")
        print(dir([1, 2, 3]))
        print("Case2 : dir({'1':'a'})" )
        print(dir({'1':'a'}))

    def study_divmod(self):
        print("Case1 : divmod(7, 3)")
        print(divmod(7, 3))

    def study_enumerate(self):
        print("Case : ['body', 'foo', 'bar']")
        for i, name in enumerate(['body', 'foo', 'bar']):
            print(i, name)

    def study_eval(self):
        print("Case1 : eval('1+2')")
        print(eval('1+2'))
        print("Case2 : eval(hi + a)")
        print(eval("'hi' + 'a'"))
        print("Case3 : eval('divmod(4, 3)')")
        print(eval('divmod(4, 3)'))

    def study_filter(self):
        print("Case : list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))")
        print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

    def study_hex(self):
        print("Case1 : hex(234)")
        print(hex(234))
        print("Case2 : hex(3)")
        print(hex(3))

    def study_id(self):
        print("변수 생성 a =3")
        a = 3
        print("a 주소 값")
        print(id(a))
        print("3 주소 값")
        print(id(3))

    def study_input(self):
        text = input("이것이 input 함수 입니다. 아무 값 이나 입력 하세요 : ")
        print("입력 값 : " +  text)

    def study_int(self):
        number = float(input("숫자 입력 :"))
        print(int(number))

    def study_ininstance(self):
        a = built_in()
        print("isinstance(a, built_in)")
        print(isinstance(a, built_in))

    def study_len(self):
        print("len([1,2,3])")
        print(len([1,2,3]))

    def study_list(self):
        print("list(python)")
        print(list("python"))

    def study_map(self):
        print("list(map(lambda a: a*2, [1, 2, 3, 4]))")
        print(list(map(lambda a: a*2, [1, 2, 3, 4])))

    def study_max(self):
        print("max([1, 2, 3])")
        print(max([1, 2, 3]))

    def study_min(self):
        print("min([1, 2, 3])")
        print(min([1, 2, 3]))

    def study_oct(self):
        print("oct(34)")
        print(oct(34))
        print("oct(12345)")
        print(oct(12345))

    def study_open(self):
        print('''f = open("binary_file", "rb")''')

    def study_ord(self):
        print("ord('a')")
        print(ord('a'))
        print("ord('가')")
        print(ord('가'))

    def study_pow(self):
        print("pow(2, 4)")
        print(pow(2, 4))
        print("pow(3, 3)")
        print(pow(3, 3))

    def study_range(self):
        print("list(range(5))")
        print(list(range(5)))

    def study_round(self):
        print("round(4.6)")
        print(round(4.6))
        print("round(4.2)")
        print(round(4.2))

    def study_sorted(self):
        print("sorted([3, 1, 2])")
        print(sorted([3, 1, 2]))

    def study_str(self):
        num = 3
        print(f"num = 3 type = {type(num)}")
        print(f"str 타입 변환 str(num)")
        num = str(num)
        print(f"num = 3 type = {type(num)}")
        
    def study_sum(self):
        print("sum([1,2,3])")
        print(sum([1,2,3]))

    def study_tuple(self):
        print("tuple(abc)")
        print(tuple("abc"))

    def study_type(self):
        print("type(abc)")
        print(type("abc"))
        print("type([ ])")
        print(type([ ]))

    def study_zip(self):
        print("list(zip([1, 2, 3], [4, 5, 6]))")
        print(list(zip([1, 2, 3], [4, 5, 6])))
        print("""list(zip("abc", "def"))""")
        print(list(zip("abc", "def")))


