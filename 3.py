class Painting:
    
    def __init__(self, arg1, arg2, arg3, arg4):
        
        self.pid = arg1
        self.pname = arg2
        self.pprice = arg3
        self.ptype = arg4

class ShowRoom:
    
    def __init__(self, arg1):
        
        self.plist = arg1
    
    
    def getTotalPaintingPrice(self, ptype):
        
        tprice = 0
        flag = 0
        
        for obj in self.plist:
            
            if obj.ptype == ptype:
                flag = 1
                tprice += obj.pprice
            
        if flag:
            return tprice
        
        return None 
    
    def getPainterWithMaxCountOfPaintings(self):
        
        nameCount = {}
        rslt = []
        
        for obj in self.plist:
            
            if obj.pname in nameCount:
                nameCount[obj.pname] += 1
            else:
                nameCount[obj.pname] = 1
        

        sort = sorted(nameCount.items(), key = lambda x: x[1])
        
        
        

        val = sort[-1][1]
    
        
        for value in sort:
            if val == value[1]:
                rslt.append(value[0])
                
        if len(rslt) > 1:
            rslt.sort()
            return rslt[0]
        else:
            return sort[-1][0]
        

if __name__ == "__main__":
    
    n = int(input())
    
    plist = []
    
    for val in range(n):
        
        val1 = input().lower()
        val2 = input().lower()
        val3 = int(input())
        val4 = input().lower()
        
        pobj = Painting(val1, val2, val3, val4)
        
        plist.append(pobj)
        
    
    sobj = ShowRoom(plist)
    
    ptype = input().lower()
    
    rslt = sobj.getTotalPaintingPrice(ptype)
    
    if rslt:
        print(rslt)
    else:
        print("Painting Not Found")
        
    rslt = sobj.getPainterWithMaxCountOfPaintings()
    
    print(rslt)
    
