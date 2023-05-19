from faker import Faker

class ext_lib:
    def __init__(self):
        pass

    def study_pip(self):
        print("설치 : pip install SomePackage")
        print("삭제 : pip uninstall SomePackage")
        print("특정 버전 설치 : pip install SomePackage==1.0.4")
    
    def study_faker(self):
        print("라이브러리 설치 : pip install Faker")
        print("fake = Faker()")
        print("fake.name()")
        fake = Faker()
        print(fake.name())

    def study_sympy(self):
        pass