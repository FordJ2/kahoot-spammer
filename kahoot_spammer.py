import asyncio, os, sys
from kahoot import client
_ = os.system('clear')
bot = client()
pin = input('Enter game pin> ')
botname = 'notalan'
async def run(digit):
    bot.join(pin, botname+str(digit))
    _ = os.system('clear')
    print(botname+str(digit))
try:
    for digit in range(50000):
        asyncio.run(run(digit))
except KeyboardInterrupt:
    sys.exit()