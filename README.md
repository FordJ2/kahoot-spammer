# kahoot-spammer

dependancy: `pip3.9 install kahootpy`

execution: `python3.9 spam.py`

```py
import asyncio, kahoot, os, sys
_ = os.system('clear')          # should be 'cls' on windows
bot = kahoot.client()
pin = input('Enter game pin> ')
botname = input('Enter bot name> ')
botnum = 50000 #input('Enter number of bots> ')
async def run(digit):
    bot.join(pin, botname+str(digit))
    _ = os.system('clear')      # should be 'cls' on windows
    print(botname+str(digit))
try:
    for digit in range(botnum):
        asyncio.run(run(digit))
except KeyboardInterrupt:
    sys.exit()
```
