
class Life:
    import random
    a=random.randint(27000, 32400)
    def __init__(self, name, satiety=250, happiness=250, health=250, money=1000, total_days=7560, days_for_death=a, education_list=[], apartmemts='', days_in_game=0):
        self.name=name
        self.satiety=satiety
        self.happiness=happiness
        self.health=health
        self.money=money
        self.total_days=total_days
        self.days_for_death=days_for_death
        self.education_list=education_list
        self.days_in_game=days_in_game
        self.apartments=apartmemts

    def pass_day(self):
        self.satiety-=12.5
        self.happiness-=12.5
        self.health-=12.5
        self.days_in_game+=1
        self.total_days+=1

        if self.satiety<1:
             raise SystemExit ('Вы умерли от голода, вы прожили всего', self.days_in_game, 'дней')
        elif self.health<1:
             raise SystemExit ('Вы умерли от болезни, вы прожили всего', self.days_in_game, 'дней')
        elif self.happiness<1:
             raise SystemExit ('Вы умерли от депресии, вы прожили всего', self.days_in_game, 'дней')
        elif self.total_days>self.days_for_death:
             raise SystemExit ('Вы умерли от старости, прожив долгую жизнь')
        if self.total_days%360==0:
             print('У вас сегодня день рождения! В подарок вы получаете 10000 грн')
             self.money+=10000
        if self.apartments=='Общежитие':
             if self.days_in_game%30==0:
                 self.money-=1000
                 print('Снята плата по общежитию')
        elif self.apartments=='Парковочное место':
            if self.days_in_game%30==0:
                 self.money-=700
                 print('Снята плата по Парковочному месту')

        elif self.apartments=='Съёмная комната':
            if self.days_in_game%30==0:
                 self.money-=1500
                 print('Снята оплата за съемную комнату')

        elif self.apartments=='Съёмная квартира':
            if self.days_in_game%30==0:
                 self.money-=5000
                 print('Снята оплата за сьёмную квартиру')
        if self.money<0:
             self.money=0 
        if self.days_in_game%30==0:
            self.money+=self.sallary   
            print('Вы получили зп')   



    def apartment(self):
        print \
        ("""
        Выберите, какое жилье вы хотите приобрести: 
    
        0 - Выйти
        1 - Палатка (500)
        2 - Общежитие (1000/месяц)
        3 - Парковочное место (700/месяц)
        4 - Снять комнату (1500/месяц)
        5 - Снять квартиру (5000/месяц)
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
                         self.money-=1000
                         self.pass_day()
                         break
                     else:
                         print('У вас недостаточно денег')
                         break
                        
                else:
                    break

            elif choice==3:
                 print \
                 ("""
                 Вы уверены?
                 1 - Да
                 2 - Нет 
                 """)
                 choice1=int(input())
                 if choice1==1:
                     if self.car!='':
                         if self.money>700:
                             self.apartments='Парковочное место'
                             print('Теперь', self.apartments, "является вашим местом жительства")
                             self.money-=700
                             self.pass_day()
                             break
                         else:
                             print('У вас недостаточно денег')
                             break
                     else:
                         print('Для начала купите машину')
                         break
                 else:
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
                if self.money>75*count:
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
                if self.money>140*count:
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
                if self.money>200*count:
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
                if self.money>1000*count:
                    for i in range(count):
                        self.satiety+=45*count
                        self.health+=5*count
                        self.happiness+=5*count
                        self.money-=1000
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
                if self.money>1700*count:
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
    
    def satiety_status(self):
        if self.satiety>400:
            s='Я сыт до отвала'
        elif 250<self.satiety<400:
            s='Я не голоден'  
        elif 100<self.satiety<250:
            s='Я голоден'
        elif self.satiety<100:
            s='Я при голодной смерти'
        return s

    def health_status(self):
        if self.health>400:
            h='Я здоров как бык'
        elif 250<self.health<400:
            h='Я здоров'  
        elif 100<self.health<250:
            h='Я чувствую себя не очень хорошо'
        elif self.health<100:
            h='Я присмерти от болезни'
        return h  

    def happiness_status(self):
        if self.happiness>400:
            ha='Я считаю, что жизнь прекрасна'
        elif 250<self.happiness<400:
            ha='Я чувтсвую себя счастливым'  
        elif 100<self.happiness<250:
            ha='Я чувствую себя грустным'
        elif self.happiness<100:
            ha='Я готов покончить жизнь самоубийством'
        return ha              

    def status(self):
        print('Мое имя -', self.name, 'и я сыт на', self.satiety, 'единиц, и счастлив на', self.happiness, 'единиц, и мое здоровье соствляет', self.health, 'eдиниц, у меня в наличии', self.money, 'гривен. '
        'Лет осталось до смерти: ', self.days_for_death//360, 'Дней в игре: ', self.days_in_game)

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
                if self.money>50*count:
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
                if self.money>125*count:
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
                if self.money>200*count:
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
                if self.money>500*count:
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
                if self.money>1500*count:
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
                if self.money>10000*count:
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
                if self.money>100000*count:
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

    def treatment(self):
         print \
         (""" 
         Выберите, как вы хотите лечится:
         0 - В меню
         1 - Таблетки с мусорки
         2 - Лечение от бабки (50)
         3 - Государственная больница (150)
         4 - Частная клиника (500)
         5 - Лучшая больница в стране (1500)
         6 - Лечится за границей (5000)
         """)
         choice=int(input())
         while choice!=0:

             if choice==0:
                 break

             elif choice==1:
                 count=int(input("Введите количество сеансов: "))
                 for i in range(count):
                     self.health+=30*count
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
                 count=int(input('Введите количество сеансов: '))
                 if self.money>50*count:
                     for i in range(count):
                         self.health+=50*count
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

             elif choice==3:
                 count=int(input('Введите количество сеансов: '))
                 if self.money>150*count:
                     for i in range(count):
                         self.health+=70*count
                         self.money-=150*count

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
                 count=int(input('Введите количество сеансов: '))
                 if self.money>500*count:
                     for i in range(count):
                         self.health+=100*count
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
                 count=int(input('Введите количество сеансов: '))
                 if self.money>1500*count:
                     for i in range(count):
                         self.health+=150*count
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
                 count=int(input('Введите количество сеансов: '))
                 if self.money>5000*count:
                     for i in range(count):
                         self.health+=250*count
                         self.money-=5000*count

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
                 print('В меню нет пункта', choice)
                 break

    def clothes(self):
         print \
         (""" 
         Выберите, какую одежду вы хотите купить?
         
         0 - Выйти
         1 - Порванные футболка и штаны (50)
         2 - Дешевый секонд-хэнд (500)
         3 - Свитер и штаны (1000)
         4 - Рубашка с брюками (1500)
         5 - Дорогой смокинг (5000)
         """)
         choice=int(input())

         while choice!=0:

             if choice==1:
                 if self.money>50:
                     self.clothes='Порванные футболка и штаны'
                     print('Теперь вашей одеждой является: ', self.clothes)
                     self.money-=50
                     self.pass_day()
                     break
                 else:
                     print('У вас недостаточно денег')
                     break

             elif choice==2:
                 if self.money>500:
                     self.clothes='Дешевый секонд-хэнд'
                     print('Теперь вашей одеждой является: ', self.clothes)
                     self.money-=500
                     self.pass_day()
                     break
                 else:
                     print('У вас недостаточно денег')
                     break

             elif choice==3:
                 if self.money>1000:
                     self.clothes='Свитер и штаны'
                     print('Теперь вашей одеждой является: ', self.clothes)
                     self.money-=1000
                     self.pass_day()
                     break
                 else:
                     print('У вас недостаточно денег')
                     break

             elif choice==4:
                 if self.money>1500:
                     self.clothes='Рубашка с брюками'
                     print('Теперь вашей одеждой является: ', self.clothes)
                     self.money-=1500
                     self.pass_day()
                     break
                 else:
                     print('У вас недостаточно денег')
                     break
                 
             elif choice==5:
                 if self.money>5000:
                     self.clothes='Дорогой смокинг'
                     print('Теперь вашей одеждой является: ', self.clothes)
                     self.money-=50
                     self.pass_day()
                     break
                 else:
                     print('У вас недостаточно денег')
                     break
             
             else:
                 print('В меню нет пункта', choice)

    def car(self):
         print \
         (""" 
         Выберите, какую машину вы хотите взять
         0 - В меню
         1 - Старая машина со свалки (2000)
         2 - Дедушкина машина (5000)
         3 - Очень дешевая легковушка (25 000)
         4 - Более новая машина (50 000)
         5 - Хорошая машина (150 000)
         6 - Дорогая марка (500 000)
         7 - Грёбанный вертолёт (4 000 000)
         """)
         choice=int(input())

         while choice!=0:

             if choice==1:
                 print \
                 ("""
                 Вы уверены?
                 1 - Да
                 2 - Нет 
                 """)
                 choice1=int(input())
                 if choice1==1:
                     if 'Права' in self.education_list:
                         if self.money>2000:
                             self.car='Старая машина со свалки'
                             self.money-=2000
                             print('Теперь', self.car, "ваша машина")
                             self.pass_day()
                             break
                         else:
                             print('У вас недостаточно денег')
                             break
                     else:
                         print('Для начала получите права')
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
                     if 'Права' in self.education_list:
                         if self.money>5000:
                             self.car='Дедушкина машина'
                             self.money-=5000
                             print('Теперь', self.car, "ваша машина")
                             self.pass_day()
                             break

                         else:
                             print('У вас недостаточно денег')
                             break

                     else:
                        print("Для начала получите права")
                        break
                 else:
                     break


             elif choice==3:
                 print \
                 ("""
                 Вы уверены?
                 1 - Да
                 2 - Нет 
                 """)
                 choice1=int(input())
                 if choice1==1:
                    if self.money>25000:
                        self.car='Очень дешевая легковушка'
                        self.money-=25000
                        print('Теперь', self.car, "ваша машина")
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        break
                 else:
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
                     if 'Права' in self.education_list:
                         if self.money>50000:
                             self.car='Более новая машина'
                             self.money-=50000
                             print('Теперь', self.car, "ваша машина")
                             self.pass_day()
                             break
                         else:
                             print('У вас недостаточно денег')
                             break
                        
                     else:
                         print("Для начала получите права")
                 else:
                     break

             elif choice==5:
                 print \
                 ("""
                 Вы уверены?
                 1 - Да
                 2 - Нет 
                 """)
                 choice1=int(input())
                 if choice1==1:
                     if 'Права' in self.education_list:
                         if self.money>15000:
                             self.car='Хорошая машина'
                             self.money-=15000
                             print('Теперь', self.car, "ваша машина")
                             self.pass_day()
                             break
                         else:
                             print('У вас недостаточно денег')
                             break
                     else:
                         print('Для начала получите права')
                         break
                 else:
                     break

             elif choice==6:
                 print \
                 ("""
                 Вы уверены?
                 1 - Да
                 2 - Нет 
                 """)
                 choice1=int(input())
                 if choice1==1:
                     if 'Права' in self.education_list:
                         if self.money>500000:
                             self.car='Дорогая марка'
                             self.money-=500000
                             print('Теперь', self.car, "ваша машина")
                             self.pass_day()
                             break
                         else:
                             print('У вас недостаточно денег')
                             break
                     else:
                         print('Для начала получите права')
                         break
                 else:
                     break

             elif choice==7:
                 print \
                 ("""
                 Вы уверены?
                 1 - Да
                 2 - Нет 
                 """)
                 choice1=int(input())
                 if choice1==1:
                     if 'Права' in self.education_list:
                         if self.money>4000000:
                             self.car='Грёбанный вертолёт'
                             self.money-=4000000
                             print('Теперь у вас есть грёбанный вертолет')
                             self.pass_day()
                             break
                         else:
                             print('У вас недостаточно денег')
                             break
                     else:
                         print('Для начала получите права')
                         break
                 else:
                     break
             else:
                 print('Выберите пункт из меню')
                              
    def education(self):
         print \
         ('''
         Выберите пункт в меню
         0 - Выйти
         1 - Закончить школу (5000)
         2 - Закончить еще два класса (2000)
         3 - Закончить техникум (10 000)
         4 - Закончить медицинский (20 000)
         5 - Закончить экономический (35 000)
         6 - Закончить юридический (50 000)
         7 - Получить права (1500)
         8 - Получить права на вертолёт (50 000)
         ''')
         choice=int(input())
         while choice!=0:
             if choice==1:
                 if self.money>5000:
                     self.total_days+=810
                     self.money-=5000
                     self.education_list.append('Среднее образование')
                     print('Вы отучились в школе')
                     self.pass_day()
                     break
                 else:
                     print('У вас недостаточно денег')
                     break
             
             elif choice==2:
                 if 'Среднее образование' in self.education_list:
                     if self.money>2000:
                         self.total_days+=810
                         self.money-=2000
                         self.education_list.append('Высшее образование')
                         print('Вы закончили еще два класса')
                         self.pass_day()
                         break
                     else:
                         print('У вас недостаточно денег')
                         break
                 else:
                     print('Для начала отучитесь в школе')
                     break
            
             elif choice==3:
                 if 'Среднее образование' in self.education_list:
                     if self.money>10000:
                         self.total_days+=1080
                         self.money-=10000
                         self.education_list.append('Техникум')
                         print('Вы закончили техникум')
                         self.pass_day()
                         break
                     else:
                         print('У вас недостаточно денег')
                         break
                 else:
                     print('Для начала отучитесь в школе')
                     break
             
             elif choice==4:
                 if 'Высшее образование' in self.education_list:
                     if self.money>20000:
                         self.total_days+=1800
                         self.money-=20000
                         self.education_list.append('Медицинский')
                         print('Вы закончили медицинский')
                         self.pass_day()
                         break
                     else:
                         print('У вас недостаточно денег')
                         break
                 else:
                     print('Для начала получите высшее образование')
                     break
             
             elif choice==5:
                 if 'Высшее образование' in self.education_list:
                     if self.money>35000:
                         self.total_days+=810
                         self.money-=35000
                         self.education_list.append('Экономический')
                         print('Вы закончили экономический')
                         self.pass_day()
                         break
                     else:
                         print('У вас недостаточно денег')
                         break
                 else:
                     print('Для начала отучитесь в школе')
                     break
                
             elif choice==6:
                 if 'Высшее образование' in self.education_list:
                     if self.money>50000:
                         self.total_days+=810
                         self.money-=50000
                         self.education_list.append('Юридический')
                         print('Вы закончили юридический')
                         self.pass_day()
                         break
                     else:
                         print('У вас недостаточно денег')
                         break
                 else:
                     print('Для начала отучитесь в школе')
                     break
                
             elif choice==7:
                 if self.money>1500:
                     self.total_days+=30
                     self.money-=30
                     self.education_list.append('Права на грёбанный вертолёт')
                     print('Вы получили права на грёбанный вертолёт')
                     break
                 else:
                     print('У вас недостаточно денег')
                     break
             else:
                 print('В меню нет пункта')
                 break
            
    def job(self):
        print \
        ('''
        Выберите работу на которую вы хотите устроится:
        
        0 - Выход
        1 - Промоутер (3000)
        2 - Дворник (5000)
        3 - Продавец (7000)
        4 - Таксист (10 000)
        5 - Каменщик (13 000)
        6 - Сварщик (15 000)
        7 - Медбрат (20 000)
        8 - Врач (25 000)
        9 - Бухгалтер (35 000)
        10 - Директор банка (100 000)
        11 - Министр финансов (150 000)
        12 - Президент (500 000)
        ''')
        choice=int(input())
        while choice!=0:
            if choice==1:
                self.job_days=0
                self.sallary=3000
                print('Вы стали Промоутером')
                break
            elif choice==2:
                if 'Среднее образование' in self.education_list:
                    if self.apartment!='':
                        if self.clothes!='':
                            self.job_days=0
                            self.sallary=5000
                            print('Вы стали Дворником, поздравляю')
                            break
                        else:
                            print('Для начала вам нужна одежда поновее')
                    else:
                        print('Для начала вам нужно жилье получше')
                else:
                    print('Вот говорили тебе, что без образования тебя даже дворником работать не возьмут, вот и я не возьму, иди учись')
                    break
            elif choice==3:
                if self.job_days>90:
                    if 'Среднее образование' in self.education_list:
                        self.job_days=0
                        self.sallary=7000
                        break
                    else:
                        print('Отучитесь в школе')
                        break
                else:
                    print('Вам нужен опыт работы')
            elif choice==4:
                if self.car!='':
                    if self.apartments!='' and self.apartments!='Палатка':
                        if self.clothes!='Порванные футболка и штаны' and self.clothes!='':
                            self.sallary=10000
                            print('Вы стали таксистом')
                            break
                        else:
                            print('Вам нужна одежда поновее')
                    else:
                        print('Вам нужно жильё поновее')
                else:
                    print('Для начала купите машину')
                    break
            elif choice==5:
                if 'Техникум' in self.education_list:
                    if self.car!='' and self.car!='Старая машина со свалки':
                        if self.clothes!='Порванные одежда и штаны' and self.clothes!='' and self.clothes!='Дешёвый секонд-хэнд':
                            if self.apartments!='' and self.apartments!='Палатка' and self.apartments!='Общежитие':
                                self.job_days=0
                                self.sallary=13000
                                break
                            else:
                                print('Вам нужно жильё поновее')
                                break
                        else:
                            print('Вам нужна одежда поновее')
                            break
                    else:
                        print('Вам нужна машина поновее')
                        break
                else:
                    print('Для начала пройдите обучение')
                    break
            elif choice==6:
                if 'Техникум' in self.education_list:
                    if self.job_days>90:
                        self.sallary=15000
                        self.job_days=0
                        break
                    else:
                        print('Вам нужен опыт работы')
                        break
                else:
                    print('Для начала отучитесь')
                    break
            elif choice==7:
                if 'Медицинский' in self.education_list:
                    if self.car!='' and self.car!='Старая машина со свалки' and self.car!='Очень дешевая легковушка':
                        if self.clothes!='Порванные одежда и штаны' and self.clothes!='' and self.clothes!='Дешёвый секонд-хэнд':
                            if self.apartments!='' and self.apartments!='Палатка' and self.apartments!='Парковочное место' and self.apartments!='Сьёмная комната':
                                self.job_days=0
                                self.sallary=20000
                                break
                            else:
                                print('Вам нужно новое место жительства')
                                break
                        else:
                            print('Вам нужна одежда поновее')
                            break
                    else:
                        print('Вам нужна машина поновее')
                        break
                else:
                    print('Для начала отучитесь')  
                    break
            elif choice==8:
                if 'Медицинский' in self.education_list:
                    if self.job_days>90:
                        self.sallary=25000
                        self.job_days=0
                        break
                    else:
                        print('Вам нужен опыт работы')
                        break                                                                                         
                else:
                     print('Для начала обучитесь')
                     break
            elif choice==9:
                if 'Экономический' in self.education_list:
                    if self.car!='' and self.car!='Старая машина со свалки' and self.car!='Очень дешевая легковушка' and self.car!='Более новая машина':
                        if self.clothes!='Порванные одежда и штаны' and self.clothes!='' and self.clothes!='Дешёвый секонд-хэнд' and self.clothes!='Свитер и штаны':
                            if self.apartments!='' and self.apartments!='Палатка' and self.apartments!='Парковочное место' and self.apartments!='Сьёмная комната' and self.apartments!='Квартира':
                                self.job_days=0
                                self.sallary=35000
                                break
                            else:
                                print('Вам нужна квартира поновее')
                                break
                        else:
                            print('Вам нужна одежда поновее')
                            break
                    else:
                        print('Вам нужна машина поновее')
                        break
                else:
                    print('Для начала отучитесь')
                    break
            elif choice==10:
                if 'Экономический' in self.education_list:
                    if self.job_days>90:
                        self.sallary=100000
                        self.job_days=0
                        break
                    else:
                        print('Вам нужен опыт работы')
                        break
                else:
                    print('Вам нужно обучится')
                    break
            elif choice==11:
                if 'Юридический' and 'Экономический' in self.education_list:
                    if self.car=='Дорогая марка':
                        if self.apartments=='Огромный особняк за городом':
                            self.job_days=0
                            self.sallary=150000
                            print('Вы стали министром финансов')
                            break
                        else:
                            print('Вам нужно жильё поновее')
                            break
                    else:
                        print('Вам нужна машина поновее')
                        break
                else:
                    print('Закончите надлежащее образование')
                    break

                    
                    
            elif choice==12:
                if 'Юридический' in self.education_list:
                    if self.clothes=='Дорогой смокинг':
                        if self.car=='Грёбанный вертолёт':
                            if self.apartments=='Пентхаус':
                                if self.job_days>1800:
                                    if self.money>1000000:
                                        self.money-=1000000
                                        d=random.randint(1,4)
                                        if d==1:
                                            print('Вы стали президентом')
                                            self.sallary=500000
                                            break
                                        else:
                                            print('Вы проиграли выборы')
                                            break
                                    else:
                                        print('Для начала соберите 1 000 000 для того что бы баллотироваться в приезиденты')
                                        break
                                else:
                                    print('Вам нужен опыт работы')
                                    break
                            else:
                                print('Вам нужно жильё поновее')
                                break
                        else:
                            print('Вам нужен вертолет))')
                            break
                    else:
                        print('Без нормальной одежды в президенты пойти не получится')
                        break
                else:
                    print('Вам нужно надлежащее образование')
                    break
            else:
                print('Выберите пункт из меню')

def main():
     name=input('Введите имя персонажа, за которого вы будете играть: ')
     character=Life(name)
     choice=None
     while choice !=0:
         character.status()
         print \
         (""" 
         Выберите пункт в меню
         0 - Выйти из игры
         1 - Поесть что нибудь
         2 - Вылечится
         3 - Развлечься
         4 - Купить новое жильё
         5 - Купить новую одежду
         6 - Купить новую машину
         7 - Пойти учиться
         8 - Пропустить день
         9 - Пропустить неделю
         10 - Найти новую работу
         """)
         choice=int(input())
         

         if choice==0:
             print('Буэнас Диас')

         elif choice==1:
             character.eat()
             
         elif choice==2:
             character.treatment()
                
         elif choice==3:
             character.have_fun()

         elif choice==4:
             character.apartment()

         elif choice==5:
             character.clothes()

         elif choice==6:
             character.car()

         elif choice==7:
             character.education()

         elif choice==8:
             character.pass_day()

         elif choice==9:
             for i in range(7):
                 character.pass_day()
         elif choice==10:
             character.job()

         else:
            print('В меню нет пункта,', choice)
     print('Окей')
main()
