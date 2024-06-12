class Point:
    def _init_(self,x,y):
        print("init called")
        self.x=x
        self.y=y
    def _str_(self):
        print("str called")
        return "[{0},{1}]".format(self.x,self.y)
    def _add_(self,obj):
        print("add called")
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)



p1=Point(10,20)
print(p1)
p2=Point(30,40)
print(p2)
print("Addition of 2 obj: ",p1+p2)
    
