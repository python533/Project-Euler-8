class enbüyük():
    def __init__(self,product,biggest):
        self.product=product
        self.biggest=biggest

    def hesapla(self,n):
        for i in range(1000):
            self.product=int(n[i]) * int(n[i+1]) *int(n[i+2]) * int(n[i+3])
            self.biggest=max(self.biggest,self.product)
            print(self.biggest)



