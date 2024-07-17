import cv2
import numpy as np

cap = cv2.VideoCapture('VIDEO.mp4')

if not cap.isOpened():
    print("Erro ao abrir o arquivo de vídeo.")
    exit()

tracker = cv2.TrackerCSRT_create()

pessoas_contadas = 0

ret, frame = cap.read()
if not ret:
    print("Não foi possível ler o primeiro frame do vídeo.")
    exit()

roi = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Frame")

tracker.init(frame, roi)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    ret, bbox = tracker.update(frame)

    if ret:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

        line_y = 150  
        if p1[1] <= line_y <= p2[1]:
            pessoas_contadas += 1
            print(f"Pessoas contadas: {pessoas_contadas}")

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
