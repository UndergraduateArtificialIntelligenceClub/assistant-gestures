import sys
import json
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import *


# API KEY : 6-pyGRDak39QWhJWSGOPQHEmUNscoyne
# SECRET KEY : b3RftF6kSJfkqcpi_3K5ZRz148kNTr2p


class Window(QtGui.QMainWindow):

    def __init__(self):

        with open("config.json") as data_file:    
            self.config = json.load(data_file)

        super(Window, self).__init__()
        self.setGeometry(100, 100, 700, 700)
        self.setWindowTitle("Gesture Config Editor")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        # QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

        quitAction = QtGui.QAction("&Quit", self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.setStatusTip("Exit the application")
        quitAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(quitAction)

        self.get_api_keys()

        self.get_gesture_functions()

        self.show()

    
    def get_api_keys(self):

        #----- Enter api key -----#

        self.apiKeyText = QtGui.QLabel(self)
        self.apiKeyText.setText("Enter your FacePlusPlus public key")
        self.apiKeyText.setGeometry(205, 30, 290, 26)
        self.apiKeyText.setAlignment(Qt.AlignCenter)
        self.apiKeyText.setFont(QtGui.QFont("SansSerif", 10))

        self.apiKeyLineEdit = QtGui.QLineEdit(self)
        self.apiKeyLineEdit.move(400, 250)
        self.apiKeyLineEdit.setMaxLength(32)
        self.apiKeyLineEdit.setGeometry(205, 56, 290, 26)
        self.apiKeyLineEdit.setFont(QtGui.QFont("SansSerif", 10))
        
        self.apiKeyButton = QtGui.QPushButton("Ok", self)
        self.apiKeyButton.setGeometry(500, 55, 70, 28)

        self.apiKeyButton.clicked.connect(self.apiKeyButtonClicked)

        #----- Enter secret key -----#

        self.secretKeyText = QtGui.QLabel(self)
        self.secretKeyText.setText("Enter your FacePlusPlus private key")
        self.secretKeyText.setGeometry(205, 80, 290, 26)
        self.secretKeyText.setAlignment(Qt.AlignCenter)
        self.secretKeyText.setFont(QtGui.QFont("SansSerif", 10))

        self.secretKeyLineEdit = QtGui.QLineEdit(self)
        self.secretKeyLineEdit.move(400, 250)
        self.secretKeyLineEdit.setMaxLength(32)
        self.secretKeyLineEdit.setGeometry(205, 106, 290, 26)
        self.secretKeyLineEdit.setFont(QtGui.QFont("SansSerif", 10))
 
        self.secretKeyButton = QtGui.QPushButton("Ok", self)
        self.secretKeyButton.setGeometry(500, 105, 70, 28)
 
        self.secretKeyButton.clicked.connect(self.secretKeyButtonClicked)

    def apiKeyButtonClicked(self, text):

        print(self.apiKeyLineEdit.text())
        self.config["api_key"] = self.apiKeyLineEdit.text()
        print(self.config["api_key"])


    def secretKeyButtonClicked(self, text):

        print(self.secretKeyLineEdit.text())
        self.config["secret_key"] = self.secretKeyLineEdit.text()
        print(self.config["secret_key"])

    
    def get_gesture_functions(self):
        images = []
        text_fields = []
        combo_boxes = []

        for i in range(1, 6):
            image = QtGui.QLabel(self)
            image.setPixmap(QPixmap("{}.png".format(i)).scaled(50, 50))
            image.setGeometry(20, 120 + 80*i, 50, 50)
            images.append(image)

            text = QtGui.QLabel(self)
            text.setText("{} Fingers".format(i))
            text.setGeometry(75, 130 + 80*i, 100, 26)
            text.setAlignment(Qt.AlignLeft)
            text.setFont(QtGui.QFont("SansSerif", 10))
            text_fields.append(text)

            comboBox = QtGui.QComboBox(self)
            comboBox.addItem("Run Python script")
            comboBox.addItem("Execute terminal command")
            comboBox.addItem("Press key")
            comboBox.setGeometry(175, 130 + 80*i, 200, 26)
            combo_boxes.append(comboBox)

            comboBox.activated[str].connect(self.function_choice)


    def function_choice(self, choice):
        pass    


    def closeEvent(self, event):      
        event.ignore()      
        self.close_application()
        

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Quit", "Do you really want to exit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:

            with open("config.json", 'w') as outfile:
                json.dump(self.config, outfile, sort_keys=True, indent=4)

            sys.exit()

    
def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()