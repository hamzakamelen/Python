class DawoodUni:
    def AIDept(self):
        self.AIDept = True
    def ABCDept(self):
        self.ABCDept = False

class SirSyedUni:
    def AIDept(self):
        self.AIDept = False
    def ABCDept(self):
        self.ABCDept = True

D = DawoodUni()
S = SirSyedUni()

print(S.AIDept()) #---False
print(D.AIDept()) #---True

# -----------------------------------------------------
class Muzzamil:
    def Cricket(self):
        self.Player = False
        self.Viewer = False
        print(self.Player,self.Viewer)
class Wajahat:
    def Cricket(self):
        self.Player = False
        self.Viewer = True
        print(self.Player,self.Viewer)
class Moiz:
    def Cricket(self):
        self.Player = True
        self.Viewer = True
        print(self.Player,self.Viewer)

M= Muzzamil()
W = Wajahat()
Mo = Moiz()

for x in (M,W,Mo):
    x.Cricket()