class demo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f"hello {self.name} ,age is {self.age}")


demo1 = demo("ali", "18")
demo1.hello()
