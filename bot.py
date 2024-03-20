import discord
import random
import time

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привилегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привилегии
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('Пингани всех'):
        await message.channel.send('@everyone')
    elif message.content.startswith('Рандом'):
        await message.channel.send(random.randint(1, 100))
    elif message.content.startswith('Поспи 10 сек'):
        time.sleep(10)
        await message.channel.send('**проснулся**')
    elif message.content.startswith('Таймер'):
        for timer in range(1, 11):
            await message.channel.send(timer)
            time.sleep(1)
    elif message.content.startswith('$Потревожь @'):
        for i in range(3):
            await message.channel.send(message.content - '$потревожь')
    else:
        time.sleep(1)
        await message.channel.send(message.content)
