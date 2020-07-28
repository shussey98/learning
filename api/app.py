import time
from libs.openexchange import OpenExchangeClient

APP_ID = 'e5d9739215664df7bd26d8e7ed04faa0'

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "EUR", "GBP")
end = time.time()

print(end-start)



print(f'{gbp_amount:.2f}')