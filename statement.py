class statement:
    def __init__(self):
        pass

    def study_if(self):
        decision = input("택시 탑승 여부 y 또는 n : ")

        if decision == "y":
            money = int(input("현재 가지고 있는 돈 : "))
            if money >= 3000:
                print("택시타고 집으로")    
            else:
                print("걸어서 집으로")
        elif decision == "n":
            print("걸어서 집으로")
        


    def study_while(self):
        while treeHit < 10:
         treeHit = treeHit +1
         print("나무를 %d번 찍었습니다." % treeHit)
         if treeHit == 10:
             print("나무 넘어갑니다.")


    def study_for(self):
        test_list = ['one', 'two', 'three'] 
        for i in test_list:
            print("기본 for 문 : " + i)

        a = [(1,2), (3,4), (5,6)]
        for (first, last) in a:
            print("리스트 내부 튜플 출력 : " + str(first) + str(last))

        marks = [90, 25, 67, 45, 80]
        number = 0 
        for mark in marks: 
            number = number +1 
            if mark < 60:
                continue 
            print(f"for + continue {number}번 학생 축하합니다. 합격입니다. " )
        
        print("for + range 구구단 ")
        for i in range(2,10):
            for j in range(1,10):
                print(i*j, end=" ")

            print('')
