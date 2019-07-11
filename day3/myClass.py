
class Student: # 상속받는게 아니라면, ()는 불요
    def __init__(self, num, name, kor, eng, mat):
        self.num=num
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat
        
    def sum(self):
        return self.kor+self.eng+self.mat
        
    def avg(self):
        return self.sum()/3
    
    def __str__(self):
        #return "번호: "+str(self.num)+" 이름: "+self.name+" 국어: "+str(self.kor)+" 영어: "+str(self.eng)+" 수학: "+str(self.mat)\
        return "학번:%d \t이름:%s \t총점:%4d \t평균:%.2f"%(self.num, self.name, self.sum(), self.avg())
    
# Encapsulation
class Car():
    def __init__(self, num, price, model): #변수의 값 설정
        self.num = num
        self.price = price
        self.model = model
        
    def setNum(self, num): # num값을 수정할 때 사용
        if len(num)==7:
            self.__num=num
        else:
            print("차량변호 형식 오류")
        
    def getNum(self): # num값을 검색할 때 사용
        return self.num
        
    def drive(self, speed):
        print(speed, " 속도로 달립니다")
        
    def getPrice(self):
        return self.price
    
    def __str__(self): # 이 클래스의 정보 문자열을 리턴
        return "Car: 차량변호"+self.num+" 가격:"+str(self.price)+" 모델:"+self.model
        #print("Car: 차량번호{}, 가격:{}, 모델:{}".format(self.num, self.price, self.model))        

#inheritage
class Bus(Car):
    def __init__(self, num, price, model, seat):
        #super().__init__(num, price, model)
        Car.__init__(self, num, price, model)
        self.seat=seat
        
    def drive(self, speed):
        print("버스가 ",speed*0.9," 속도로 달립니다")
        
    def autoDoor(self, flag):
        if flag:
            print("open the door")
        else:
            print("close the door")
            
    def __str__(self):
        return super().__str__()+" 좌석:"+str(self.seat)
