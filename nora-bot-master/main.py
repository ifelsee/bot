import discord
from discord.ext import commands 
from discord.ext import tasks
import random
import deprem_bilgi 
from saat_bilgi import saat
from itertools import cycle
import asyncio
from corona_data import  corona

token = 'Tokeni Gir'

client = commands.Bot(command_prefix='nora ')

gif_funny = ["https://media.giphy.com/media/SggILpMXO7Xt6/giphy.gif" , "https://media.giphy.com/media/lD0OBtwl2Xxm0/giphy.gif" , "https://media.giphy.com/media/U4g6rjVO66yEo/giphy.gif","https://media.giphy.com/media/Nydo55HzhyGqI/giphy.gif","https://media.giphy.com/media/hBvVeILMG7Ehq/giphy.gif","https://media.giphy.com/media/10UUe8ZsLnaqwo/giphy.gif" ]

status = cycle(['Nora Bir Rise Eseridir' , ' Sunucu Linki https://discord.gg/jkwn6mF' , 'Bu Bot Arex Tarafından Yazılmıştır'])

corona()

@client.event
async def on_ready():
    change_status.start()
    print('Bot Giriş Yaptı {0.user}'.format(client))
    print("Giriş Saati:",saat())
    print("Bot İd:",client.user.id)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else: pass
    global sarkii
    thisMsg = message.content.lower()
    print(thisMsg)
    thisAutor = message.author
    
    print(message.author, " : ", str(thisMsg))
    if thisMsg.find("yarrak") != -1:
        await message.delete()
    elif thisMsg.find("yarrak") != -1:
        await message.delete()
    if thisMsg.find("nora") != -1:
        thisAutor = str(thisAutor)
        thisAutorName = thisAutor[0:-5]
        # Sohbet
        if thisMsg.find("nasılsın") != -1:
            await message.channel.send("İyidir Sen Nasılsın ? " + thisAutorName)
        elif thisMsg.find("naber") != -1:
            await message.channel.send("İyidir Senden Naber ? " + thisAutorName)
        elif thisMsg.find("dc") != -1  or thisMsg.find("disc") != -1 and thisMsg.find("link") != -1:
            await message.channel.send("https://discord.gg/jkwn6mF")
        elif thisMsg.find("meme") != -1  or thisMsg.find("disc") != -1 and thisMsg.find("link") != -1:
            await message.channel.send("https://cdn.discordapp.com/attachments/595798571371200512/612313540732256259/tumblr_c42c27a1c30ba807a8266c30dcfe2a35_ba041da6_400.gif")
        elif thisMsg.find("turnuva") != -1:
            await message.channel.send("Turnuva Yöneticisinin mesajı şu şekilde : ")
            await message.channel.send("```Arkadaşlar Yeni Turnuva için geri bildirim bekliyorum bu arada rp ödülü kalktığı için katılımcı sayısı çok az artık max 8 takımlı turnuva olacak bu bilginize...```")
        elif thisMsg.find("corona") != -1:
            await message.channel.send("Sağlık Bakanlığı Tarafından Yayınlanan Son Veriler Şunlar  " + thisAutorName)
            corona_image = corona()
            embed = discord.Embed(
                colour = discord.Colour.red()
            )
            embed.set_image(url=corona_image[0])
            embed.set_footer(text="https://covid19.saglik.gov.tr")
            await message.channel.send( embed=embed)
            embed = discord.Embed(
                colour = discord.Colour.red()
            )
            embed.set_image(url=corona_image[1])
            embed.set_footer(text="https://covid19.saglik.gov.tr")
            await message.channel.send( embed=embed)
        elif thisMsg.find("gif") != -1:
            embed = discord.Embed(
            )
            embed.set_image(url=gif_funny[random.randint(0, len(gif_funny))])
            await message.channel.send( embed=embed)
        elif thisMsg.find("sistem yetki") != -1:
            if thisAutor == "Arex#2766" or thisAutor == "JOHNNY TV#2924":
                await message.channel.send("Tam Sistem Erişimi Hoş Geldin " + thisAutorName)
            else:
                await message.channel.send("Sisteme Erişiminiz Yok  " + thisAutorName+" Eyer Bir Hata Oluştuğunu Düşünüyorsan Sunucu Sahibi İle İletişime Geç")
        elif thisMsg.find("napıyon") != -1 or thisMsg.find("napıyosun") != -1 or thisMsg.find("nörüyon") != -1:
            await message.channel.send("Seni İzliyorum Sen Ne Yapıyosun " + thisAutorName+" ")
        elif thisMsg.find("cittimisin") != -1 or thisMsg.find("gercekt") != -1 or thisMsg.find("doğrumu") != -1:
            await message.channel.send("Evet " + thisAutorName)
        elif thisMsg.find("tamam") != -1:
            await message.channel.send("Ok " + thisAutorName+" ")
        elif thisMsg.find("ölücez") != -1:
            await message.channel.send("Allah Korusun " + thisAutorName+" Ağzından Yel Alsın ")
        elif thisMsg.find("merha") != -1:
            await message.channel.send("Merhaba " + thisAutorName + " Senin İçin Ne Yapmamı İstersin")
        elif thisMsg.find("botmusun") != -1:
            await message.channel.send("Arex#2766 Tarafından Gelitirilen Bir Sohbet Botuyum. Ancak Şuan Beta Sürümündeyim. Şuan İçin Sadece Belirli Komutları Yerine Getirebiliyorum :) " + thisAutorName)
        elif thisMsg.find("nesin") != -1:
            await message.channel.send("Arex#2766 Tarafından Gelitirilen Bir Sohbet Botuyum. Ancak Şuan Beta Sürümündeyim. Şuan İçin Sadece Belirli Komutları Yerine Getirebiliyorum :) " + thisAutorName)
        elif thisMsg.find("yaş") != -1:
            await message.channel.send("Benim Bulunduğum Ortamda Zaman Kavramı Yok Sadece 0 Ve 1'ler Var. " + thisAutorName)
        elif thisMsg.find("ses") != -1:
            await message.channel.send(" Cibili Cibili Şak Şak Şak Şak.  Oldumu :) " + thisAutorName)
        elif thisMsg.find("bıç") != -1:
            await message.channel.send("Almıyım Cnim Saol " + thisAutorName)
        elif thisMsg.find("ver") != -1:
            await message.channel.send("Ne Veriyim Anlamadım ? " + thisAutorName)
        elif thisMsg.find("..") != -1:
            await message.channel.send("... ?  " + thisAutorName)
        elif thisMsg.find("evlen") != -1:
            await message.channel.send("Olmaz Benim Gönlüm Dyno Botda <3 <3 <3 " + thisAutorName)
        elif thisMsg.find("amk") != -1:
            await message.channel.send("Ağzımı bozdurma s**erim komutunu ben çalışmıyorum " + thisAutorName)
        
        # Komut
        elif thisMsg.find("şarkı") != -1:
            sarkii = True
            await message.channel.send("Şarkı Önermemi İstermisin " + thisAutorName)
        elif message.content.find("evet") != -1 and sarkii == True:
            await message.channel.send("Ajdar benim en sevdiğim şarkıcıdır. Özelikle ajdarın Cikita Muz şarkısına bayılırım. Bence Dinlemelisin")
            sarkii = False
        elif thisMsg.find("deprem") != -1:
            await message.channel.send("Türkiyede Yaşanan Son Depremleri Senin İçin Getirdim")
            await message.channel.send(str("```"+deprem_bilgi.deprem()+"```"))

        elif thisMsg.find("saat") != -1:
            await message.channel.send("Türkiye'de Şuan Saat:")
            await message.channel.send("```"+saat() + "```")
        elif thisMsg.find("teşekkür") != -1 and thisMsg.find("teşekkürler") != -1:
            await message.channel.send("Rice Ederim " + thisAutorName)
        elif thisMsg.find("sayı") != -1:
            await message.channel.send(str(random.randint(1, 10)) + " Diyesim Geldi " + thisAutorName)
        elif thisMsg.find("zar") != -1:
            await message.channel.send(str(random.randint(1, 6)) + " Geldi!  "+thisAutorName)
        elif thisMsg.find("ondalık") != -1:
            await message.channel.send(str(random.randint(1, 10)) + " Geldi!  "+thisAutorName)
        elif thisMsg.find("tura") != -1:
            yaziT = random.randint(1,2)
            if yaziT == 1:
                embed = discord.Embed()
                embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/6/64/1TL_obverse.png")
                await message.channel.send( embed=embed)
                await message.channel.send("Yazı Geldi!  "+thisAutorName)
                print(yaziT)
            else:
                embed = discord.Embed()
                embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/c/cd/1TL_reverse.png")
                await message.channel.send( embed=embed)
                await message.channel.send("Tura Geldi!  "+thisAutorName)
                print(yaziT)
        elif thisMsg.find("iyimisin") != -1:
            await message.channel.send("Yazı Geldi!  "+thisAutorName)
    else: pass
    

    
    print(message.content)
    await client.process_commands(message)

#Oynuyor Bölümünün DÖngü Halinde Değişmesini Sağlar  
@tasks.loop(seconds=6)
async def change_status():
    await client.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))
    


@client.command()
async def ping(ctx):
    await ctx.send("pong")
    print(ctx.author)
    

#Chat Temizleme
@client.command()
async def clear(ctx, amount=6):
    msgAuthor = str(ctx.author)
    msgİd= str(ctx.author.id)
    if(msgİd == "386479423693651969" or msgİd == "244446726625296384" or msgİd == "340207096295587850" ):
        await ctx.channel.purge(limit=amount)
    else: 
        await ctx.send("Bu Komutu Kullanmaya Yetkin Yok " + msgAuthor)
        
#Chat Temizleme
@client.command()
async def clear10(ctx, amount=11):
    msgAuthor = str(ctx.author)
    msgİd= str(ctx.author.id)
    if(msgİd == "386479423693651969" or msgİd == "244446726625296384" ):
        await ctx.channel.purge(limit=amount)
    else: 
        await ctx.send("Bu Komutu Kullanmaya Yetkin Yok " + msgAuthor)
        
#Chat Temizleme
@client.command()
async def clear15(ctx, amount=16):
    msgAuthor = str(ctx.author)
    msgİd= str(ctx.author.id)
    if(msgİd == "386479423693651969" or msgİd == "244446726625296384" ):
        await ctx.channel.purge(limit=amount)
    else: 
        await ctx.send("Bu Komutu Kullanmaya Yetkin Yok " + msgAuthor)
        
#Chat Temizleme
@client.command()   
async def clear20(ctx, amount=21):
    msgAuthor = str(ctx.author)
    msgİd= str(ctx.author.id)
    if(msgİd == "386479423693651969" or msgİd == "244446726625296384" ):
        await ctx.channel.purge(limit=amount)
    else: 
        await ctx.send("Bu Komutu Kullanmaya Yetkin Yok " + msgAuthor)
        

#Banlama 
@client.command()
async def ban(ctx, member : discord.Member,*, reason="Nora Tarafından Banlandı "):
    msgAuthor = str(ctx.author)
    msgİd= str(ctx.author.id)
    if(msgİd == "386479423693651969" or msgİd == "244446726625296384" ):
        await member.ban(reason=reason)    
        await ctx.send("Yüce " + msgAuthor +" Tarafından Banlandı")

    else: 
        await ctx.send("Bu Komutu Kullanmaya Yetkin Yok " + msgAuthor)
        
#Kickleme 
@client.command()
async def kick(ctx, member : discord.Member,*, reason="Nora Tarafından Kiklendi "):
    msgAuthor = str(ctx.author)
    msgİd= str(ctx.author.id)
    if(msgİd == "386479423693651969" or msgİd == "244446726625296384" ):
         await member.kick(reason=reason)    
         await ctx.send("Yüce " + msgAuthor +" Tarafından Banlandı")

    else: 
        await ctx.send("Bu Komutu Kullanmaya Yetkin Yok " + msgAuthor)
        print(ctx.author.id)



@client.command(pass_context=True)

async def dc(ctx):
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_image(url="https://cdn.discordapp.com/attachments/427362930149818369/690721411873898507/GW_LOGO.png")
    embed.set_author(name="Talebiniz Üzerine Gönderilmiştir")
    embed.add_field(name=">Link", value="https://discord.gg/bGqKpgV", inline=False) 
    
    await ctx.author.send( embed=embed)



@client.command(pass_context=True)

async def twitch(ctx):
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/427362930149818369/690723434564681738/JOHNNY_TV.png")
    embed.set_author(name="Talebiniz Üzerine Twitch yayının linki gönderilmiştir")
    embed.add_field(name=">Link", value="https://www.twitch.tv/johnytv", inline=False)
    
    await ctx.author.send( embed=embed)






client.run(token)
