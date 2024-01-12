import requests
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types, asyncio
import pandas as pd

API_TOKEN = 'token'  # указать свой токен бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def with_puree(message: types.Message):
    if message.from_user.id == 1234567890:  # указать свой user.id
        while True:
            count, count2, a = 0, 0, 0
            df_orders = pd.read_excel('valuesk.xlsx')  # valuesk.xlsx - файл с данными
            ticker = "USD"  # можно указать свою валюту (RUB, EUR, TRY)

            def request(currency, values, priced):
                response = requests.get(f'https://api.coinbase.com/v2/prices/{currency}-{ticker}/spot')
                try:
                    counts = 0
                    btc = response.json()
                    currency = btc['data']['base']
                    price = btc['data']['amount']
                    counts += round(float(price) * values, 2)
                    return [f"Криптовалюта: {currency}  "
                            f"|  Цена: {round(float(price), 2)} {ticker}  "
                            f"|  В активе: {round(float(price) * values, 2)} {ticker}  "
                            f"|  Прибыль: {round(((float(price) - float(priced)) / float(priced)) * 100, 2)}%", counts]
                except KeyError:
                    return f"Возникла ошибка! курс {currency} к {ticker} не найден."

            lines = df_orders.shape[0]
            current_time = datetime.now()
            txt = (f"{current_time.hour:02d}:{current_time.minute:02d} {current_time.day:02d}."
                   f"{current_time.month:02d}.{current_time.year:04d}\n")
            while lines > 0:
                r = request(df_orders.iloc[a, 0], df_orders.iloc[a, 1], df_orders.iloc[a, 2])
                txt += r[0] + "\n\n"
                count += r[1]
                count2 += df_orders.iloc[a, 2] * df_orders.iloc[a, 1]
                a += 1
                lines -= 1

            ms = (f'Стоимость всех автивов: {round(count, 2)} {ticker} '
                  f'Вложено: {round(count2, 2)} {ticker} '
                  f'Прибыль: {round(((float(count) - float(count2)) / float(count2)) * 100, 2)}%')

            msg = await message.answer(txt + ms)
            await asyncio.sleep(60)  # время через которое будут отправляться сводки (сек)
            await msg.delete()  # удаление отправленного сообщения


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
