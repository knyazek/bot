import telebot
from telebot import types
import random

# Ваш API-ключ токена
API_TOKEN = 'Вставь_свой_токен'

# Создание экземпляра бота
bot = telebot.TeleBot(token=API_TOKEN)

# Списки блюд для каждой категории
breakfast_menu = ["Омлет", "Мюсли", "Тосты", "Яичница", "Гранола"]
lunch_menu = ["Салат", "Сэндвич", "Пицца", "Суп", "Бургер"]
dinner_menu = ["Стеак", "Лазанья", "Суши", "Карри", "Рыба с картофельным пюре"]

# Обработчик команды /start и создание кнопок
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_breakfast = types.KeyboardButton("Завтрак")
    item_lunch = types.KeyboardButton("Обед")
    item_dinner = types.KeyboardButton("Ужин")
    markup.add(item_breakfast, item_lunch, item_dinner)

    bot.send_message(message.chat.id, "Привет! Я могу помочь вам выбрать, что поесть. Выберите один из вариантов ниже.", reply_markup=markup)

# Обработчики кнопок и рандомизация блюд
@bot.message_handler(func=lambda message: message.text == "Завтрак")
def recommend_breakfast(message):
    recommended_dish = random.choice(breakfast_menu)
    bot.send_message(message.chat.id, f"Я рекомендую вам на завтрак: {recommended_dish}")

@bot.message_handler(func=lambda message: message.text == "Обед")
def recommend_lunch(message):
    recommended_dish = random.choice(lunch_menu)
    bot.send_message(message.chat.id, f"Я рекомендую вам на обед: {recommended_dish}")

@bot.message_handler(func=lambda message: message.text == "Ужин")
def recommend_dinner(message):
    recommended_dish = random.choice(dinner_menu)
    bot.send_message(message.chat.id, f"Я рекомендую вам на ужин: {recommended_dish}")

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
