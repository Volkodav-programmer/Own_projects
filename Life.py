<<<<<<< HEAD
class Life:

    def __init__(self, name, satiety=100, happiness=100, health=100, money=10000000, total_days=0):
        self.name=name
        self.satiety=satiety
        self.happiness=happiness
        self.health=health
        self.money=money
        self.total_days=total_days

    def pass_day(self):
        self.satiety-=15
        self.happiness-=10
        self.health-=10
        #self.money+=sallary
        self.total_days+=1

    def apartment(self):
        print \
        ("""
        Выберите, какое жилье вы хотите приобрести: 
    
        0 - Выйти
        1 - Палатка (500)
        2 - Общежитие (1000/месяц)
        3 - Парковочное место (700/месяц)
        4 - Снять комнату (1500/месяц)
        5 - Снять квартиру (2000/месяц)
        6 - Купить квартиру (35 000)
        7 - Частный дом за городом (85 000)
        8 - Огромный особняк за городом (150 000)
        9 - Пентхаус (1 000 0000)
        """)
    
        choice = int(input("Ваш выбор: "))
        while choice!=0:

            if choice==0:
                break

            elif choice==1:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>500:
                        self.apartments='Палатка'
                        self.money-=500
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        break
                else:
                    break

            elif choice==2:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>1000:
                        self.apartments='Общежитие'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        #while apartments=='Общежитие':
                            #if total_days%30==0:
                        self.money-=1000
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        break
                        
                else:
                    break

            elif choice==3:
                if self.car!='':
                    print \
                    ("""
                    Вы уверены?
                    1 - Да
                    2 - Нет 
                    """)
                    choice1=int(input())
                    if choice1==1:
                        if self.money>700:
                            self.apartments='Парковочное место'
                            print('Теперь', self.apartments, "является вашим местом жительства")
                            #while apartments=='Парковочное место':
                                #if total_days%30==0:
                            self.money-=700
                            self.pass_day()
                        else:
                            print('У вас недостаточно денег')
                            break
                    else:
                        break
                else:
                    print('Для начала купите машину')
                    break

            elif choice==4:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>1500:
                        self.apartments='Съёмная комната'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        #while apartments=='Съёмная комната':
                            #if total_days%30==0:
                        self.money-=1500
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        choice=0

                else:
                    choice=0

            elif choice==5:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>2000:
                        self.apartments='Съёмная квартира'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        #while apartments=='Съёмная квартира':
                            #if total_days%30==0:
                        self.money-=2000
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        choice=0

                else:
                    choice=0

            elif choice==6:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>35000:
                        self.apartments='Квартира'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        self.money-=35000
                        self.pass_day()
                    else:
                        print('У вас недостаточно денег')
                        choice==0
                        break
                else:
                    choice=0

            elif choice==7:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>85000:
                        self.apartments="Дом за городом"
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        self.money-=85000
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        choice=0
                else:
                    choice=0

            elif choice==8:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>150000:
                        self.apartments='Особняк'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        self.money-=150000
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        choice=0
                else:
                    choice=0

            elif choice==9:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>1000000:
                        self.apartments='Пентхаус'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        self.money-=1000000
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        choice=0
                else:
                    choice=0

            else:
                print('В меню нет пункта', choice)
                break
    
    def eat(self):
        print \
        (""" 
        Выберите, что будете есть:
        0 - В меню
        1 - Еда с мусорки
        2 - Дешевый фаст фуд (75)
        3 - Дешевое кафе (140)
        4 - Полноценный приём пищи в кафе (200)
        5 - Закупить продукты (1000)
        6 - Ресторан (1700)
        """)
        choice=int(input())

        while choice!=0:
        
            if choice==0:
                break

            elif choice==1:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                for i in range(count):
                    self.satiety+=10*count
                    self.health-=8*count
                    self.happiness-=5*count
                    if self.happiness>500:
                        self.happiness=500
                    if self.health>500:
                        self.health=500
                    if self.satiety>500:
                        self.satiety=500
                    self.pass_day()
                break

            elif choice==2:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>75*count:
                    for i in range(count):
                        self.satiety+=20*count
                        self.health-=10*count
                        self.money-=75*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

            elif choice==3:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>140*count:
                    for i in range(count):
                        self.satiety+=45*count
                        self.health-=10*count
                        self.money-=140*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break


            elif choice==4:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>200*count:
                    for i in range(count):
                        self.satiety+=65*count
                        self.money-=200*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

            elif choice==5:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>1000*count:
                    for i in range(count):
                        self.satiety+=45*count
                        self.health+=5*count
                        self.happiness+=5*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break
        
            elif choice==6:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>75*count:
                    for i in range(count):
                        self.satiety+=150*count
                        self.health+=30*count
                        self.happiness+=5*count
                        self.money-=1000*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break
            
            elif choice==7:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>1700*count:
                    for i in range(count):
                        self.satiety+=200*count
                        self.health+=30*count
                        self.happiness+=50*count
                        self.money-=1700*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

            else:
                print('Нет пункта в меню: ', choice)
                break
    
    def status(self):
        print('Мое имя-', self.name, 'и я сыт на', self.satiety, 'единиц, и счастлив на', self.happiness, 'единиц, и мое здоровье соствляет', self.health, 'eдиниц, у меня в наличии', self.money, 'гривен' )
        self.pass_day

    def have_fun(self):
         print \
        (""" 
         Выберите, как вы хотите повеселится:
         0 - В меню
         1 - Выпить в баре с друзьями (50)
         2 - Пойти на каток (125)
         3 - Отдохнуть в тц (200)
         4 - Сходить в кинотеатр (500)
         5 - Провести время в ночном клубе (1500)
         6 - Слетать за границу (10 000)
         7 - Отдых на яхте на Мальдивах (100 000)
         """)
         choice=int(input())

         while choice !=0:

             if choice==0:
                 break
            
             elif choice==1:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>50*count:
                    for i in range(count):
                        self.happiness+=10*count
                        self.health-=5*count
                        self.money-=50*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==2:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>125*count:
                    for i in range(count):
                        self.happiness+=25*count
                        self.health+=5*count
                        self.money-=125*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==3:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>200*count:
                    for i in range(count):
                        self.happiness+=45*count
                        self.money-=200*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==4:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>500*count:
                    for i in range(count):
                        self.happiness+=90*count
                        self.health-=5*count
                        self.money-=500*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==5:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>1500*count:
                    for i in range(count):
                        self.happiness+=135*count
                        self.health+=5*count
                        self.money-=1500*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==6:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>10000*count:
                    for i in range(count):
                        self.happiness+=250*count
                        self.health-=30*count
                        self.money-=10000*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==7:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>100000*count:
                    for i in range(count):
                        self.happiness+=500*count
                        self.health+=50*count
                        self.money-=100000*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             else:
                print('В меню нет пункта: ', choice)
                break





def main():
    character=Life('Сергей')
    character.apartment()
    character.eat()
    character.have_fun()
    character.status()
    print('Окей')
=======
class Life:

    def __init__(self, name, satiety=100, happiness=100, health=100, money=10000000, total_days=0):
        self.name=name
        self.satiety=satiety
        self.happiness=happiness
        self.health=health
        self.money=money
        self.total_days=total_days

    def pass_day(self):
        self.satiety-=15
        self.happiness-=10
        self.health-=10
        #self.money+=sallary
        self.total_days+=1

    def apartment(self):
        print \
        ("""
        Выберите, какое жилье вы хотите приобрести: 
    
        0 - Выйти
        1 - Палатка (500)
        2 - Общежитие (1000/месяц)
        3 - Парковочное место (700/месяц)
        4 - Снять комнату (1500/месяц)
        5 - Снять квартиру (2000/месяц)
        6 - Купить квартиру (35 000)
        7 - Частный дом за городом (85 000)
        8 - Огромный особняк за городом (150 000)
        9 - Пентхаус (1 000 0000)
        """)
    
        choice = int(input("Ваш выбор: "))
        while choice!=0:

            if choice==0:
                break

            elif choice==1:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>500:
                        self.apartments='Палатка'
                        self.money-=500
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        break
                else:
                    break

            elif choice==2:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>1000:
                        self.apartments='Общежитие'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        #while apartments=='Общежитие':
                            #if total_days%30==0:
                        self.money-=1000
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        break
                        
                else:
                    break

            elif choice==3:
                if self.car!='':
                    print \
                    ("""
                    Вы уверены?
                    1 - Да
                    2 - Нет 
                    """)
                    choice1=int(input())
                    if choice1==1:
                        if self.money>700:
                            self.apartments='Парковочное место'
                            print('Теперь', self.apartments, "является вашим местом жительства")
                            #while apartments=='Парковочное место':
                                #if total_days%30==0:
                            self.money-=700
                            self.pass_day()
                        else:
                            print('У вас недостаточно денег')
                            break
                    else:
                        break
                else:
                    print('Для начала купите машину')
                    break

            elif choice==4:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>1500:
                        self.apartments='Съёмная комната'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        #while apartments=='Съёмная комната':
                            #if total_days%30==0:
                        self.money-=1500
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        choice=0

                else:
                    choice=0

            elif choice==5:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>2000:
                        self.apartments='Съёмная квартира'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        #while apartments=='Съёмная квартира':
                            #if total_days%30==0:
                        self.money-=2000
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        choice=0

                else:
                    choice=0

            elif choice==6:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>35000:
                        self.apartments='Квартира'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        self.money-=35000
                        self.pass_day()
                    else:
                        print('У вас недостаточно денег')
                        choice==0
                        break
                else:
                    choice=0

            elif choice==7:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>85000:
                        self.apartments="Дом за городом"
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        self.money-=85000
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        choice=0
                else:
                    choice=0

            elif choice==8:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>150000:
                        self.apartments='Особняк'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        self.money-=150000
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        choice=0
                else:
                    choice=0

            elif choice==9:
                print \
                ("""
                Вы уверены?
                1 - Да
                2 - Нет 
                """)
                choice1=int(input())
                if choice1==1:
                    if self.money>1000000:
                        self.apartments='Пентхаус'
                        print('Теперь', self.apartments, "является вашим местом жительства")
                        self.money-=1000000
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        choice=0
                else:
                    choice=0

            else:
                print('В меню нет пункта', choice)
                break
    
    def eat(self):
        print \
        (""" 
        Выберите, что будете есть:
        0 - В меню
        1 - Еда с мусорки
        2 - Дешевый фаст фуд (75)
        3 - Дешевое кафе (140)
        4 - Полноценный приём пищи в кафе (200)
        5 - Закупить продукты (1000)
        6 - Ресторан (1700)
        """)
        choice=int(input())

        while choice!=0:
        
            if choice==0:
                break

            elif choice==1:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                for i in range(count):
                    self.satiety+=10*count
                    self.health-=8*count
                    self.happiness-=5*count
                    if self.happiness>500:
                        self.happiness=500
                    if self.health>500:
                        self.health=500
                    if self.satiety>500:
                        self.satiety=500
                    self.pass_day()
                break

            elif choice==2:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>75*count:
                    for i in range(count):
                        self.satiety+=20*count
                        self.health-=10*count
                        self.money-=75*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

            elif choice==3:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>140*count:
                    for i in range(count):
                        self.satiety+=45*count
                        self.health-=10*count
                        self.money-=140*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break


            elif choice==4:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>200*count:
                    for i in range(count):
                        self.satiety+=65*count
                        self.money-=200*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

            elif choice==5:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>1000*count:
                    for i in range(count):
                        self.satiety+=45*count
                        self.health+=5*count
                        self.happiness+=5*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break
        
            elif choice==6:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>75*count:
                    for i in range(count):
                        self.satiety+=150*count
                        self.health+=30*count
                        self.happiness+=5*count
                        self.money-=1000*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break
            
            elif choice==7:
                count=int(input('Сколько приёмов пищи вы хотите совершить?: '))
                if self.money*count>1700*count:
                    for i in range(count):
                        self.satiety+=200*count
                        self.health+=30*count
                        self.happiness+=50*count
                        self.money-=1700*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

            else:
                print('Нет пункта в меню: ', choice)
                break
    
    def status(self):
        print('Мое имя-', self.name, 'и я сыт на', self.satiety, 'единиц, и счастлив на', self.happiness, 'единиц, и мое здоровье соствляет', self.health, 'eдиниц, у меня в наличии', self.money, 'гривен' )
        self.pass_day

    def have_fun(self):
         print \
        (""" 
         Выберите, как вы хотите повеселится:
         0 - В меню
         1 - Выпить в баре с друзьями (50)
         2 - Пойти на каток (125)
         3 - Отдохнуть в тц (200)
         4 - Сходить в кинотеатр (500)
         5 - Провести время в ночном клубе (1500)
         6 - Слетать за границу (10 000)
         7 - Отдых на яхте на Мальдивах (100 000)
         """)
         choice=int(input())

         while choice !=0:

             if choice==0:
                 break
            
             elif choice==1:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>50*count:
                    for i in range(count):
                        self.happiness+=10*count
                        self.health-=5*count
                        self.money-=50*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==2:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>125*count:
                    for i in range(count):
                        self.happiness+=25*count
                        self.health+=5*count
                        self.money-=125*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==3:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>200*count:
                    for i in range(count):
                        self.happiness+=45*count
                        self.money-=200*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==4:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>500*count:
                    for i in range(count):
                        self.happiness+=90*count
                        self.health-=5*count
                        self.money-=500*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==5:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>1500*count:
                    for i in range(count):
                        self.happiness+=135*count
                        self.health+=5*count
                        self.money-=1500*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==6:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>10000*count:
                    for i in range(count):
                        self.happiness+=250*count
                        self.health-=30*count
                        self.money-=10000*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             elif choice==7:
                count=int(input("Сколько сеансов вы хотите совершить: "))
                if self.money*count>100000*count:
                    for i in range(count):
                        self.happiness+=500*count
                        self.health+=50*count
                        self.money-=100000*count
                        if self.happiness>500:
                            self.happiness=500
                        if self.health>500:
                            self.health=500
                        if self.satiety>500:
                            self.satiety=500
                        self.pass_day()
                    break
                else:
                    print('У вас недостаточно денег')
                    break

             else:
                print('В меню нет пункта: ', choice)
                break





def main():
    character=Life('Сергей')
    character.apartment()
    character.eat()
    character.have_fun()
    character.status()
    print('Окей')
>>>>>>> b60b2edda9393feab763a2af62489de70c1f9804
main()