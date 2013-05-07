
class DefaultAction:
    action1 = 0
    action2 = 0
    action3 = 0
    def New_action(main, new_action1, new_action2, new_action3, new_action4):
        main.new_action1 = new_action1
        main.new_action2 = new_action2
        main.new_action3 = new_action3
#Вывод на экран меню и выбор пункта
print('''Выбор:
        1 - Играть в компютер
        2 - Заняться учебой
        3 - Отправиться гулять
        4 - Любое другое действие.''')
Your_action = ""
while (Your_action == ""):
    Your_action = input()
    try: Your_action = int(Your_action )
    except ValueError:
            print("Пожалуйста, введите число.")
            Your_action = ""
            continue
    if (Your_action < 1 or Your_action > 4):
        Your_action = ""
        print("Введенное число должно лежать в интервале [1; 4] в соответствии количеством пунктов меню.")
#Вывод на экран и выбор соответствующего подраздела
if Your_action == 1:
    class  GameAction(DefaultAction):
        print('''Выбор:
        1 - Counter Strike
        2 - Starcraft
        3 - Diablo III''')
    Your_actiongame1 = input()
    Your_actiongame1 = int(Your_actiongame1 )
    if Your_actiongame1 == 1:
        class Ingame1Action1(GameAction):
            print('''Выбор:
        1 - Террористы
        2 - Контр-террористы
        3 - Наблюдение
        4 - Выход''')
        your_game1_action1 = input()
        your_game1_action1 = int(your_game1_action1)
        if your_game1_action1 == 1:
            print('Ты выбрал сторону Террористов, удачных плэнтов тебе:D')
        elif your_game1_action1 == 2:
            print('Ты выбрал сторону Контр-террористов, Легкого овобождения заложников тебе:D')
        elif your_game1_action1 == 3:
            print('Ты выбрал режим наблюдения, удачного просмотра.')
        elif your_game1_action1 == 4:
            print ('GL HF')
    elif Your_actiongame1 == 2:
        class Ingame2Action2(GameAction):
            print('''Выбор:
        1 - Зерги
        2 - Протосы
        3 - Терраны
        4 - Наблюдение''')
        your_game2_action2 = input()
        your_game2_action2 = int(your_game2_action2)
        if your_game2_action2 == 1:
            print('Ты выбрал сторону Зергов, удачного пуша тебе:D')
        elif your_game2_action2 == 2:
            print('Ты выбрал сторону Протосов, дарк тамплиеры дисбаланс:D ')
        elif your_game2_action2 == 3:
            print('Ты выбрал режим наблюдения, строй больше пехотинцев,побеждай!:D.')
        elif your_game2_action2 == 4:
            print ('GL HF')
    elif Your_actiongame1 == 3:
        class Ingame3Action3(GameAction):
            print('''Выбор:
        1 - Барбариан
        2 - Сорка
        3 - Вд
        4 - ДХ
        5 - Монк
        6 - Выход''')
        your_game3_action3 = input()
        your_game3_action3 = int(your_game3_action3)
        if your_game3_action3 == 1:
            print('Ты выбрал Варвара, удачного дропа тебе:D')
        elif your_game3_action3 == 2:
            print('Ты выбрал Мага, удачного дропа тебе:D ')
        elif your_game3_action3 == 3:
            print('Ты выбрал режим Колдун, судачного дропа тебе:D.')
        elif your_game3_action3 == 4:
            print ('Ты выбрал режим Охотника на демонов,удачного дропа тебе:D')
        elif your_game3_action3 == 5:
            print ('Ты выбрал режим Монаха,удачного дропа тебе:D')
        elif your_game3_action3 == 6:
            print ('GL HF')
elif Your_action == 2:
    class  UniversityAction(DefaultAction):
        print('''Выбор:
        1 - Математика
        2 - Физика
        3 - Основы программирования''')
    Your_actiongame1 = input()
    Your_actiongame1 = int(Your_actiongame1)
    if Your_actiongame1 == 1:
        class Ingame1Action1():
            print('''Выбор:
        1 - Домашняя работа
        2 - Курсовая работа
        3 - Типовик
        4 - Уснуть выбирав тип работы''')
        your_game1_action1 = input()
        your_game1_action1 = int(your_game1_action1)
        if your_game1_action1 == 1:
            print('Задание :sqrt(25)+sqrt(36) =')
        elif your_game1_action1 == 2:
            print('Задание :Расчитать массу луны, если козырь пики')
        elif your_game1_action1 == 3:
            print('Задание :sqrt99999999 =')
        elif your_game1_action1 == 4:
            print ('zzzzzzzzzzz')
    elif Your_actiongame1 == 2:
        class Ingame2Action2(UniversityAction):
            print('''Выбор:
        1 - Домашняя работа
        2 - Курсовая работа
        3 - Типовик
        4 - Уснуть выбирав тип работы''')
        your_game2_action2 = input()
        your_game2_action2 = int(your_game2_action2)
        if your_game2_action2 == 1:
            print('Задание: скорость велосипеда 10км/ч,какова скорость человека на велосипеде относительно велосипеда?  ')
        elif your_game2_action2 == 2:
            print('Задание :Расчитать массу луны, если козырь крести')
        elif your_game2_action2 == 3:
            print('Задание : Человек весит 100кг какое давление он оказывает на пол')
        elif your_game2_action2 == 4:
            print ('zzzzzzzzzzz')
    elif Your_actiongame1 == 3:
        class Ingame3Action3(UniversityAction):
            print('''Выбор:
        1 - Домашняя работа
        2 - Курсовая работа
        3 - Типовик
        4 - Уснуть выбирав тип работы''')
        your_game3_action3 = input()
        your_game3_action3 = int(your_game3_action3)
        if your_game3_action3 == 1:
            print('Напиши программу показывающую что ты твое знание классов')
        elif your_game3_action3 == 2:
            print('Напиши программу показывающую что ты достоин работать в Google ')
        elif your_game3_action3 == 3:
            print('А его нет,:D')
        elif your_game3_action3 == 4:
            print ('Программист не спит, он находится в режиме ожидания')
elif Your_action == 3:
    class  OtherAction(DefaultAction):
        print('''Выбор:
        1 - Пойти гулять с друзьями
        2 - Пойти гулять с девушкой
        3 - FOREVE ALONE''')
    Your_actiongame1 = input()
    Your_actiongame1 = int(Your_actiongame1)
    if Your_actiongame1 == 1:
        class Ingame1Action1(OtherAction):
            print('''Выбор:
        1 - Пойти с друзьями в бар
        2 - Позависать на улице
        3 - Пойти на халяву в кино''')
        your_game1_action1 = input()
        your_game1_action1 = int(your_game1_action1)
        if your_game1_action1 == 1:
            print('На утро ваш кошелк пуст,ну и голова в принципе тоже')
        elif your_game1_action1 == 2:
            print('На улице было холодно и ты заболел,Неудачник')
        elif your_game1_action1 == 3:
            print('Лучшее кино - Халявное кино')
    elif Your_actiongame1 == 2:
        class Ingame2Action2(OtherAction):
            print('''Выбор:
        1 - Пойти в кафе
        2 - Пойти в кино
        3 - Погулять в парке''')
        your_game2_action2 = input()
        your_game2_action2 = int(your_game2_action2)
        if your_game2_action2 == 1:
            print('Девушка затащила вас в суши бар и накормила ролами,будь доволен,платить то тебе:D')
        elif your_game2_action2 == 2:
            print('Ну задний ряд,все дела')
        elif your_game2_action2 == 3:
            print('Дождь на улице какой парк?')
    elif Your_actiongame1 == 3:
        class Ingame3Action3(OtherAction):
            print('''Такое тоже бывает:D''')
elif Your_action == 4:
    print ('''Тут ты можешь выбрать себе занятие сам''')
    class OtherAction(DefaultAction):
        print ('Напиши чем ты хочешь заняться?:')
        your1_action = input()
        print ('Сегодня ты займешься',your1_action)

    
print ('Удачи!')
