class a:
    def sshow(self):
        
        print("class a")

class b(a):
    def show(self):
        super().show()
        print("class b")
        
bobj = b()
bobj.a().show()

