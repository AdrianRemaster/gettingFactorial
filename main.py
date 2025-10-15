class fact:
    def __init__(self, number):
        self.number = number

    def calculate(self):
        LL = []
        for i in range(1, self.number+1):
            
            LL.append(i)

        
        
        intager = 1
        rn = 0
        for i in LL:
            intager *= i
            
            

        return intager
    
# obj = fact(9)

# print(obj.calculate())
