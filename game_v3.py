"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def game_core_v3(number):
    
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его 
        в зависимости от того, больше оно или меньше нужного.
        Функция принимает загаданное число и возвращает число попыток'''   
    
    count = 0
    low_num = 1    # минимальное значение из диапазона
    high_num = 100    # максимальное значение из диапазона
    predict = np.random.randint(1,101) # предполагаемое число
    
    while number != predict:
        count+=1
        if number > predict: 
            low_num = predict + 1
            '''Если загаданное число больше предполагаемого, устанавливаем минимальное значение на единицу больше'''
        elif number < predict: 
            '''Если загаданное число меньше предполагаемого, устанавливаем его в качестве максимального значения'''
            high_num = predict
        predict = (low_num+high_num) // 2 
        '''Предполагаемое число приравниваем к среднему значению между максимальным и минимальным'''
    return(count) # выход из цикла, если угадали

game_core_v3(98)
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)