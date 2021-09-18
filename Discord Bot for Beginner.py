import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='&')                                  # กำหนด Prefix ในการเรียก Command
#bot.ชื่อตัวแปร = ค่าอะไรก็ได้                                                # ประกาศตัวแปรไว้ใช้ทั้งโปรแกรม

@bot.command()                                                          # bot.command จะทำงานเมื่อถูกคนเรียก
async def ชื่อคำสั่ง(ctx) :
    await ctx.send('Hello XDDDDDDDDDD')                                 # ctx.send คล้าย ๆ print แต่จะส่งไปทางแชท Discord แทน

@bot.event                                                              # bot.event จะทำงานเอง
async def on_ready() :                                                  # เมื่อบอทเริ่มต้น
    await bot.change_presence(activity=discord.Game(name="ชื่อสถานะ"))
    print("Bot has been Started!")                                      # Print แสดงผลใน CMD

@bot.listen()                                                           # bot.event จะทำงานเองโดยรับข้อความจากแชท
async def on_message(message):
	if "สวัสดี" in message.content.lower():                               # ถ้าเจอ "สวัสดี" ในแชทให้...
		await message.channel.send('สวัสดีย์')                             # ส่งข้อความทันทีว่า "สวัสดีย์"

bot.run('ใส่ Token')                                                     # รันบอท (โดยนำ Token จากบอทที่เราสร้างไว้นำมาวาง)
#bot.run(os.environ["ชื่อตัวแปรที่เราตั้ง"])                                   # อันนี้กรณีจะเก็บ Token ไว้บนคอมเรา 
