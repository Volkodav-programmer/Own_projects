class Life:

    def __init__(self, name, satiety=250, happiness=250, health=250, money=10000000, total_days=0):
        self.name=name
        self.satiety=satiety
        self.happiness=happiness
        self.health=health
        self.money=money
        self.total_days=total_days

    def pass_day(self):
        self.satiety-=25
        self.happiness-=25
        self.health-=25
        #self.money+=self.sallary
        self.total_days+=1
        if self.satiety<1:
             raise SystemExit ('Вы умерли от голода, вы прожили всего', self.total_days)
        elif self.health<1:
             raise SystemExit ('Вы умерли от болезни, вы прожили всего', self.total_days)
        elif self.happiness<1:
             raise SystemExit ('Вы умерли от депресии, вы прожили всего', self.total_days)

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
                         #while self.apartments=='Общежитие':
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
    
    def status(self):
        print('Мое имя -', self.name, 'и я сыт на', self.satiety, 'единиц, и счастлив на', self.happiness, 'единиц, и мое здоровье соствляет', self.health, 'eдиниц, у меня в наличии', self.money, 'гривен')
        self.pass_day()

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
                     self.money-=50*count
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
         2 - Дедушкина машина (3500)
         3 - Очень дешевая легковушка (5000)
         4 - Более новая машина (15000)
         5 - Хорошая машина (45 000)
         6 - Дорогая марка (100 000)
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
                    if self.money>2000:
                        self.car='старая машина со свалки'
                        self.money-=2000
                        print('Теперь', self.car, "ваша машина")
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
                    if self.money>3500:
                        self.car='дедушкина машина'
                        self.money-=3500
                        print('Теперь', self.car, "ваша машина")
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
                    if self.money>5000:
                        self.car='очень дешевая легковушка'
                        self.money-=5000
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
                    if self.money>15000:
                        self.car='более новая машина'
                        self.money-=15000
                        print('Теперь', self.car, "ваша машина")
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        break
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
                    if self.money>45000:
                        self.car='хорошая машина'
                        self.money-=45000
                        print('Теперь', self.car, "ваша машина")
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
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
                    if self.money>100000:
                        self.car='дорогая марка'
                        self.money-=100000
                        print('Теперь', self.car, "ваша машина")
                        self.pass_day()
                        break
                    else:
                        print('У вас недостаточно денег')
                        break
                 else:
                     break
             else:
                 print('Выберите пункт из меню')
                 
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
         7 - Пропустить день
         8 - Пропустить неделю
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
             character.pass_day()

         elif choice==8:
             for i in range(7):
                 character.pass_day()

         else:
            print('В меню нет пункта,', choice)
     print('Окей')
main()