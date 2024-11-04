import sys
from PySide6.QtWidgets import QApplication
from barcode_checksum import BarcodeChecksum

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BarcodeChecksum()
    window.show()
    sys.exit(app.exec())