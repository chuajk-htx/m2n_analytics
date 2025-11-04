# This is just a demo application
# Guide to running the application
# Step 1: Activate the environment using the command
# source /home/timothy/anaconda3/bin/activate Analytics
# Step 2: Run the application using the command
# python app.py

import sys


from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Demo Application for iNspectorate Analytics Platform</h1>", parent=window)
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec())