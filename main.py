import sys
import cv2
import numpy as np
import time

# from kucc_frame import image_frame
from sw_frame import image_frame
from print_file import print_file
from playsound import playsound

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtCore import QTimer


class MainApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.capture = cv2.VideoCapture(0)
        self.setStyleSheet("background-color: black;")
        self.video_size = QSize(640, 480)
        self.setup_ui()
        self.setup_camera()

    def print_photo(self):
        photo = self.capture.read()[1]

        alpha = 1.5
        beta = 0
        photo = cv2.convertScaleAbs(photo, alpha=alpha, beta=beta)

        modify = np.ones(photo.shape, dtype="uint8") * 120
        photo = cv2.subtract(photo, modify)

        playsound("shutter.mp3")
        cv2.imwrite("photo.png", photo)
        image_frame("photo.png")
        print_file("print_photo.png")
        time.sleep(0.3)

    def setup_ui(self):
        self.image_label = QLabel()
        self.image_label.setFixedSize(self.video_size)

        self.photo_button_layout = QVBoxLayout()
        self.photo_button_layout.setContentsMargins(0, 10, 0, 10)
        self.photo_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.photo_button = QPushButton()
        self.photo_button.setIcon(QIcon("camera.png"))
        self.photo_button.setIconSize(QSize(50, 50))
        self.photo_button.setFixedSize(100, 100)
        self.photo_button.setStyleSheet(
            "background-color: white; border: 0px solid; border-radius: 50px;"
        )
        self.photo_button.clicked.connect(self.print_photo)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.image_label)

        self.main_layout.addLayout(self.photo_button_layout)
        self.photo_button_layout.addWidget(self.photo_button)

        self.setLayout(self.main_layout)

    def setup_camera(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = QImage(
            frame,
            frame.shape[1],
            frame.shape[0],
            frame.strides[0],
            QImage.Format_RGB888,
        )
        self.image_label.setPixmap(QPixmap.fromImage(image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainApp()
    win.show()
    sys.exit(app.exec())
