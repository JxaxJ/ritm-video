from PIL import Image
import numpy as np
import cv2

# Загрузка изображения для наложения поверх видео
overlay_image = Image.open("R_3.png")

# Настройка размера изображения наложения
overlay_image = overlay_image.resize((200, 150))

# Создание видеопотока с помощью USB-камеры
cap = cv2.VideoCapture(0)

while True:
    # Получение кадра видео из камеры
    ret, frame = cap.read()

    # Изменение размера кадра, если необходимо
    # frame = cv2.resize(frame, (640, 480))

    # Создание пустого холста для объединения кадра видео и изображения наложения
    height, width = frame.shape[:2]
    composite = np.zeros((height, width, 3), np.uint8)

    # Копирование кадра видео на холст
    composite[0:height, 0:width] = frame

    # Конвертирование изображения наложения в формат, который может быть объединен с кадром видео
    overlay_image_array = np.array(overlay_image)
    overlay_image_array = cv2.cvtColor(overlay_image_array, cv2.COLOR_RGB2BGR)

    # Копирование изображения наложения на холст
    composite[0:overlay_image_array.shape[0], 0:overlay_image_array.shape[1]] = overlay_image_array

    # Отображение полученного изображения
    cv2.imshow("Composite", composite)

    # Ожидание нажатия клавиши "q" для выхода из цикла
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
