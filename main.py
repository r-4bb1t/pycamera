import cv2
from print_file import print_file
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication()
window = QWidget()
window.show()

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    laplacian = cv2.Laplacian(blurred_frame, cv2.CV_64F)
    canny = cv2.Canny(blurred_frame, 100, 150)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)   
    if key == 27: #27번 key는 esc
        break
    if key == 13:
        cv2.imwrite('photo.jpg', frame)
        print_file('photo.jpg')
        break
    
app.exec()
cap.release()
cv2.destroyAllWindows()

