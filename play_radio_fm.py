import vlc
import os
def play_radio(url, name_radio):
    p = vlc.MediaPlayer(url)
    p.play()
    while True:
        n = input(">> ")
        if n == '/stop':
            p.stop()
        elif n == '/play':
            p.play()
        elif n == '/clear':
            os.system('cls')
        elif n == '/exit':
            p.stop()
            break
        elif n == '/now_radio':
            print(f'Сейчас играет {name_radio}')
        elif n == '/help':
            print('/play - озабновить радиопоток\n/stop - остановить радио вещание с возможностью возабнавления\n/clear - отчистить консоль(только для windows)\n/now_radio - узнать какая радиостанция играет\n/exit - выйти из приложения')    
        else:
            print('Erorr command')
