from xml.etree.ElementTree import tostring
from twitchio.ext import commands
import pvz

class Bot(commands.Bot):


    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token="YOURTWITCHTOKEN", prefix='?', initial_channels=['elmarceloc'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def sun(self, ctx: commands.Context):
        #await ctx.send(f'Hello {ctx.author.name}!')
        pvz.collectSun()

    @commands.command()
    async def resume(self, ctx: commands.Context):
        #await ctx.send(f'Hello {ctx.author.name}!')
        pvz.resumeGame()
    @commands.command()
    async def plant(self, ctx: commands.Context):
        index = int(ctx.message.content.split(' ')[1])

        if(index is not None and index >= 1 and index <= 10 ):
            await ctx.send(f'@{ctx.author.name}, Planta número #{ str(index)} selecionada')

            pvz.selectPlant(index - 1)
    @commands.command()
    async def put(self, ctx: commands.Context):
        x = int(ctx.message.content.split(' ')[1]) -1
        y = int(ctx.message.content.split(' ')[2]) -1

        if(x is not None and y is not None and x >= 0 and x <= 9 and y >= 0 and y <= 5):
            await ctx.send(f'@{ctx.author.name}, Plantada puesta en {str(x + 1)}, {str(y + 1)}')

            pvz.clickSlot(x, y)
    @commands.command()
    async def unlock(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name}, Planta desbloqueada')

        pvz.unlockPlant()
    @commands.command()
    async def tryagain(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name}, Intentando de nuevo')

        pvz.tryagain()

bot = Bot()
bot.run()