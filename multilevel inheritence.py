#multilevel me ek ke bad ek me call krte h jisse phle vali ko dusri access kr skti h fir dusri or phli ko tisri access kr skti h ase krke hi multilevel inheritence hoti h

class Dad:
    basketball = 3
    dance = 4

class Son(Dad):
    dance = 5
    def howdance(self):
        return f"this is dance {self.dance} time done"
class Grandson(Son): # ye sbse phle khud k andr dhundhega attribute ko jab ise nhi milega fir son k andr jayega or uske bad dad me jayega

    dance = 89

    def howdance(self):
        return f"this is dance {self.dance} time done"

gaurav =  Dad()
harry = Son()
larry = Grandson()

print(harry.howdance())