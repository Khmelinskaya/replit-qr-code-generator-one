import qrcodeT

# Заполните переменные ниже
name = "дочь твоя, любимая" # Введите свое имя между кавычек
telegram_account = "maevia_inclemens" # Введи между кавычек свой аккаунт в Telegram

application_msg = f"Привет, я {name} прошу добавить меня в Кодильню, мой телеграмм http://t.me/{telegram_account}"
qrcodeT.qrcodeT(application_msg)
