class Property:
    
    def __init__(self, arg1, arg2, arg3):
        
        self.pType = arg1
        self.pValue = arg2
        self.max_Bprice = arg3
    
class Tender:
    
    def __init__(self, arg1, arg2, arg3):
        
        self.bName = arg1
        self.pType = arg2
        self.bPrice = arg3
        
def bidProperty(pObjs, tObjs):
    
    nameList = []
    
    typeSet = set()
    
    removeObj = set()
    
    objDict = {}
    
    for obj1 in tObjs:
        
        for obj2 in pObjs:
            
            #Condition1
            
            if obj1.pType.lower() == obj2.pType.lower():
                
                #Condition2
                
                if obj1.pType.lower() in objDict:
                    
                    if objDict[obj1.pType][1] < obj1.bPrice:
                        
                        objDict[obj1.pType.lower()] = (obj1.bName, obj1.bPrice)
                    
                else:
                    objDict[obj1.pType.lower()] = (obj1.bName, obj1.bPrice)
                        
            
                #Condition3
                
                if obj1.bPrice >= obj2.pValue and obj1.bPrice <= obj2.max_Bprice:
                    
                    typeSet.add(obj1.pType.lower())
                    removeObj.add(obj2)
                

    for pType in typeSet:
        nameList.append(objDict[pType][0])
        
    for obj in removeObj:
        pObjs.remove(obj)
    
    return nameList
    

if __name__ == "__main__":
    
    n1 = int(input())
    
    pObjs = []
    
    for num in range(n1):
        
        property_type = input()
        property_value = int(input())
        max_bid_price = int(input())
        
        pObj = Property(property_type, property_value, max_bid_price)
        
        pObjs.append(pObj)
    
    n2 = int(input())
    
    tObjs = []
    
    for num in range(n2):
        
        buyerName = input()
        propertyType = input()
        bidPrice = int(input())
        
        tObj = Tender(buyerName, propertyType, bidPrice)
        
        tObjs.append(tObj)
    
    returnValue = bidProperty(pObjs, tObjs)

    if len(returnValue):
        
        for name in returnValue:
            print(name)
    
    else:
        print("Property Not Found")
    
    for obj in pObjs:
        
        print(obj.pType)
