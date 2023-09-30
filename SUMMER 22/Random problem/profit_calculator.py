import sys 
sys.setrecursionlimit(15000)
class FinalQ:
    def print(self,array,idx):
        if(idx<len(array)):
            profit=self.calcProfit(array[idx])
            print("Investment",array[idx],"Profit:",profit)
            self.print(array,idx+1)
    def calcProfit(self,investment):
        if investment==25000:
            return 0.0
        if investment<=100000:
            return 4.5 + self.calcProfit(investment-100)
        else:
            return 8 + self.calcProfit(investment-100)
array=[25000,100000,250000,350000] 
f = FinalQ() 
f.print(array,0)