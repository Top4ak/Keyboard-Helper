# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_app.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGroupBox,
    QHBoxLayout, QKeySequenceEdit, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 340)
        MainWindow.setMinimumSize(QSize(850, 340))
        MainWindow.setMaximumSize(QSize(850, 340))
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: QLinearGradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(45, 45, 75, 255), stop:0.427447 rgba(30, 35, 55, 235), stop:1 rgba(60, 60, 85, 255));\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(850, 340))
        self.centralwidget.setMaximumSize(QSize(850, 340))
        self.textedit_userText = QTextEdit(self.centralwidget)
        self.textedit_userText.setObjectName(u"textedit_userText")
        self.textedit_userText.setGeometry(QRect(30, 40, 500, 230))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(1, 1, 0, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(45, 45, 75, 255))
        gradient.setColorAt(0.427447, QColor(30, 35, 55, 235))
        gradient.setColorAt(1, QColor(60, 60, 85, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        gradient1 = QLinearGradient(1, 1, 0, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(45, 45, 75, 255))
        gradient1.setColorAt(0.427447, QColor(30, 35, 55, 235))
        gradient1.setColorAt(1, QColor(60, 60, 85, 255))
        brush3 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(107, 107, 107, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush4)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient2 = QLinearGradient(1, 1, 0, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(45, 45, 75, 255))
        gradient2.setColorAt(0.427447, QColor(30, 35, 55, 235))
        gradient2.setColorAt(1, QColor(60, 60, 85, 255))
        brush6 = QBrush(gradient2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        gradient3 = QLinearGradient(1, 1, 0, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(45, 45, 75, 255))
        gradient3.setColorAt(0.427447, QColor(30, 35, 55, 235))
        gradient3.setColorAt(1, QColor(60, 60, 85, 255))
        brush8 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        gradient4 = QLinearGradient(1, 1, 0, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(45, 45, 75, 255))
        gradient4.setColorAt(0.427447, QColor(30, 35, 55, 235))
        gradient4.setColorAt(1, QColor(60, 60, 85, 255))
        brush9 = QBrush(gradient4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        gradient5 = QLinearGradient(1, 1, 0, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(45, 45, 75, 255))
        gradient5.setColorAt(0.427447, QColor(30, 35, 55, 235))
        gradient5.setColorAt(1, QColor(60, 60, 85, 255))
        brush11 = QBrush(gradient5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.textedit_userText.setPalette(palette)
        self.textedit_userText.setStyleSheet(u"color: white;\n"
"font-family: \"Segoe UI\";\n")
        self.textedit_userText.setInputMethodHints(Qt.ImhEmailCharactersOnly|Qt.ImhMultiLine)
        self.textedit_userText.setAutoFormatting(QTextEdit.AutoAll)
        self.textedit_userText.setAcceptRichText(False)
        self.textedit_userText.setTabStopDistance(12)
        self.btn_settings = QPushButton(self.centralwidget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setGeometry(QRect(730, 20, 30, 30))
        self.btn_settings.setStyleSheet(u"background-color: rgba(45, 45, 70, 255);")
        icon = QIcon()
        icon.addFile(u"images/icons8-settings-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setIconSize(QSize(30, 30))
        self.btn_info = QPushButton(self.centralwidget)
        self.btn_info.setObjectName(u"btn_info")
        self.btn_info.setGeometry(QRect(630, 20, 30, 30))
        self.btn_info.setAutoFillBackground(False)
        self.btn_info.setStyleSheet(u"background-color: rgba(45, 45, 70, 255);")
        icon1 = QIcon()
        iconThemeName = u"accessories-text-editor"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"images/icons8-info-30.png", QSize(), QIcon.Normal, QIcon.Off)

        self.btn_info.setIcon(icon1)
        self.btn_info.setIconSize(QSize(30, 30))
        self.frame_settings = QFrame(self.centralwidget)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setEnabled(True)
        self.frame_settings.setGeometry(QRect(570, 60, 250, 200))
        self.frame_settings.setTabletTracking(False)
        self.frame_settings.setAcceptDrops(False)
        self.frame_settings.setStyleSheet(u"QFrame {\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"QFrame QLabel {\n"
"	border: none;\n"
"}")
        self.frame_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.frame_settings.setLineWidth(1)
        self.btn_save = QPushButton(self.frame_settings)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(150, 165, 75, 24))
        self.btn_save.setStyleSheet(u"background-color: rgba(45, 45, 70, 255);\n"
"font-size: 12pt;\n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"images/icons8-save-20.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon2)
        self.group_settings = QGroupBox(self.frame_settings)
        self.group_settings.setObjectName(u"group_settings")
        self.group_settings.setGeometry(QRect(10, 10, 221, 151))
        self.group_settings.setTabletTracking(False)
        self.group_settings.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"border: none;")
        self.verticalLayout = QVBoxLayout(self.group_settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group_start = QGroupBox(self.group_settings)
        self.group_start.setObjectName(u"group_start")
        self.group_start.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.group_start.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout = QHBoxLayout(self.group_start)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.start_icon = QLabel(self.group_start)
        self.start_icon.setObjectName(u"start_icon")
        self.start_icon.setMinimumSize(QSize(20, 20))
        self.start_icon.setMaximumSize(QSize(20, 20))
        self.start_icon.setStyleSheet(u"background-color: none;")
        self.start_icon.setPixmap(QPixmap(u"images/icons8-play-20.png"))

        self.horizontalLayout.addWidget(self.start_icon)

        self.start_label = QLabel(self.group_start)
        self.start_label.setObjectName(u"start_label")
        self.start_label.setMinimumSize(QSize(70, 0))
        self.start_label.setMaximumSize(QSize(500, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.start_label.setFont(font1)
        self.start_label.setStyleSheet(u"background-color: none;\n"
"font-size: 12pt;\n"
"color: white;\n"
"padding-right: 10px;")

        self.horizontalLayout.addWidget(self.start_label)

        self.start_value = QKeySequenceEdit(self.group_start)
        self.start_value.setObjectName(u"start_value")
        self.start_value.setStyleSheet(u"background-color: rgba(15, 20, 40, 235);\n"
"border: none;")
        self.start_value.setClearButtonEnabled(True)
        self.start_value.setMaximumSequenceLength(1)

        self.horizontalLayout.addWidget(self.start_value)


        self.verticalLayout.addWidget(self.group_start)

        self.group_stop = QGroupBox(self.group_settings)
        self.group_stop.setObjectName(u"group_stop")
        self.group_stop.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.horizontalLayout_3 = QHBoxLayout(self.group_stop)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stop_icon = QLabel(self.group_stop)
        self.stop_icon.setObjectName(u"stop_icon")
        self.stop_icon.setMaximumSize(QSize(20, 20))
        self.stop_icon.setStyleSheet(u"background-color: none;")
        self.stop_icon.setPixmap(QPixmap(u"images/icons8-stop-20.png"))

        self.horizontalLayout_3.addWidget(self.stop_icon)

        self.stop_label = QLabel(self.group_stop)
        self.stop_label.setObjectName(u"stop_label")
        self.stop_label.setMinimumSize(QSize(70, 0))
        self.stop_label.setFont(font1)
        self.stop_label.setStyleSheet(u"background-color: none;\n"
"font-size: 12pt;\n"
"color: white;\n"
"padding-right: 10px;")

        self.horizontalLayout_3.addWidget(self.stop_label)

        self.stop_value = QKeySequenceEdit(self.group_stop)
        self.stop_value.setObjectName(u"stop_value")
        self.stop_value.setStyleSheet(u"background-color: rgba(15, 20, 40, 235);\n"
"border: none;")
        self.stop_value.setClearButtonEnabled(True)
        self.stop_value.setMaximumSequenceLength(1)

        self.horizontalLayout_3.addWidget(self.stop_value)


        self.verticalLayout.addWidget(self.group_stop)

        self.group_delay = QGroupBox(self.group_settings)
        self.group_delay.setObjectName(u"group_delay")
        self.group_delay.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.group_delay)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.delay_icon = QLabel(self.group_delay)
        self.delay_icon.setObjectName(u"delay_icon")
        self.delay_icon.setMaximumSize(QSize(20, 20))
        self.delay_icon.setStyleSheet(u"background-color: none;")
        self.delay_icon.setPixmap(QPixmap(u"images/icons8-time-machine-20.png"))

        self.horizontalLayout_4.addWidget(self.delay_icon)

        self.delay_label = QLabel(self.group_delay)
        self.delay_label.setObjectName(u"delay_label")
        self.delay_label.setMinimumSize(QSize(122, 0))
        self.delay_label.setFont(font1)
        self.delay_label.setStyleSheet(u"background-color: none;\n"
"font-size: 12pt;\n"
"color: white;\n"
"padding-right: 10px;")

        self.horizontalLayout_4.addWidget(self.delay_label)

        self.delay_value = QDoubleSpinBox(self.group_delay)
        self.delay_value.setObjectName(u"delay_value")
        self.delay_value.setStyleSheet(u"color: white;\n"
"background-color: rgba(15, 20, 40, 235);")

        self.horizontalLayout_4.addWidget(self.delay_value)


        self.verticalLayout.addWidget(self.group_delay)

        self.group_interval = QGroupBox(self.group_settings)
        self.group_interval.setObjectName(u"group_interval")
        self.group_interval.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.horizontalLayout_5 = QHBoxLayout(self.group_interval)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.interval_icon = QLabel(self.group_interval)
        self.interval_icon.setObjectName(u"interval_icon")
        self.interval_icon.setMaximumSize(QSize(20, 20))
        self.interval_icon.setStyleSheet(u"background-color: none;")
        self.interval_icon.setPixmap(QPixmap(u"images/icons8-time-lapse-20.png"))

        self.horizontalLayout_5.addWidget(self.interval_icon)

        self.interval_label = QLabel(self.group_interval)
        self.interval_label.setObjectName(u"interval_label")
        self.interval_label.setMinimumSize(QSize(122, 0))
        self.interval_label.setMaximumSize(QSize(167777, 16777215))
        self.interval_label.setFont(font1)
        self.interval_label.setStyleSheet(u"background-color: none;\n"
"font-size: 12pt;\n"
"color: white;\n"
"padding-right: 10px;")

        self.horizontalLayout_5.addWidget(self.interval_label)

        self.interval_value = QDoubleSpinBox(self.group_interval)
        self.interval_value.setObjectName(u"interval_value")
        self.interval_value.setStyleSheet(u"color: white;\n"
"background-color: rgba(15, 20, 40, 235);")
        self.interval_value.setSingleStep(0.010000000000000)

        self.horizontalLayout_5.addWidget(self.interval_value)


        self.verticalLayout.addWidget(self.group_interval)

        self.group_randomFactor = QGroupBox(self.group_settings)
        self.group_randomFactor.setObjectName(u"group_randomFactor")
        self.group_randomFactor.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.horizontalLayout_9 = QHBoxLayout(self.group_randomFactor)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.randomFactor_icon = QLabel(self.group_randomFactor)
        self.randomFactor_icon.setObjectName(u"randomFactor_icon")
        self.randomFactor_icon.setMaximumSize(QSize(20, 20))
        self.randomFactor_icon.setStyleSheet(u"background-color: none;")
        self.randomFactor_icon.setPixmap(QPixmap(u"images/icons8-dice-20.png"))

        self.horizontalLayout_9.addWidget(self.randomFactor_icon)

        self.randomFactor_label = QLabel(self.group_randomFactor)
        self.randomFactor_label.setObjectName(u"randomFactor_label")
        self.randomFactor_label.setMinimumSize(QSize(70, 0))
        self.randomFactor_label.setMaximumSize(QSize(167777, 16777215))
        self.randomFactor_label.setFont(font1)
        self.randomFactor_label.setStyleSheet(u"background-color: none;\n"
"font-size: 12pt;\n"
"color: white;\n"
"padding-right: 10px;")

        self.horizontalLayout_9.addWidget(self.randomFactor_label)

        self.randomFactor_value = QDoubleSpinBox(self.group_randomFactor)
        self.randomFactor_value.setObjectName(u"randomFactor_value")
        self.randomFactor_value.setStyleSheet(u"color: white;\n"
"background-color: rgba(15, 20, 40, 235);")
        self.randomFactor_value.setSingleStep(0.010000000000000)

        self.horizontalLayout_9.addWidget(self.randomFactor_value)


        self.verticalLayout.addWidget(self.group_randomFactor)

        self.label_writeText = QLabel(self.centralwidget)
        self.label_writeText.setObjectName(u"label_writeText")
        self.label_writeText.setGeometry(QRect(30, 10, 221, 31))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_writeText.setFont(font2)
        self.label_writeText.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 16pt;")
        self.frame_info = QFrame(self.centralwidget)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setGeometry(QRect(570, 60, 250, 200))
        self.frame_info.setStyleSheet(u"QFrame {\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"QFrame QLabel {\n"
"	border: none;\n"
"}")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.label_about = QLabel(self.frame_info)
        self.label_about.setObjectName(u"label_about")
        self.label_about.setGeometry(QRect(10, 10, 231, 91))
        self.label_about.setStyleSheet(u"color: white;\n"
"background-color: none;")
        self.label_about.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_about.setWordWrap(False)
        self.group_createdBy = QGroupBox(self.frame_info)
        self.group_createdBy.setObjectName(u"group_createdBy")
        self.group_createdBy.setGeometry(QRect(10, 140, 231, 51))
        self.group_createdBy.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.verticalLayout_2 = QVBoxLayout(self.group_createdBy)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_createdBy = QLabel(self.group_createdBy)
        self.label_createdBy.setObjectName(u"label_createdBy")
        self.label_createdBy.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"")
        self.label_createdBy.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_createdBy)

        self.group_credits = QGroupBox(self.group_createdBy)
        self.group_credits.setObjectName(u"group_credits")
        self.group_credits.setStyleSheet(u"border: none;\n"
"background-color: none;\n"
"padding-bottom: 2px;")
        self.horizontalLayout_10 = QHBoxLayout(self.group_credits)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_github = QPushButton(self.group_credits)
        self.btn_github.setObjectName(u"btn_github")
        self.btn_github.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"border: none;")
        icon3 = QIcon()
        icon3.addFile(u"images/icons8-github-20.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_github.setIcon(icon3)

        self.horizontalLayout_10.addWidget(self.btn_github)

        self.btn_telegram = QPushButton(self.group_credits)
        self.btn_telegram.setObjectName(u"btn_telegram")
        self.btn_telegram.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"border: none;")
        icon4 = QIcon()
        icon4.addFile(u"images/icons8-telegram-20.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_telegram.setIcon(icon4)

        self.horizontalLayout_10.addWidget(self.btn_telegram)


        self.verticalLayout_2.addWidget(self.group_credits)

        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(30, 280, 40, 40))
        self.btn_start.setStyleSheet(u"background-color: rgba(45, 45, 70, 255);")
        icon5 = QIcon()
        icon5.addFile(u"images/icons8-play-20.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start.setIcon(icon5)
        self.btn_start.setIconSize(QSize(40, 40))
        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(90, 280, 40, 40))
        self.btn_stop.setStyleSheet(u"background-color: rgba(45, 45, 70, 255);")
        icon6 = QIcon()
        icon6.addFile(u"images/icons8-stop-20.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stop.setIcon(icon6)
        self.btn_stop.setIconSize(QSize(40, 40))
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_settings.raise_()
        self.textedit_userText.raise_()
        self.btn_settings.raise_()
        self.btn_info.raise_()
        self.label_writeText.raise_()
        self.start_icon.raise_()
        self.frame_info.raise_()
        self.btn_start.raise_()
        self.btn_stop.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Anti-Anti-Pasta", None))
        self.btn_settings.setText("")
        self.btn_info.setText("")
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.start_icon.setText("")
        self.start_label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_icon.setText("")
        self.stop_label.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.delay_icon.setText("")
        self.delay_label.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.interval_icon.setText("")
        self.interval_label.setText(QCoreApplication.translate("MainWindow", u"Interval", None))
        self.randomFactor_icon.setText("")
        self.randomFactor_label.setText(QCoreApplication.translate("MainWindow", u"Random Factor", None))
        self.label_writeText.setText(QCoreApplication.translate("MainWindow", u"Write text here", None))
        self.label_about.setText(QCoreApplication.translate("MainWindow", u"The app helps you bypass anti-pasta\n"
"protection. When you are not allowed to\n"
"use copied material in certain services.\n"
"This program simulates keystrokes on the\n"
"keyboard and types the text you want.", None))
        self.label_createdBy.setText(QCoreApplication.translate("MainWindow", u"Created by", None))
        self.btn_github.setText(QCoreApplication.translate("MainWindow", u"Top4aK", None))
        self.btn_telegram.setText(QCoreApplication.translate("MainWindow", u"miketapok", None))
        self.btn_start.setText("")
        self.btn_stop.setText("")
    # retranslateUi

