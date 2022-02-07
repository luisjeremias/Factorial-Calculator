import time

class Factorial:
  def __init__(self):
    try:
      self.number = int(input("###################[ TYPE A NUMBER TO CALCULATE FACTORIAL ]###################\n"))
      self.total = 1
    except:
      self.__init__()

   
  def calculate(self):
    for i in range(1,self.number + 1):
      self.total = self.total * i
    time.sleep(3)
    print(f"##########[ {self.number} FACTORIAL IS: {self.total}  ]##########")
    more_cal = str(input("Do you want to calculate more? Y or N: ")).upper()
    if(more_cal == 'Y'):
      self.__init__()
      self.calculate()
    else:
      print("##########[ CLOSING! ]##########")
      time.sleep(3)


    
    
