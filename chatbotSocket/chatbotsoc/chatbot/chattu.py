import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
'''
chatbot = ChatBot("Rog")
chatterbot.trainers.UbuntuCorpusTrainer(storage, **kwargs)
'''
'''
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    '''
bot = ChatBot(
    'Rog',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='F:\Projects\chatbotSocket\chatbotsoc\chatbot_tutorial/database.sqlite3'
)
#from chatterbot.trainers import ListTrainer

bot.set_trainer(ChatterBotCorpusTrainer)
#bot.train("chatterbot.corpus.english")
bot.train("C:\Users\AK24ALIVE\Desktop\Deeper\df\ubuntu_dialogs.tar")
#response = bot.get_response("Fuck off")
#print(response)