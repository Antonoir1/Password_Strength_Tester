import BruteForce, Dictionary, Hash, Load, Speed
import sys, os
import numpy as np
from PySide2 import QtCore, QtGui, QtWidgets

import time

#THREAD HANDLING BOTH THE CRACKING AND THE COMPUTATION SPEED PROCESS
class Woker(QtCore.QObject):
    finished = QtCore.Signal()
    finished2 = QtCore.Signal()

    def __init__(self, window):
        QtCore.QObject.__init__(self)
        self.window = window

    #CRACKING PROCESS
    def work(self):
        if(self.window.mode == "Brute-Force"):
            alpha = Load.get_Characters()
            end = BruteForce.simple( Hash.convert_sha256(self.window.pwd), alpha, self.window.time, len(self.window.pwd))
            self.window.crackoutput += "\n["+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"] "+end
        elif(self.window.mode == "Dictionary"):
            words = Load.load_Wordlist("./passwords")
            if(len(words) == 0):
                self.window.crackoutput += "\n["+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"] "+ "ERROR: NO .txt FILES WERE FOUND IN "+str(os.getcwd())+"\\passwords" 
            else:
                end = Dictionary.word( Hash.convert_sha256(self.window.pwd), words, self.window.time)
                self.window.crackoutput += "\n["+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"] "+end
        self.finished.emit()

    #COMPUTATION SPEED PROCESS
    def GetSpeed(self):
        alpha = Load.get_Characters()
        words = Load.load_Wordlist("./passwords")
        self.window.speedoutput += "\n"+str(Speed.Check(self.window.pwd, alpha, words))
        self.finished2.emit()

#THREAD DISPLAYING THE TIME LEFT ON THE PROGRESS BAR
class Timer(QtCore.QObject):
    working = QtCore.Signal(int)

    def __init__(self, window):
        QtCore.QObject.__init__(self)
        self.window = window

    def count(self):
        maxi = self.window.time
        start = time.perf_counter()
        while(time.perf_counter()-start < maxi and self.window.has_finished == False):
            self.working.emit((time.perf_counter()-start)*(100/maxi) )
            time.sleep(0.5)
        self.working.emit(100)

#CLASS TO HANDLE THE WINDOW
class Window(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)

        #PROCESS THREAD
        self.worker1 = Woker(self)
        self.thread = QtCore.QThread()
        self.worker1.moveToThread(self.thread)
        self.connect(self, QtCore.SIGNAL("processing()"), self.worker1, QtCore.SLOT("work()"))
        self.connect(self, QtCore.SIGNAL("computation()"), self.worker1, QtCore.SLOT("GetSpeed()"))
        self.thread.start()

        self.timer = Timer(self)
        self.thread2 = QtCore.QThread()
        self.timer.moveToThread(self.thread2)
        self.connect(self, QtCore.SIGNAL("starting()"), self.timer, QtCore.SLOT("count()"))
        self.thread2.start()

        self.worker1.finished.connect(self.End_Process)
        self.worker1.finished2.connect(self.End_ComputationSpeed)

        #MENU BARS
        bar = QtWidgets.QMenuBar()
        filemenu = QtWidgets.QMenu()
        filemenu.setTitle("File")
        escape = QtWidgets.QAction("Quit",self)
        escape.setShortcut("Escape")
        filemenu.addAction(escape)
        self.connect(escape, QtCore.SIGNAL("triggered()"),self, QtCore.SLOT("Delete()"))
        bar.addMenu(filemenu)

        #TITLE
        Title = QtWidgets.QLabel("Password Strength Tester")
        Title.setAlignment(QtCore.Qt.AlignTop)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        Title.setFont(font)
        font.setBold(False)

        #PASSWORD INPUT
        font.setPointSize(20)
        font.setBold(True)
        inputs = QtWidgets.QLabel("Inputs:")
        inputs.setAlignment(QtCore.Qt.AlignBottom)
        inputs.setFont(font)
        font.setPointSize(16)
        font.setBold(False)
        pwd = QtWidgets.QLabel("Password:")
        pwd.setFont(font)
        font.setPointSize(11)
        pwd.setFixedWidth(140)
        self.inputpwd = QtWidgets.QLineEdit()
        self.inputpwd.setFont(font)
        self.inputpwd.setMinimumWidth(300)
        self.inputpwd.setFixedHeight(35)
        
        #TIME LIMIT INPUT
        timelimit = QtWidgets.QLabel("Time Limit:")
        Hlimit = QtWidgets.QLabel("Hours:")
        Mlimit = QtWidgets.QLabel("Minutes:")
        Mlimit.setContentsMargins(15,0,0,0)
        Slimit = QtWidgets.QLabel("Seconds:")
        Slimit.setContentsMargins(15,0,0,0)
        font.setPointSize(16)
        timelimit.setFont(font)
        font.setPointSize(12)
        Hlimit.setFont(font)
        Mlimit.setFont(font)
        Slimit.setFont(font)
        font.setPointSize(11)
        timelimit.setFixedWidth(140)
        Hlimit.setFixedWidth(70)
        Mlimit.setFixedWidth(100)
        Slimit.setFixedWidth(105)
        self.inputH = QtWidgets.QSpinBox()
        self.inputH.setMinimum(0)
        self.inputH.setFont(font)
        self.inputH.setFixedWidth(107)
        self.inputH.setFixedHeight(35)
        self.inputM = QtWidgets.QSpinBox()
        self.inputM.setMinimum(0)
        self.inputM.setFont(font)
        self.inputM.setFixedWidth(107)
        self.inputM.setFixedHeight(35)
        self.inputS = QtWidgets.QSpinBox()
        self.inputS.setMinimum(0)
        self.inputS.setFont(font)
        self.inputS.setFixedWidth(107)
        self.inputS.setFixedHeight(35)

        #SELECTING MODE
        modes = QtWidgets.QLabel("Mode:")
        modes.setFixedWidth(120)
        font.setPointSize(16)
        modes.setFont(font)
        self.inputmodes = QtWidgets.QComboBox()
        font.setPointSize(12)
        self.inputmodes.setFont(font)
        self.inputmodes.setFixedWidth(175)
        self.inputmodes.addItem("Brute-Force")
        self.inputmodes.addItem("Dictionary")

        #GETTING COMPUTATION SPEED
        font.setPointSize(20)
        font.setBold(True)
        speeds = QtWidgets.QLabel("Computation speed:")
        speeds.setAlignment(QtCore.Qt.AlignBottom)
        speeds.setFont(font)
        font.setBold(False)
        font.setPointSize(16)
        self.speedB = QtWidgets.QPushButton("Get Computation speed")
        self.speedB.setFixedHeight(50)
        self.speedB.setFont(font)
        self.speedB.clicked.connect(self.ComputationSpeed)
        font.setPointSize(12)
        self.speedtxt = QtWidgets.QPlainTextEdit()
        self.speedtxt.setFont(font)
        self.speedtxt.setFixedHeight(116)

        #PROCESS BUTTON
        font.setPointSize(16)
        self.processB = QtWidgets.QPushButton("Crack")
        self.processB.setFixedHeight(50)
        self.processB.setFont(font)
        self.processB.clicked.connect(self.Process)

        #PROGRESS BAR
        self.progress = QtWidgets.QProgressBar(self)
        font.setPointSize(11)
        self.progress.setFont(font)
        self.progress.setMinimumHeight(40)
        self.labelprogress = QtWidgets.QLabel("")
        self.labelprogress.setAlignment(QtCore.Qt.AlignTop)
        self.labelprogress.setFont(font)
        font.setPointSize(16)
        
        self.timer.working.connect(self.progress.setValue)

        #OUTPUT
        font.setPointSize(20)
        font.setBold(True)
        outputs = QtWidgets.QLabel("Output:")
        outputs.setAlignment(QtCore.Qt.AlignBottom)
        outputs.setFont(font)
        font.setBold(False)
        font.setPointSize(12)
        self.outputtxt = QtWidgets.QPlainTextEdit()
        self.outputtxt.setFont(font)
        self.outputtxt.setFixedHeight(116)

        #LAYOUTS (GLOBAL LAYOUT, INPUT LAYOUT, OUTPUT LAYOUT)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(15,0,15,15)
        self.layout.setSpacing(15)
        inputlayout = QtWidgets.QHBoxLayout()
        inputlayout.setContentsMargins(0,0,0,0)
        inputlayout.setSpacing(0)
        inputlayout2 = QtWidgets.QHBoxLayout()
        inputlayout2.setContentsMargins(0,0,0,0)
        inputlayout2.setSpacing(0)
        inputlayout2.setAlignment(QtCore.Qt.AlignLeft)
        inputlayout4 = QtWidgets.QHBoxLayout()
        inputlayout4.setContentsMargins(0,0,0,0)
        inputlayout4.setSpacing(0)
        inputlayout4.setAlignment(QtCore.Qt.AlignLeft)

        #GLOBAL VARIABLES FOR PROCESSING IMAGES
        self.has_finished = True
        self.time = 0
        self.mode = ""
        self.pwd = ""
        self.speedoutput = ""
        self.crackoutput = ""

        #SET THE LAYOUTS (GLOBAL LAYOUT, INPUT LAYOUT, OUTPUT LAYOUT)
        self.layout.addWidget(Title)
        self.layout.addWidget(inputs)
        inputlayout.addWidget(pwd)
        inputlayout.addWidget(self.inputpwd)
        self.layout.addLayout(inputlayout)
        inputlayout2.addWidget(timelimit)
        inputlayout2.addWidget(Hlimit)
        inputlayout2.addWidget(self.inputH)
        inputlayout2.addWidget(Mlimit)
        inputlayout2.addWidget(self.inputM)
        inputlayout2.addWidget(Slimit)
        inputlayout2.addWidget(self.inputS)
        self.layout.addLayout(inputlayout2)
        inputlayout4.addWidget(modes)
        inputlayout4.addWidget(self.inputmodes)
        self.layout.addLayout(inputlayout4)
        self.layout.addWidget(speeds)
        self.layout.addWidget(self.speedB)
        self.layout.addWidget(self.speedtxt)
        self.layout.addWidget(self.processB)
        self.layout.addWidget(self.progress)
        self.layout.addWidget(self.labelprogress)
        self.layout.addWidget(outputs)
        self.layout.addWidget(self.outputtxt)

        #SCROLLING BAR WIDGETS
        Container = QtWidgets.QWidget()
        Container.setLayout(self.layout)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setMinimumSize(790,400)
        self.scroll.setWidget(Container)

        #SCROLLING BAR LAYOUT
        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.setContentsMargins(0,0,0,0)
        vlayout.setSpacing(0)
        vlayout.addWidget(bar)
        vlayout.addWidget(self.scroll)
        self.setLayout(vlayout)

    #DETECT CLOSING EVENT
    def closeEvent(self, event):
        if(self.has_finished == True):
            self.thread.quit()
            self.thread2.quit()
            self.deleteLater()
            event.accept()
        else:
            event.ignore()

    #DELETE THE THREAD BEFORE EXITING
    def Delete(self):
        if(self.has_finished == True):
            self.thread.quit()
            self.thread2.quit()
            QtWidgets.qApp.quit()


    #RUN THE CRACKING PROCESS
    def Process(self):
        if(self.inputpwd.text() == "" or (self.inputH.text() == "0" and self.inputM.text() == "0" and self.inputS.text() == "0")):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText( u"ERROR:\nNo password or/and no time limit was entered. Please enter a password and a time limit." )
            msg.exec()
        else:
            self.pwd = self.inputpwd.text()
            self.time  = int(self.inputH.text())*60*60+int(self.inputM.text())*60+int(self.inputS.text())
            self.mode = self.inputmodes.currentText()
            self.crackoutput = "["+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"]"+" Cracking the password \""+self.pwd+"\" in "+self.mode+" mode with a Time Limit of "+self.inputH.text()+" hours, "+self.inputM.text()+" minutes and "+self.inputS.text()+" seconds..."
            self.outputtxt.setPlainText(self.crackoutput)

            self.labelprogress.setText("in progress...")
            self.has_finished = False
            self.speedB.setEnabled(False)
            self.processB.setEnabled(False)
            self.emit(QtCore.SIGNAL("processing()"))
            self.emit(QtCore.SIGNAL("starting()"))


    #END OF THE CRACKING PROCESS
    def End_Process(self):
        self.outputtxt.setPlainText(self.crackoutput)
        self.labelprogress.setText("done.")
        self.speedB.setEnabled(True)
        self.processB.setEnabled(True)
        self.has_finished = True

    #RUN THE PROCESS THAT GET THE COMPUTATION SPEED
    def ComputationSpeed(self):
        self.speedoutput = "Getting your computation speed..."
        self.speedtxt.setPlainText(self.speedoutput)
        self.pwd = self.inputpwd.text()
        self.has_finished = False
        self.speedB.setEnabled(False)
        self.processB.setEnabled(False)
        self.emit(QtCore.SIGNAL("computation()"))
    
    #END OF THE PROCESS THAT GET THE COMPUTATION SPEED
    def End_ComputationSpeed(self):
        self.speedtxt.setPlainText(self.speedoutput)
        self.speedB.setEnabled(True)
        self.processB.setEnabled(True)
        self.has_finished = True

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("Password Strength Tester")
    window.show()
    sys.exit(app.exec_())
        