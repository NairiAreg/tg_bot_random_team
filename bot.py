import telebot
import random
import math


bot = telebot.TeleBot('5160133360:AAFAbx1b_zQN7x5HfsDQez0cAuDRWeR1ANM')

@bot.message_handler()
def start(message):
    arr = message.text.split()
    str = ''

    lowerArr = list(map(lambda x: x.lower(),arr))

    if 'nairi' in lowerArr and 'iren' in lowerArr:
        str = "Nairi - Iren\n" if random.random() > 0.5 else "Iren - Nairi\n"

        arr = list(filter(lambda x:x.lower()!='nairi' and x.lower()!='iren', arr))

    forLength = math.floor(len(arr) / 2)
    for x in range(forLength):
        if random.random() > 0.5:
            str += arr.pop(math.floor(random.random() * (len(arr) - 1))) + ' - ' + arr.pop(math.floor(random.random() * (len(arr) - 1))) + '\n'
        else:
            str = arr.pop(math.floor(random.random() * (len(arr) - 1))) + ' - ' + arr.pop(math.floor(random.random() * (len(arr) - 1))) + '\n' + str
    # print(str)

    bot.send_message(message.chat.id, "<b>The Team Is</b> \n"+str, parse_mode='html')

bot.polling(non_stop=True)