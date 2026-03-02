import os, asyncio, yt_dlp
from aiogram import Bot, Dispatcher, types, F

TOKEN = '8727207372:AAHRKRCwGN_BXnWs4NExcOh8bn5JadRUjE8'
bot = Bot(token=TOKEN)
dp = Dispatcher()

def dl(url):
    opts = {'format': 'best', 'outtmpl': 'v.mp4', 'noplaylist': True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
    return 'v.mp4'

@dp.message(F.text.contains('http'))
async def h(m: types.Message):
    w = await m.answer('Yuklanmoqda...')
    try:
        f = dl(m.text)
        await m.answer_video(types.FSInputFile(f))
        os.remove(f)
    except:
        await m.answer('Xato!')
    finally:
        await w.delete()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
  
