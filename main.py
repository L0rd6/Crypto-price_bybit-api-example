from requests import Session

req = Session()

coin = #coin name

coin_info = req.get(f'https://api-testnet.bybit.com/public/linear/recent-trading-records?symbol={coin}USDT&limit=1').json()['result'][0]['price']

print(coin,coin_info)
