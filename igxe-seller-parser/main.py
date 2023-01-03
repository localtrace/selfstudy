import time
from seller import SellerData

while True:
    seller = SellerData('https://www.igxe.cn/cdkey-0-4812', '莱拉')
    sellerData = seller.getData()
    print(sellerData)
    time.sleep(5)
                    
                    