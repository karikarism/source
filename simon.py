# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークン
TOKEN = ODE3Mzc3NTY0NzQ5NzI1NzA3.YEIoLQ.EsSok43zfjcDngsaHJ8q5nnC6LY

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'おやすみ':
        await message.channel.send('おやすみなさいもん☆')

client.run(TOKEN)
