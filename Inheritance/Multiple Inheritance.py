class Add:
    def add(self,a,b):
        return a+b;
class Sub:
    def sub(self,a,b):
        return a-b;
class Mul:
    def mul(self,a,b):
        return a*b;
class Div:
    def div(self,a,b):
        return a/b;

class Result (Add,Sub,Mul,Div):
        print("Result is : ")
R = Result()
print(R.add(5,8))
print(R.sub(10,2))
print(R.mul(8,2))
print(R.div(6,2))