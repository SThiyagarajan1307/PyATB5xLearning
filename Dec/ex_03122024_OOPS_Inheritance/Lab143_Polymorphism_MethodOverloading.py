class Father:
    def home(self):
        print("1BHK")

class thiyaga(Father):
    def home(self):
        print("3BHK")


p = thiyaga()
p.home()

f = Father()
f.home()