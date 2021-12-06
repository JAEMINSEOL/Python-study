import NumPy as np

class statistic:
    num_id=0
    def __init__(self,data):
        self.data = data
        self.data=data
        statistic.num_id+=1
    def sum(self):
        o = sum(self.data)
        return(o)
    def sd(self):
        o=np.var(self.data)
        return(o)
    def len(self):
        o=len(self.data)
        return o
    def view(self):
        print(self.data)
