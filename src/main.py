import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class PSATWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PSAT - Professional System Administration Toolkit")
        self.setFixedSize(800, 500)

        layout = QVBoxLayout()

        title = QLabel("PSAT")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 24, QFont.Bold))

        subtitle = QLabel("Professional System Administration Toolkit")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont("Arial", 14))

        developer = QLabel("Developed by\nMd. Ahsanul Kabir")
        developer.setAlignment(Qt.AlignCenter)
        developer.setFont(QFont("Arial", 12))

        version = QLabel("Version 0.1.0")
        version.setAlignment(Qt.AlignCenter)
        version.setFont(QFont("Arial", 10))

        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(developer)
        layout.addSpacing(20)
        layout.addWidget(version)
        layout.addStretch()

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PSATWindow()
    window.show()

    sys.exit(app.exec())