RU
Этот бот позволяет отослеживать криптоактивы. Бот работает только для определенного пользователя чей user id указан в скрипте.
Программа состоит из Excel таблицы и скрипта.

Инструкция по работе
ТАБЛИЦА
valuesk.xlsx - таблица с вашими активами. 

Описание колонок таблицы: 
currency - тикер валюты (BTC, ETH, ETC и тд.)
values - количество актива 
price$ - стоимость актива на момент покупки


!ВНИМАНИЕ: в сторке "Валюта" указывается валюта в которой производтся расчет, если валюта в скрипте и в таблице будет отличаться то возникнет ошибка в расчетах итоговой суммы.

СКРИПТ 
Скрипт написан на языке программирования Python (v. 3.11) с использованием библиотеки aiogram (v. 2.25.1). Все необходимые библиотеки нужно установить из requirements.txt.
API_TOKEN - необходимо указать токен вашего бота
message.from_user.id - ваш user id
ticker = "USD" - тикер валюты (можно менять)
await asyncio.sleep(60) - в скобках выставляете промежуток времени через который будут приходить уведомления


EN
This bot allows you to track crypto assets. The bot only works for a specific user whose user id is specified in the script.
The program consists of an Excel spreadsheet and a script.

Work instructions
table
valuesk.xlsx is a table with your assets.

Description of the columns of the table:
currency - currency ticker (BTC, ETH, ETC., etc.)
values - the amount of the asset
price$ - the value of the asset at the time of purchase


!ATTENTION: the "Currency" column indicates the currency in which the calculation is performed, if the currency in the script and in the table is different, then an error will occur in calculating the total amount.

THE SCRIPT
The script is written in the Python programming language (v. 3.11) using the aiogram library (v. 2.25.1). All necessary libraries need to be installed from requirements.txt.
API_TOKEN - you need to specify your bot's token
message.from_user.id - your user id
ticker = "USD" - currency ticker (can be changed)
await asyncio.sleep(60) - set the time interval in parentheses after which notifications will be received