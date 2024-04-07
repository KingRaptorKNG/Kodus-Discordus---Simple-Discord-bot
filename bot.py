import discord
from discord.ext import commands
import random
import time
import os
import requests
print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
client = discord.Client(intents=intents)

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


def get_fox_image_url():
    image = 'https://randomfox.ca/floof/'
    res = requests.get(image)
    data = res.json()
    return data['image']


@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.event
async def on_message(message):
        if message.content.startswith('$challenge'):
            start = True
            await message.channel.send('Вы готовы начать челлендж: Кто больше соберёт пластика?')
            while start:
                time.sleep(1)
                user_response = await bot.wait_for('message', timeout=10)
                if user_response.content == 'yes' or user_response.content == 'Yes':
                    await message.channel.send('Челлендж начинается!')
                    time.sleep(1)
                    await message.channel.send('Ваша задача отправлять + если вы собрали пластик!')
                    time.sleep(1)
                    await message.channel.send('Игрок 1 отправьте + если готовы или - чтобы закончить')
                    time.sleep(1)
                    user_response = await bot.wait_for('message')
                    if user_response.content == '+':
                        player1 = message.author
                        count1 = 0
                    else:
                        start = False
                        continue
                    time.sleep(1)
                    await message.channel.send('Игрок 2 отправьте + если готовы или - чтобы закончить')
                    time.sleep(1)
                    user_response = await bot.wait_for('message')
                    if user_response.content == '+':
                        player2 = message.author
                        count2 = 0
                    else:
                        start = False
                        continue
                    await message.channel.send('Начинаем! Отправляйте плюсы когда собрали пластик!')
                    time.sleep(3)
                    end = True
                    while end:
                        user_response = await bot.wait_for('message')
                        time.sleep(1)
                        if user_response.content == '+' and message.author == player1:
                            await message.channel.send('Игрок 1 получил очко! score - просмотр очков!')
                            count1 += 1
                        if user_response.content == '+' and message.author == player2:
                            await message.channel.send('Игрок 2 получил очко! score - просмотр очков!')
                            count2 += 1
                        if user_response.content == 'score':
                            player1_score1 = 'Очки Игрока 1 = ', count1, '!'
                            player1_score2 = 'Очки Игрока 2 = ', count2, '!'
                            await message.channel.send(player1_score1)
                            time.sleep(1)
                            await message.channel.send(player1_score2)
                        if user_response.content == '-':
                            end = False
                            continue
                    else:
                        start = False
                elif user_response.content == 'no':
                    start = False

            else:
                await message.channel.send('Челлендж завершён.')
        await bot.process_commands(message)




@bot.command()
async def timer(ctx, how_much = 5, timer = False):
    await ctx.send('Запущен таймер!')
    how_much = int(how_much)
    timer = bool(timer)
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
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    if 'uncommon' in img_name:
        img_name = random.choice(os.listdir('images'))
        if 'uncommon' in img_name:
            with open(f'images/{img_name}', 'rb') as f:
                picture = discord.File(f)
            await ctx.send('Вам попался необычный мем!')
            time.sleep(1)
            await ctx.send(file=picture)
    elif 'rare' in img_name:
        img_name = random.choice(os.listdir('images'))
        if 'rare' in img_name:
            img_name = random.choice(os.listdir('images'))
            if 'rare' in img_name:
                with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
                await ctx.send('Вам попался редкий мем!')
                time.sleep(1)
                await ctx.send(file=picture)
    else:
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send('Вам попался обычный мем!')
        time.sleep(1)
        await ctx.send(file=picture)

@bot.command()
async def commands(ctx):
    await ctx.send('Пока что я могу выполнить эти команды:')
    time.sleep(1)
    await ctx.send('$ - префикс;')
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
    await ctx.send('clear [сколько] - заполняю [сколько] строк пустыми сообщениями;')
    time.sleep(1)
    await ctx.send('fox - отправляю рандомное изображение лисы;')
    time.sleep(1)
    await ctx.send('duck - отправляю рандомное изображение утки;')
    time.sleep(1)
    await ctx.send('mem - отправляю рандомный мем;')
    time.sleep(1)
    await ctx.send('challenge - челлендж по сбору пластика.')

bot.run("")
