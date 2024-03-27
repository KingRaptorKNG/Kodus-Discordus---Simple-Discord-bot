import discord
from discord.ext import commands
import random
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def coin(ctx):
    coin = random.randint(0,1)
    if coin == 1:
        await ctx.send('Орёл!')
    else:
        await ctx.send('Решка!')

@bot.command()
async def timer(ctx, how_much = 5, timer = False):
    await ctx.send('Запущен таймер!')
    try:
        if how_much < 0:
            for i in range(how_much, 0+1, 1):
                if timer is True:
                    await ctx.send(i)
                time.sleep(1)
        elif how_much >= 0:
            for i in range(1, how_much+1):
                if timer is True:
                    await ctx.send(i)
                time.sleep(1)
        await ctx.send('Время вышло!')
    except ValueError:
        await ctx.send('Данные введены неверно!')

@bot.command()
async def number(ctx, random_from=0, random_to=0):
    if random_from == 0 and random_to == 0:
        await ctx.send('Число не выбрано!')
    else:
        if random_from > random_to:
            await ctx.send('Число от больше числа до!')
        elif random_from == random_to:
            await ctx.send('Числа равны!')
        else:
            random_int = random.randint(int(random_from), int(random_to))
            await ctx.send(random_int)


@bot.command()
async def clear(ctx, clear_much=0):
    await ctx.send('Начинаю очистку чата!')
    time.sleep(5)
    if clear_much == 0:
        await ctx.send('Не выбрано сколько строк очищать!')
    else:
        for clearing in range(clear_much):
            await ctx.send('** **')
            time.sleep(1)



@bot.command()
async def commands(ctx):
    await ctx.send('Пока что я могу выполнить эти команды:')
    time.sleep(1)
    await ctx.send('coin - подбрасываю монетку;')
    time.sleep(1)
    await ctx.send('timer [сколько] [показывать время] - [сколько] - на сколько секунд засекаю таймер - [показывать время] False/True - писать ли время по секундам;')
    time.sleep(1)
    await ctx.send('heh [число] - пишу heh [число] раз;')
    time.sleep(1)
    await ctx.send('commands - расписываю команды;')
    time.sleep(1)
    await ctx.send('hello - скажу привет и представлюсь;')
    time.sleep(1)
    await ctx.send('number [от] [до] - выбираю случайное число от [от] до [до];')
    time.sleep(1)
    await ctx.send('clear [сколько] - заполняю [сколько] строк пустыми сообщениями.')
