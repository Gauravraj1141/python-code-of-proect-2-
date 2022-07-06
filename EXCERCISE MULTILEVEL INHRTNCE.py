#ELECTRONIC DEVICES , POCKET GADGET, PHONE
class Electronic_devices:
    inverter = 700
    watch = 4
    def light_charge(self):
        return f"it is consume {self.inverter} watt light {self.watch} "


class Pocket_gadget(Electronic_devices):
    watch = 20
    def light_charge(self):
        return f"it is consume {self.watch} watt light "

class Phone(Pocket_gadget):
    pass
    redmi_phone  = 3300
    def light_charge(self):
        return f"it is consume {self.redmi_phone}  mh battry "

invertr = Electronic_devices()
ghadi =  Pocket_gadget()
mobile = Phone()

print(mobile.light_charge()) # or iska khud ka function comment krne par ye apne se phle vale ka function leleta h pocket vale ka 
