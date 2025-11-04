from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

# Main App Objects and Settings

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("iNspectorate Analytics Tool")
main_window.resize(1000,500)
main_window.showMaximized()
# Create all App objects

title = QLabel("iNspectorate Analytics Tool")

text1 = QLabel("Connection Status: Disconnected")
text2 = QLabel("Selected MS Folder:")
text3 = QLabel("Selected QS Folder:")

button1 = QPushButton("Connect to Database")
button2 = QPushButton("Select Folder for Matching Score (MS)")
button3 = QPushButton("Select Folder for Quality Score (QS)")

# All Designs here

master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

# Adding Widgets into the screen

row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

#

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Creating functions

'''
def connection_status():
    # if the connection has been established, will replace the text will the status
    connectionstatus = 
    text1.setText("Connection Status: Connected")

def matchingfolder():
    # Return the matching folder location
    text2.setText(#Matching Folder Location)

def qualityfolder():
    # Return the quality folder location
    text3.setText(#Quality Folder Location)
'''

connection_placeholder = ['Connection Status: Connected']

# Events
button1.clicked.text1.setText(connection_placeholder)

main_window.show()
app.exec_()