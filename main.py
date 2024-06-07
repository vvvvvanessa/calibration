from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

import sys
from Calibration.calib import Calibration

if __name__ == "__main__":
    app = QApplication([])
    main_window = Calibration()
    sys.exit(app.exec())

