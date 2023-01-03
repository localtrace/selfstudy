import requests
import cfscrape


username = 'saloeroblam30'
password = 'wMk8XOqimWiOy8qt243'


class Account:
    HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Content-Length': '116'
    }
    DATA = {
        "type": "auth",
        "username": username,
        "password": password,
        "remember": "false",
        "language": "en_US",
    }
    
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.session = cfscrape.create_scraper()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36', 
            })

    def get_info(self):
        self.session.get('https://account.riotgames.com/') # setting up cookies
        token_auth_link = self.session.put('https://auth.riotgames.com/api/v1/authorization', headers=self.HEADERS, json=self.DATA)
        token_auth_uri = token_auth_link.json()['response']['parameters']['uri']
        self.session.get(token_auth_uri)
        account_info = self.session.get('https://account.riotgames.com/api/account/v1/user')
        return account_info.json()
    

acc = Account(username, password)
print(acc.get_info())

