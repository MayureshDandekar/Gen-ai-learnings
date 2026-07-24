class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello From B")

class C(A,B):
    pass

o = C()
o.greet()
print(C.__mro__)
