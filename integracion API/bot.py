import discord
from discord.ext import commands 
from api import get_data_from_api
from api import take_info
from voz import sintesis_voz

#configuración del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents= intents)

#eventos
@bot.event
async def on_ready():
    print(f"bot en linea")

#comandos
@bot.command()
async def clima(ctx):
    await ctx.send("introduce el nombre de la ciudad de la cual quieres conocer el clima")

    def verificar(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        message = await bot.wait_for("message", check=verificar, timeout=30)
        ciudad = message.content
        clima = get_data_from_api(ciudad)
        await ctx.send(f"el clima en {ciudad} es: {clima}")
    except:
        await ctx.send("no se recibió una respuesta a tiempo")

@bot.command()
async def dato(ctx):
    dato_random = take_info()
    await ctx.send("sabías que")
    await ctx.send(dato_random)
    sintesis_voz(dato_random)

bot.run("token")