def add_all(*args):
    total=0
    for num in args:
        total+=num
        return total
    print(add_all(1,2,3))
    print(add_all(15,20,30,40))

def show_args(*args):
    print(type(args))
    print(args)

    def show_args(*args):
        print(type(args))
        print(args)
show_args(5,"Hello",True)

def show_info(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
show_info(name="Sumaia",age=21,city="Dhaka")

def checker_kwargs(**kwargs):
              print(type(kwargs))
              print(kwargs)
checker_kwargs(language="Python",Lvel="Beginner")


