import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret_key.json', scope)
client = gspread.authorize(creds)

sheet = client.open('spread_sheet_test').sheet1

names = ['Yota', 'Takato', 'Yosuke', 'Makoto', 'Keita']

for i in range(100):
    sheet.update_cell(random.randint(1, 10), random.randint(1, 10), random.randint(1,10))
    print(i)
