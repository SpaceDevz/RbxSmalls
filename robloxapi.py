import requests
import json
from bs4 import BeautifulSoup
import shlex

# def legitFedora():
    #print("Legit Fedora ")
    #print(rapstring + rapvalue)


    #value = rapvalueINT + 2500
    #print("Value: " + str(value))


# legitFedora()

# BOT PART

import os

import discord

TOKEN = "Nzg0OTgyNDgxMTQ5MTAwMDUz.X8xN5w.CiuaGse-phesHJfrfkdKaFT91vY"

client = discord.Client()


@client.event
async def on_ready():
    print(
        f'{client.user} is connected to the following guild:\n'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!scissors':
        
        page = requests.get("https://www.roblox.com/catalog/6550129/Scissors")
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all(class_="text-robux-lg wait-for-i18n-format-render")
        bestprice = price[0]
        textstring= "Bestprice: "

        rapstring= "RAP: "
        url = "https://economy.roblox.com/v1/assets/6550129/resale-data"
        r = requests.get(url)
        cont = r.json()
        rapvalue= str(cont['recentAveragePrice'])
        rapvalueINT = cont['recentAveragePrice']

        embedVar = discord.Embed(title="Scissors", color=0x00FFFF)
        embedVar.add_field(name="Rap", value=f'{rapvalue}', inline=True)
        embedVar.add_field(name="Value", value=f'32,000', inline=True)
        embedVar.add_field(name="Demand", value=f'Normal', inline=True)
        embedVar.add_field(name="Trend", value=f'Stable', inline=True)
        embedVar.add_field(name="Best Price", value=f'{bestprice.prettify().split()[3]}', inline=True)
        embedVar.add_field(name="Copies (Avail/Premium)", value=f'4,324/327', inline=True)
        embedVar.add_field(name="Comments", value=f'Proof Based #proofs', inline=True)
        embedVar.set_thumbnail(url="https://www.roblox.com/thumbs/asset.ashx?width=420&height=420&assetid=6550129")
        await message.channel.send(embed=embedVar)
        print(rapvalue.split())

    if message.content == '!snowflake':
        
        page = requests.get("https://www.roblox.com/catalog/67201161/Snowflake-Shutter-Shades")
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all(class_="text-robux-lg wait-for-i18n-format-render")
        bestprice = price[0]
        textstring= "Bestprice: "

        rapstring= "RAP: "
        url = "https://economy.roblox.com/v1/assets/67201161/resale-data"
        r = requests.get(url)
        cont = r.json()
        rapvalue= str(cont['recentAveragePrice'])
        rapvalueINT = cont['recentAveragePrice']

        embedVar = discord.Embed(title="Snowflake Shutter Shades", color=0x00FFFF)
        embedVar.add_field(name="Rap", value=f'{rapvalue}', inline=True)
        embedVar.add_field(name="Value", value=f'20,000', inline=True)
        embedVar.add_field(name="Demand", value=f'Terrible', inline=True)
        embedVar.add_field(name="Trend", value=f'Stable', inline=True)
        embedVar.add_field(name="Best Price", value=f'{bestprice.prettify().split()[3]}', inline=True)
        embedVar.add_field(name="Copies (Avail/Premium)", value=f'118/23', inline=True)
        embedVar.add_field(name="Comments", value=f'Proof Based #proofs', inline=True)
        embedVar.set_thumbnail(url="https://www.roblox.com/thumbs/asset.ashx?width=420&height=420&assetid=67201161")
        await message.channel.send(embed=embedVar)
        print(rapvalue.split())

    if message.content == '!camo':
        
        page = requests.get("https://www.roblox.com/catalog/1230403652/Camo-Commando")
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all(class_="text-robux-lg wait-for-i18n-format-render")
        bestprice = price[0]
        textstring= "Bestprice: "

        rapstring= "RAP: "
        url = "https://economy.roblox.com/v1/assets/1230403652/resale-data"
        r = requests.get(url)
        cont = r.json()
        rapvalue= str(cont['recentAveragePrice'])
        rapvalueINT = cont['recentAveragePrice']

        embedVar = discord.Embed(title="Camo Commando", color=0x00FFFF)
        embedVar.add_field(name="Rap", value=f'{rapvalue}', inline=True)
        embedVar.add_field(name="Value", value=f'3,000', inline=True)
        embedVar.add_field(name="Demand", value=f'High', inline=True)
        embedVar.add_field(name="Trend", value=f'Fluctuating', inline=True)
        embedVar.add_field(name="Best Price", value=f'{bestprice.prettify().split()[3]}', inline=True)
        embedVar.add_field(name="Copies (Avail/Premium)", value=f'11,720/2,639', inline=True)
        embedVar.set_thumbnail(url="https://www.roblox.com/thumbs/asset.ashx?width=420&height=420&assetid=1230403652")
        await message.channel.send(embed=embedVar)
        print(rapvalue.split())
    
    if message.content == '!black iron':
        
        page = requests.get("https://www.roblox.com/catalog/928908332/Black-Iron-Commando")
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all(class_="text-robux-lg wait-for-i18n-format-render")
        bestprice = price[0]
        textstring= "Bestprice: "

        rapstring= "RAP: "
        url = "https://economy.roblox.com/v1/assets/928908332/resale-data"
        r = requests.get(url)
        cont = r.json()
        rapvalue= str(cont['recentAveragePrice'])
        rapvalueINT = cont['recentAveragePrice']

        embedVar = discord.Embed(title="Black Iron Commando", color=0x00FFFF)
        embedVar.add_field(name="Rap", value=f'{rapvalue}', inline=True)
        embedVar.add_field(name="Value", value=f'3,000', inline=True)
        embedVar.add_field(name="Demand", value=f'Amazing', inline=True)
        embedVar.add_field(name="Trend", value=f'Fluctuating', inline=True)
        embedVar.add_field(name="Best Price", value=f'{bestprice.prettify().split()[3]}', inline=True)
        embedVar.add_field(name="Copies (Avail/Premium)", value=f'54,025/9,510', inline=True)
        embedVar.set_thumbnail(url="https://www.roblox.com/thumbs/asset.ashx?width=420&height=420&assetid=928908332")
        await message.channel.send(embed=embedVar)
        print(rapvalue.split())

    if message.content == '!sinister':

        page = requests.get("https://www.roblox.com/catalog/71484026/Sinister-Branches")
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all(class_="text-robux-lg wait-for-i18n-format-render")
        bestprice = price[0]
        textstring= "Bestprice: "

        rapstring= "RAP: "
        url = "https://economy.roblox.com/v1/assets/71484026/resale-data"
        r = requests.get(url)
        cont = r.json()
        rapvalue= str(cont['recentAveragePrice'])
        rapvalueINT = cont['recentAveragePrice']

        embedVar = discord.Embed(title="Sinister", color=0x00FFFF)
        embedVar.add_field(name="Rap", value=f'{rapvalue}', inline=True)
        embedVar.add_field(name="Value", value=f'2,500', inline=True)
        embedVar.add_field(name="Demand", value=f'Amazing', inline=True)
        embedVar.add_field(name="Trend", value=f'Fluctuating', inline=True)
        embedVar.add_field(name="Best Price", value=f'{bestprice.prettify().split()[3]}', inline=True)
        embedVar.add_field(name="Copies (Avail/Premium)", value=f'71,693/9,874', inline=True)    
        embedVar.set_thumbnail(url="https://www.roblox.com/thumbs/asset.ashx?width=420&height=420&assetid=71484026")
        await message.channel.send(embed=embedVar)
        print(rapvalue.split())

    if message.content == '!winter':

        page = requests.get("https://www.roblox.com/catalog/22587828/Winter")
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all(class_="text-robux-lg wait-for-i18n-format-render")
        bestprice = price[0]
        textstring= "Bestprice: "

        rapstring= "RAP: "
        url = "https://economy.roblox.com/v1/assets/22587828/resale-data"
        r = requests.get(url)
        cont = r.json()
        rapvalue= str(cont['recentAveragePrice'])
        rapvalueINT = cont['recentAveragePrice']

        embedVar = discord.Embed(title="Winter", color=0x00FFFF)
        embedVar.add_field(name="Rap", value=f'{rapvalue}', inline=True)
        embedVar.add_field(name="Value", value=f'10,000', inline=True)
        embedVar.add_field(name="Demand", value=f'Normal', inline=True)
        embedVar.add_field(name="Trend", value=f'Stable', inline=True)
        embedVar.add_field(name="Best Price", value=f'{bestprice.prettify().split()[3]}', inline=True)
        embedVar.add_field(name="Copies (Avail/Premium)", value=f'1,185/147', inline=True)    
        embedVar.set_thumbnail(url="https://www.roblox.com/thumbs/asset.ashx?width=420&height=420&assetid=22587828")
        await message.channel.send(embed=embedVar)
        print(rapvalue.split())

    if message.content == '!scroll':

        page = requests.get("https://www.roblox.com/catalog/125013830/Scroll-of-Sevenless")
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all(class_="text-robux-lg wait-for-i18n-format-render")
        bestprice = price[0]
        textstring= "Bestprice: "

        rapstring= "RAP: "
        url = "https://economy.roblox.com/v1/assets/125013830/resale-data"
        r = requests.get(url)
        cont = r.json()
        rapvalue= str(cont['recentAveragePrice'])
        rapvalueINT = cont['recentAveragePrice']

        embedVar = discord.Embed(title="Scroll of Sevenless", color=0x00FFFF)
        embedVar.add_field(name="Rap", value=f'{rapvalue}', inline=True)
        embedVar.add_field(name="Value", value=f'12,000', inline=True)
        embedVar.add_field(name="Demand", value=f'Low', inline=True)
        embedVar.add_field(name="Trend", value=f"Fluctuating", inline=True)
        embedVar.add_field(name="Best Price", value=f'{bestprice.prettify().split()[3]}', inline=True)
        embedVar.add_field(name="Copies (Avail/Premium)", value=f'571/173', inline=True)    
        embedVar.set_thumbnail(url="https://www.roblox.com/thumbs/asset.ashx?width=420&height=420&assetid=125013830")
        await message.channel.send(embed=embedVar)
        print(rapvalue.split())
    


    arguments = message.content.split()
    if arguments[0] == '!setvalue':
        async def args(arg1, arg2):
            output = ''
            output += f"Changed value of {arg1} to {arg2}"
            await message.channel.send(output)
            
        await args(arguments[1], arguments[2])
        arguments = shlex.split(message.content)   

    arguments = message.content.split()
    if arguments[0] == '!setdemand':
        async def args(arg1, arg2):
            output = ''
            output += f"Changed demand of {arg1} to {arg2}"
            await message.channel.send(output)

        await args(arguments[1], arguments[2])
        arguments = shlex.split(message.content)    

    arguments = message.content.split()
    if arguments[0] == '!settrend':
        async def args(arg1, arg2):
            output = ''
            output += f"Changed trend of {arg1} to {arg2}"
            await message.channel.send(output)

        await args(arguments[1], arguments[2])
        arguments = shlex.split(message.content)    



client.run(TOKEN) 
