class Rock:
    def __init__(self,rock_name,rock_category):

        self.name = rock_name
        self.category = rock_category

    def getname(self):
        return self.name
    
    
    def getcategory(self):
        return self.category
    
if __name__ == "__main__":
    rock1 = Rock("quartz", "mineral")
    print("This is" , rock1.getname(), "and it's a" , rock1.getcategory())