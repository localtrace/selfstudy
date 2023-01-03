import requests
import json
from datetime import datetime

class SellerData:
    headers = {'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0'}
    
    
    def __init__(self, page, sellerName):
         self.page = page
         self.sellerName = sellerName
    
    
    def _sellerExist(self, sellers, name):
        for seller in sellers:
            if seller.get('seller_name') == name:
                return True
        return False
    
    
    def _parseSellerResult(self, initial_char, html_page):
        # Parsing every char after 'seller_result: [' string in html page until finds for ]
        # Returns formatted json with string [{...}]
        result = ''
        counter = 0
        
        while(True):
            char = html_page.text[initial_char + counter]
            result += char
            if char == ']':
                break
            counter += 1
        
        return json.loads(result)
    
    
    def getData(self):
        html_page = requests.get(self.page, headers=self.headers)
        sellerResultIndex = html_page.text.find('sellers_result:') 
        
        # Verify if sellers_result rendered
        if not sellerResultIndex:
            raise Exception('something went wrong. http request or sellers_result: not found')
        
        # Initial index for 'seller_result:' inside script tag
        initial_char = sellerResultIndex + 16
        sellers = self._parseSellerResult(initial_char, html_page)
        
        # Verify if seller exists
        if not self._sellerExist(sellers, self.sellerName):                                            
            raise Exception('Seller does not exist anymore :C')   
        
        # Getting data about seller and stock
        for seller in sellers:
            if seller.get('seller_name') == self.sellerName:
                    return {'Seller': seller.get('seller_name'),
                            'Stock': seller.get('stock'),
                            'PricePerUnit': seller.get('unit_price'),
                            'Date': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                        }
