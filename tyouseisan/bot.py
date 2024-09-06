import discord
from discord.ext import tasks
import datetime
import pytz
from .scraper import get_data
import os
from dotenv import load_dotenv


def main():
    env_path = os.path.join(os.path.dirname(__file__), "../.env")
    load_dotenv(env_path)
    bot = discord.Bot()

    @tasks.loop(seconds=60)
    async  def loop():
        now = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))
        if now.hour != 12 or now.minute != 0:
            return
        data = get_data()
        hutsukago = now + datetime.timedelta(days=2)
        date = f"{hutsukago.month}/{hutsukago.day}"
        print(data.get(date))
        
        if data.get(date) and data.get(date)["ok"] >= 3:
            print('I am working')
            await bot.wait_until_ready()
            channel = bot.get_channel(1278282497188429824)
            
            mention = ""
            for member in data.get(date)["mention"]:
                mention += f"@{member} "

            text = f'【活動日の確認】\n 明後日{date}は活動日です！ \n  {mention} {date}の活動に確実に来れる場合は🆗 を、そうでない場合は❌ をリアクションしてください。\n (その他の方で活動に参加可能になった方も🆗 にリアクションをお願いします。なお、ここにリアクションしなかったからと言って参加できないわけではありません。) \n 本日 18:00時点で来れる人が2人以下になった場合は活動が取りやめになります。'
            await channel.send(text)
            
    loop.start()

    bot.run(os.getenv("DISCORD_TOKEN"))