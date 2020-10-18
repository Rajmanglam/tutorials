# so here we will learn about multilevel inheritence
# so let's understand it with a example

class Dad:
    basketball =6
class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"
class Grandson(Son):
    dance =6
    guitar = 1
    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"
# here we created a dad and son and grandson
# here son inherited dad
# and grandson inherited son
# therefore grandson also inherited dad which means it can use all attributes of dad and son also
darry = Dad()
larry = Son()
harry = Grandson()

# exercise
# electronic device
# pocket gadget
# phone
class electronicdevice():
    def portabality(self):
        return 'can be yes or no'

class pocketgadget():
    def portabality(self):
        return 'yes'


class phone():
    def portabality(self):
       return 'very portable'
mobile=phone()
print(mobile.portabality())