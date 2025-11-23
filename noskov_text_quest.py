# Носков Владислав Александрович

### Первое задание: текстовый квест

def philosophy():
    try:
        while True:
            print("Хорошо, ответьте на вопрос!")
            answer = input("Кто является основателем антропологического материализма: Гегель(1), Фейербах(2), Кант(3)?")

            if not answer.isdigit() or int(answer) not in [1, 2, 3]:
                raise ValueError("Необходимо ввести целое число от 1 до 3!")

            if answer == '2':
                print("Да вы Фейербахианец!")
            elif answer == '1':
                print("Нет, Гегель стоит на голове, а не ногах!")
            elif answer == '3':
                print("Нет, Кант не с этим не связан!")

            repeat = input("Хотите ответить на вопрос ещё раз (даже если вы гений и уже ответили правильно)? (да/нет):")
            if repeat.strip().lower() != 'да':
                print("В другой раз!")
                break
    except Exception as err:
        print(f"Произошла ошибка: {err}")


def political_economy():
    try:
        while True:
            print("Хорошо, ответьте на вопрос!")
            answer = input("Кто является автором труда Исследование о природе и причинах богатства народов: Д.Рикардо(1), Р.Оуэн(2), А.Смит(3)?")

            if not answer.isdigit() or int(answer) not in [1, 2, 3]:
                raise ValueError("Необходимо ввести целое число от 1 до 3!")

            if answer == '3':
                print("Вы прям Евгений Онегин!")
            elif answer == '1':
                print("Лучше бы вы ответили А.Смит!")
            elif answer == '2':
                print("Лучше бы вы ответили А.Смит!")

            repeat = input("Хотите ответить на вопрос ещё раз (даже если вы гений и уже ответили правильно)? (да/нет):")
            if repeat.strip().lower() != 'да':
                print("В другой раз")
                break
    except Exception as err:
        print(f"Произошла ошибка: {err}")


try:
    print("Приветствуем в кружке марксистов!")

    enter = input("Желаете присоединиться (да/нет)?")

    if 'да' == enter:
        print("Добро пожаловать!")

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
except Exception as err:
    print(f"Произошла ошибка: {err}")
