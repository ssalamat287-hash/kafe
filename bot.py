import telebot
from telebot import types

# Bot tokenin ózgertirmey qoyıw ushın ózińizdiń tokenińizdi jazasız:
TOKEN = "8838436380:AAGCHrR5G3nnkJcJC57vMPF7PmWbrnS1_LE"
bot = telebot.TeleBot(TOKEN)


# /start buyruǵı
@bot.message_handler(commands=['start'])
def send_welcome(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton('📋 Menyusi')
  btn2 = types.KeyboardButton('📞 Baylanıs / Manzil')
  markup.add(btn1, btn2)

  bot.send_message(
      message.chat.id,
      f"Assalawma aleykum, {message.from_user.first_name}! "
      "«Ush Qazan» kafesiniń rásmiy botına xosh kelipsiz. "
      "Tómendegi túymeler arqalı menyu menen tanısın:",
      reply_markup=markup,
  )


# Túymelerdi basqanda
@bot.message_handler(func=lambda message: True)
def handle_message(message):
  if message.text == '📋 Menyusi':
    markup = types.InlineKeyboardMarkup()
    btn_palaw = types.InlineKeyboardButton(
        '🍲 Palawlar hám Djiiz', callback_data='palaw'
    )
    btn_shashlik = types.InlineKeyboardButton(
        ' skewers Shashlıqlar', callback_data='shashlik'
    )
    btn_salat = types.InlineKeyboardButton('🥗 Salatları', callback_data='salat')
    btn_drink = types.InlineKeyboardButton(
        '🥤 Suwsinler', callback_data='drink'
    )
    markup.add(btn_palaw, btn_shashlik)
    markup.add(btn_salat, btn_drink)

    bot.send_message(
        message.chat.id,
        'Kategoriyalardan birewin tańlań:',
        reply_markup=markup,
    )

  elif message.text == '📞 Baylanıs / Manzil':
    bot.send_message(
        message.chat.id,
        '📍 Manzilimiz: Nókis qalası\n📞 Tel: +998 (XX) XXX-XX-XX\n\n'
        'Xizmet kórsetiw: 0%',
    )


# Inline túymelerdi isletiw
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  if call.data == 'palaw':
    text = (
        '🍲 **PALAWLAR HÁM DJIIZ:**\n\n'
        '• Djiiz 0.5kg — 110 000 sum\n'
        '• Djiiz 1kg — 220 000 sum\n'
        '• Tashkent palawı (komplekt) — 43 000 sum\n'
        '• Samarqand palawı (komplekt) — 48 000 sum\n'
        '• Uyǵur lag'man — 30 000 sum\n'
        '• Shorpa — 30 000 sum'
    )
    bot.send_message(call.message.chat.id, text, parse_mode='Markdown')

  elif call.data == 'shashlik':
    text = (
        '🍢 **SHASHLıQLAR:**\n\n'
        '• Shashlıq farsh — 12 000 sum\n'
        '• Shashlıq utka — 18 000 sum\n'
        '• Balık shashlıq — 20 000 sum\n'
        '• Shashlıq kuskovoy — 22 000 sum\n'
        '• Shashlıq okorochka — 24 000 sum\n'
        '• Shashlıq baranina — 24 000 sum\n'
        '• Shashlıq asorti (2 person) — 80 000 sum'
    )
    bot.send_message(call.message.chat.id, text, parse_mode='Markdown')

  elif call.data == 'salat':
    text = (
        '🥗 **SALATLAR:**\n\n'
        '• Suzbe — 8 000 sum\n'
        '• Chimchi — 10 000 sum\n'
        '• Svejiy salat — 12 000 sum\n'
        '• Okroshka — 10 000 sum\n'
        '• Achik-chuchuk — 14 000 sum\n'
        '• Sezar salat — 35 000 sum\n'
        '• Miasnoy asorti — 120 000 sum'
    )
    bot.send_message(call.message.chat.id, text, parse_mode='Markdown')

  elif call.data == 'drink':
    text = (
        '🥤 **SUWSINLER:**\n\n'
        '• Nan 0.5 / Nan — 3 000 / 6 000 sum\n'
        '• Chay — 5 000 sum\n'
        '• Chay limon menen — 10 000 sum\n'
        '• Mohito — 20 000 / 45 000 sum\n'
        '• Ayran — 8 000 / 24 000 sum\n'
        '• Coca-Cola / Fanta 1.5L — 19 000 sum\n'
        '• Sok — 15 000 sum'
    )
    bot.send_message(call.message.chat.id, text, parse_mode='Markdown')


# Botdı toqtawsız isletiw
bot.infinity_polling()
