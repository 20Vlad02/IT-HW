from PIL import Image

img = Image.open("images/img1.jpg")
print(f'Image size {img.size}, Image type: {img.format}')

choice = input("Выберите действие: Применить эффект(1), Сохранить изображение(2):")

if choice == '1':
    effect = input("Выберите эффект: Черно-белое(1), Отразить по вертикали(2), Отразить по горизонтали(3):")

    if effect == '1':
        img = img.convert('L')
        print("Изображение преобразовано в черно-белое.")
        img.show()

    elif effect == '2':
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        print("Изображение отражено по вертикали.")
        img.show()

    elif effect == '3':
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        print("Изображение отражено по горизонтали.")
        img.show()

    else:
        print("Неверный выбор эффекта.")

elif choice == '2':
    is_valid = True
    while is_valid:
        img = input("Введите имя файла для сохранения: ")
        try:
            img.save(img)
            print(f"Изображение сохранено как {img}")
            is_valid = False

        except Exception as e:
            print(f"Ошибка сохранения: {e}. Пожалуйста, введите корректное имя файла.")
