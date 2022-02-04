import asyncio, kahoot, os, sys

def clrscr():
    # Windows
    if os.name == 'nt':
        _ = os.system('cls')
  
    # Mac/Linux
    else:
        _ = os.system('clear')
        
clrscr()
bot = kahoot.client()
pin = input('Enter game pin> ')
botname = input('Enter bot name> ')
botnum = 50000 # input('Enter number of bots> ')
async def run(digit):
    bot.join(pin, botname+str(digit))
    clrscr()
    print(botname+str(digit))
try:
    for digit in range(botnum):
        asyncio.run(run(digit))
except KeyboardInterrupt:
    sys.exit()
