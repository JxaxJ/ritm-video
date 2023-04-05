import cv2
import numpy as np

# Загрузка изображения для наложения поверх видео
overlay_image = cv2.imread("R_3.png")

# Настройка размера изображения наложения
overlay_image = cv2.resize(overlay_image, (200, 150))

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

    # Копирование изображения наложения на холст
    composite[0:overlay_image.shape[0], 0:overlay_image.shape[1]] = overlay_image

    # Отображение полученного изображения
    cv2.imshow("Composite", composite)

    # Ожидание нажатия клавиши "q" для выхода из цикла
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
