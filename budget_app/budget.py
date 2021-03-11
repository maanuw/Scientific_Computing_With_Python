class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.balance = 0
        self.total_withdrawn = 0

    def deposit(self, amount, description=None):
        if description==None:
            description=''
        self.ledger.append({"amount":amount, "description":description})
        self.balance = self.balance + amount

    def withdraw(self, amount, description=None):
        self.total_withdrawn = self.total_withdrawn + amount
        if description==None:
            description=''
        if self.check_funds(amount) == True:
            self.ledger.append({"amount":-amount, "description":description})
            self.balance = self.balance - amount
            return True
        return False

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, other):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + other.category)
            other.deposit(amount, "Transfer from " + self.category)
            return True
        return False
        
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        line = ''
        for i in range(len(self.ledger)):
            if len(self.ledger[i]["description"]) >=24:
                line = line + self.ledger[i]["description"][0:23] + " "*(7-len("{:.2f}".format(self.ledger[i]["amount"]))) + "{:.2f}".format(self.ledger[i]["amount"]) + "\n"
            else:
                line = line + self.ledger[i]["description"] + " "*(23-len(self.ledger[i]["description"])) + " "*(7-len("{:.2f}".format(self.ledger[i]["amount"]))) + "{:.2f}".format(self.ledger[i]["amount"]) + "\n"
        return ("*"*((30-len(self.category))//2)) + self.category + ("*"*((30-len(self.category))//2))+"\n" + line + "Total: " + "{:.2f}".format(self.get_balance())
        
        




def create_spend_chart(categories):
    cat_per =[]
    for i in range(len(categories)):
        rounded_percent = 0
        percent = (categories[i].total_withdrawn/(categories[i].get_balance() + categories[i].total_withdrawn))*100
        #rounding the value
        lowerten = int(((percent)//10)*10)
        upperten = int((((percent)//10)+1)*10)
        if (percent-lowerten) < (upperten-percent):
            rounded_percent = lowerten
        else:
            rounded_percent = upperten
        #Add the percent to a list percentages corresponding to list categories.
        cat_perc.append((categories[i], rounded_percent))

    title = "Percentage spent by category" + "\n"
    line100 = "100|" + " " +

    for i in range(0, 101):
        if i%10 == 0:
            


    
        
        


































