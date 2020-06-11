class out:
    def __init__(self):
        print("Self initiated")

    class innr:
        def __init__(self):
            print("Inner initiated")
        def m1(self):
            print("inner class method")

o = out()
iobj = out.innr()
iobj.m1()
