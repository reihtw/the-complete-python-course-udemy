import time
from libs.openexchange import OpenExchangeClient

APP_ID = "833c5505c5b14bbab4e9f74ae2e2e30a"

client = OpenExchangeClient(APP_ID)

from_amount = 1
from_currency = 'BRL'
to_currency = 'VEF'

start = time.time()
to_amount = client.convert(from_amount, from_currency, to_currency)
end = time.time()

print(end-start)
print(f'{from_currency}{from_amount:.2f} is {to_currency}{to_amount:.2f}')
