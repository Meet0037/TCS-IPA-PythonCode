# TCS-IPA-PythonCode


Ex:1

    class DairyProduct:

        def __init__(self, *args):
            self.dairyId = int(args[0])
            self.dairyBrand = args[1]
            self.productType = args[2]
            self.price = int(args[3])
            self.grade = args[4]

    class ProductGrade:

        def __init__(self, *args):
            self.dairyList = args[0]
            self.wgtDict = args[1]

        def priceBasedOnBrandAndType(self, brand, ptype):

            ans = []

            for obj in self.dairyList:

                if obj.dairyBrand == brand and obj.productType == ptype:

                    obj.price += (obj.price * self.wgtDict[obj.grade]) / 100

                    ans.append((brand, obj.price))

            if len(ans):
                return ans
            else:
                return None






    if __name__ == "__main__" :

        n1 = int(input())

        dairyProducts = []

        for i in range(n1):

            dId = input()
            dBrand = input()
            pType = input()
            price = input()
            grade = input().lower()

            dpObj = DairyProduct(dId, dBrand, pType, price, grade)

            dairyProducts.append(dpObj)


        n2 = int(input())

        wgtDict = {}

        for i in range(n2):

            grade = input().lower()
            value = int(input())

            wgtDict[grade] = value

        pgObj = ProductGrade(dairyProducts, wgtDict)

        dairyBrand = input()
        productType = input()

        rslt = pgObj.priceBasedOnBrandAndType(dairyBrand, productType)

        if rslt:

            for item in rslt:
                print("Dairy Brand:", item[0])
                print("Price:", item[1])

        else:
            print("No dairy product found")


