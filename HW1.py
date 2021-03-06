class Stock():
    StockList={}
    def __init__(self, price, symbol):
        self.price=price
        self.symbol=symbol
        self.StockList.update({symbol: price})
        
    def __repr__(self):
        return self.symbol
    
class MutualFund():
    MutualFundList={}
    def __init__(self, symbol):
        self.symbol=symbol
        self.MutualFundList.update({symbol: 1})
        
    def __repr__(self):
        return  self.symbol

class Portfolio():
    import random as rand
    
    def __init__(self,cashP=0):
        self.cashP=cashP
        self.StData={}
        self.MfData={}
        self.TransactionList=[]
        self.TransactionList.append('The account is created with the initial balance: ' + str(self.cashP))
        
        print('Your portfolio has been created')
        
    def __str__(self):
        
        print('{:>15}'.format('cash: $')+str(round(self.cashP,2)))
        
        if len(self.StData.keys())>0:
            print('{:>14}'.format('stock: '),end="")
            for i in self.StData.keys():
                print(str(self.StData[i]) +' \t' +str(i))
                print('{:>14}'.format(''),end="")
        else:
            None
        
        if len(self.MfData.keys())>0:
            print('\rmutual funds: ',end="")
            for i in self.MfData.keys():
                print(str(round(self.MfData[i],2)) +' \t' +str(i))
                print('{:>14}'.format(''),end="")
        else:
            None
        
        print('\r')
        return  ''
        
    def addCash(self, cash):
        self.cashP +=cash
        print('You currently have: ' + str(self.cashP))
        self.TransactionList.append( str(cash)+ ' cash added to the portfolio')
        
    def withdrawCash(self, amount):
        
        if amount > self.cashP:
            print('You dont have enough money to do this transaction')
            self.TransactionList.append( 'You tried to withdraw ' + str(amount) + ' amount cash but you did not have enough cash.')
        else:
            self.cashP -=amount
            print('You withdrawed money and currently you have: ' + str(self.cashP))
            self.TransactionList.append( 'You withdrawed ' + str(amount) + ' cash.')
        
    def buyStock(self, amount, symbol):
        
        if  symbol.price*amount>self.cashP:                                    #amount*Stock.StockList[symbol] > self.cashP:
            print('You dont have enough money to do this transaction')
            self.TransactionList.append( 'You tried to buy '+str(amount)+' shares of ' +str(symbol)+ ' but you did not have enough cash.')
            
        else:
            if symbol in self.StData.keys():
                self.StData[symbol] +=amount
            else:
                self.StData.update({str(symbol): amount})

            self.cashP -= symbol.price*amount       
            print ('You spend ' +str(symbol.price*amount) + ' you currently have ' + str(self.cashP))
            self.TransactionList.append( 'You bought ' +str(amount) +' shares of stock ' + str(symbol))
            
    def sellStock(self, symbol, amount): 
        import random as rand
        if amount>self.StData[symbol]:
            print('You dont have enough share to do this transaction')
            self.TransactionList.append( 'You tried to sell '+str(amount)+' shares of ' +str(symbol)+ ' but you did not have that much shares.')
        else:
            self.StData[symbol] -=amount
            buyingPrice=Stock.StockList[symbol]
            sellingPrice=rand.uniform(buyingPrice*0.5,buyingPrice*1.5)
            sellingPrice=round(sellingPrice,2)
            self.cashP +=sellingPrice*amount
            print('You sold a share at :' +str(sellingPrice)+' and from this transaction you gained '                  +str(sellingPrice*amount) + ' you currently have '+str(self.cashP))
            self.TransactionList.append( 'You sold ' +str(amount) +' shares of stock ' + str(symbol))
            
    def buyMutualFund(self, amount, symbol):
        if  amount>self.cashP:
            print('You dont have enough money to do this transaction')
            self.TransactionList.append( 'You tried to buy '+str(amount)+' amount mutual fund ' +str(symbol)+ ' but you did not have enough cash.')
        else:
            if symbol in self.MfData.keys():
                self.MfData[symbol] +=amount
            else:
                self.MfData.update({str(symbol): amount})

            self.cashP -= amount       
            print ('You spend ' +str(amount) + ' you currently have ' + str(self.cashP))
            self.TransactionList.append( 'You bought ' +str(amount) +' amount mutual fund ' + str(symbol))
    
    def sellMutualFund( self, symbol, amount):
        import random as rand
        if amount > self.MfData[symbol]:
            print('You dont have enough mutual fund to do this transaction')
            self.TransactionList.append( 'You tried to sell '+str(amount)+' amount of ' +str(symbol)+ ' mutual fund but you did not have that much.')
        else:
            self.MfData[symbol] -=amount
            sellingPrice=rand.uniform(0.9,1.2)
            sellingPrice=round(sellingPrice,2)
            self.cashP +=sellingPrice*amount
            print('You sold a share at :' +str(sellingPrice)+' and from this transaction you gained '                  +str(sellingPrice*amount) + ' you currently have '+str(self.cashP))
            self.TransactionList.append( 'You sold ' +str(amount) +' amount of mutual fund ' + str(symbol))
            
    def history(self):
        
        for i in self.TransactionList:
            print(i)    
            

