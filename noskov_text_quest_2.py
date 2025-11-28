class Person:
    def __init__(self, name, attempt=2, knowledge=0):
        self.name = name
        self.attempt = attempt
        self.knowledge = knowledge
        self.reward_given = False

    def decrease_attempt(self, amount):
        self.attempt -= amount
        print(f"Количество попыток уменьшилось на {amount}. Осталось {self.attempt}")

    def increase_knowledge(self, amount):
        self.knowledge += amount
        print(f"Знания увеличились на {amount}%.")

    def give_reward(self):
        if not self.reward_given and self.knowledge >= 2:
            print(f"Поздравляем, {name}! Дарим вам книгу Чарльза Дарвина \"Происхождение видов путём естественного отбора или Сохранение благоприятствующих пород в борьбе за жизнь\".")
            self.reward_given = True
            exit()

def philosophy():
    try:
        while person.attempt > 0:
            print("Хорошо, ответьте на вопрос!")
            answer = input("Кто является основателем антропологического материализма: Гегель(1), Фейербах(2), Кант(3)?")

            if not answer.isdigit() or int(answer) not in [1, 2, 3]:
                raise ValueError("Необходимо ввести целое число от 1 до 3!")

            if answer == '2':
                print("Да вы Фейербахианец!")
                person.increase_knowledge(1)
                political_economy_bonus()
            elif answer == '1':
                print("Нет, Гегель стоит на голове, а не ногах!")
                person.decrease_attempt(1)
            elif answer == '3':
                print("Нет, Кант не с этим не связан!")
                person.decrease_attempt(1)

            repeat = input("Хотите ответить на вопрос ещё раз (даже если вы гений и уже ответили правильно)?(да/нет):")
            if repeat.strip().lower() != 'да':
                print("В другой раз!")
                break
        else:
            print("У вас закончилилсь попытки. Идите читайте книги!")
    except Exception as err:
        print(f"Произошла ошибка: {err}")

def philosophy_bonus():
    try:
        print("Дополнительный вопрос по немецкой философии!")
        answer = input("Назовите автора книги \"Наука логики\": Гегель(1), Ницше(2), Кант(3)?")

        if not answer.isdigit() or int(answer) not in [1, 2, 3]:
            raise ValueError("Необходимо ввести целое число от 1 до 3!")

        if answer == '1':
            print("Да вы Гегельянец!")
            person.increase_knowledge(1)
            person.give_reward()
        else:
            print("Ответ неверный.")
            person.decrease_attempt(1)
    except Exception as err:
        print(f"Произошла ошибка: {err}")

def political_economy():
    try:
        while person.attempt > 0:
            print("Хорошо, ответьте на вопрос!")
            answer = input("Кто является автором труда Исследование о природе и причинах богатства народов: Д.Рикардо(1), Р.Оуэн(2), А.Смит(3)?")

            if not answer.isdigit() or int(answer) not in [1, 2, 3]:
                raise ValueError("Необходимо ввести целое число от 1 до 3!")

            if answer == '3':
                print("Вы прям Евгений Онегин!")
                person.increase_knowledge(1)
                philosophy_bonus()
            elif answer == '1':
                print("Лучше бы вы ответили А.Смит!")
                person.decrease_attempt(1)
            elif answer == '2':
                print("Лучше бы вы ответили А.Смит!")
                person.decrease_attempt(1)

            repeat = input("Хотите ответить на вопрос ещё раз (даже если вы гений и уже ответили правильно)?(да/нет):")
            if repeat.strip().lower() != 'да':
                print("В другой раз")
                break
        else:
            print("У вас закончилсь попытки. Идите читайте книги!")
    except Exception as err:
        print(f"Произошла ошибка: {err}")

def political_economy_bonus():
    try:
        print("Дополнительный вопрос по английской политической экономии!")
        answer = input("Кто написал работу \"Начала политической экономии и налогового обложения\": А.Смит(1), Д.Рикардо(2), Т.Мальтус(3)?")

        if not answer.isdigit() or int(answer) not in [1, 2, 3]:
            raise ValueError("Необходимо ввести целое число от 1 до 3!")

        if answer == '2':
            print("Верно, это его труд!")
            person.increase_knowledge(1)
            person.give_reward()
        else:
            print("Неверно.")
            person.decrease_attempt(1)
    except Exception as err:
        print(f"Произошла ошибка: {err}")

print("Приветствуем в кружке марксистов!")
name = input("Введите ваше имя:")
person = Person(name)

enter = input("Желаете присоединиться (да/нет)?")

if 'да' == enter:
    print(f"Добро пожаловать, {name}!")

    answer = input("Какую тему для изучения вы хотите обсудить: немецкая философия(1), английская политическая экономия(2), этнографическая теория(3), политическая теория(4)?")

    if not answer.isdigit() or int(answer) not in [1, 2, 3, 4]:
        raise ValueError("Необходимо ввести целое число от 1 до 4!")

    if answer == '1':
        philosophy()
    elif answer == '2':
        political_economy()
    elif answer == '3':
        print("Наработки Л.Моргана мы и сами не изучили. В следующий раз!")
    elif answer == '4':
        print("Пока что не до политики!")

elif 'нет' == enter:
    print("Как-нибудь потом!")
