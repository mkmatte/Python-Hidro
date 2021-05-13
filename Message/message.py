import json
import requests
from time import sleep
from threading import Thread, Lock

# token='1847502844:AAFX6i9t5g0Gdv3NQfeqyFR6xf1YKruHic0'
#
# global CONFIG
# config = {'url': 'https://api.telegram.org/bot1847502844:AAFX6i9t5g0Gdv3NQfeqyFR6xf1YKruHic0/', 'lock': Lock()}

def del_update(data):
    global CONFIG
    print('Deletando Mensagem id: ' + str(data['update_id']))
    CONFIG['lock'].acquire()
    requests.post(CONFIG['url'] + 'getUpdates',{'offset':data['update_id']+1})
    CONFIG['lock'].release()



def telegram_message(msg):
    token='1847502844:AAFX6i9t5g0Gdv3NQfeqyFR6xf1YKruHic0'
    group_id= '-552068730'
    CONFIG = {'url': 'https://api.telegram.org/bot1847502844:AAFX6i9t5g0Gdv3NQfeqyFR6xf1YKruHic0/'}
    url = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+group_id+'&text='+msg
    requests.post(url)







# while True:
#     while True:
#         try:
#             x = json.loads(requests.get(CONFIG['url'] + 'getUpdates').text)
#
#         except  Exception as e:
#             x = {'result':[]}
#             if 'Failed to established a new connection' in str(e):
#                 print("Perca de conexão")
#             else:
#                 print('Erro desconhecido:' + str(e))
#
#     if len(x['result'])>0:
#         for data in x['result']:
#             Thread(target=del_update, args=(data,)).start()
#             print(json.dumps(data))
#         sleep(1.5)
