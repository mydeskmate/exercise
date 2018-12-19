class A:
    def __fa(self): #在定义时就变形为_A__fa
        print('from A')
    def test(self):
        self.__fa() #只会与自己所在的类为准,即调用_A__fa

class B(A):
    def __fa(self):
        print('from B')

b = B()
print(b.__dict__)
print(b.test())
