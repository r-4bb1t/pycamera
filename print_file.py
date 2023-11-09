from PySide6.QtPrintSupport import QPrinter, QPrinterInfo
from PySide6.QtGui import QImage, QImageReader, QPainter, QPageLayout, QPageSize
from PySide6.QtCore import Qt


def print_file(file_path):
    # 기본 프린터 정보 가져오기
    printer = QPrinterInfo.defaultPrinter()
    for p in QPrinterInfo.availablePrinters():
        if p.printerName().startswith("BIXOLON"):
            printer = p
    if printer.isNull():
        print("연결된 프린터가 없습니다.")
        return False
    else:
        print("연결된 프린터 : " + printer.printerName())

    printer = QPrinter(printer, mode=QPrinter.HighResolution)
    # 인쇄 매수 설정
    printer.setCopyCount(1)
    # 페이지 크기 설정 (A4)
    printer.setPageSize(QPageSize.A7)
    # 페이지 방향 설정 (가로)
    printer.setPageOrientation(QPageLayout.Orientation.Portrait)
    # DPI 설정(해상도)
    printer.setResolution(180)

    # 이미지 용량이 큰 경우 메모리 제한 해제
    QImageReader.setAllocationLimit(0)

    img = QImage(file_path)
    scaled_img = img.scaled(
        printer.pageRect(QPrinter.DevicePixel).width(),
        printer.pageRect(QPrinter.DevicePixel).height(),
        aspectMode=Qt.KeepAspectRatio,
        mode=Qt.SmoothTransformation,
    )
    painter = QPainter()
    painter.begin(printer)
    painter.drawImage(0, 0, scaled_img)
    painter.end()
