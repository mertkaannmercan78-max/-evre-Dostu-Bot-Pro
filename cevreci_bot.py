import discord
from discord.ext import commands
import requests
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir çevre duyarlılık botuyum!$komut yazarak komutlarımı öğrenebilirsin.Size nasıl yardımcı olacilirim? ')

@bot.command()
async def komut(ctx):
    await ctx.send(f'Komutlar: atıklar,onemli_bilgiler,yapmamiz_gerekenler,yapmamiz_gerekenler')

@bot.command()
async def onemli_bilgiler(ctx):
    await ctx.send(f'Yok olma süreleri:\nplastik: 400-1000 yıl,\nkağıt: 2-5 ay,\ncam: 4.000-5.000 yıl,\nmetal: 10-100 yıl')
@bot.command()
async def yapmamamiz_gerekenler(ctx):
    await ctx.send(f"atıkları öğrendinten sonra ve önemli bilgileri öğrendiğimizden sonra yapmamamız gerekenler ise şunlar; yerlere atıkları atmamalıyızgeri dönüşülebilir eşyaları geri dönüşüme atmalıyıgeri dönüşümeyen atıkları geri dönüşüme atmamalayız")

@bot.command()
async def yapmamiz_gerekenler(ctx):
    await ctx.send(f"atıkları öğrendinten sonra ve önemli bilgileri öğrendiğimizden sonra yapmamız gerekenler ise şunlar Ağaçları ve ormanları korumalıyız.Kısa mesafelerde yürümeyi veya bisiklete binmeyi tercih etmeliyiz.Çevremizdeki insanları da çevreyi korumaya teşvik etmeliyiz.")

@bot.command()
async def atiklar(ctx):
    await ctx.send(f"Tenekeler\nSünger\nSigara İzmariti\nPamuk ve kulak çubuğu\nMercek\n Daha fazla için $baska komutunu yaz yeter😊")

@bot.command()
async def baska(ctx):
    await ctx.send(f"Sakız\nCam\nKarton \nStrafor Köpük\nYapışkanlı etiketler")
