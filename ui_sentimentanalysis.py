# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1198, 944)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/asset/images/fhmup.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"")
        MainWindow.setIconSize(QSize(30, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.iconname_widget = QWidget(self.centralwidget)
        self.iconname_widget.setObjectName(u"iconname_widget")
        self.iconname_widget.setMaximumSize(QSize(140, 16777215))
        self.iconname_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(197, 173, 237);\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	text-align: left;\n"
"	height: 40px;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{	\n"
"	background-color:#F0F0F0;\n"
"	color:#8C9AFF;\n"
"	font-weight:bold;	\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika mouse hover */\n"
"	color: white; \n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.iconname_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 5, -1)
        self.label_2 = QLabel(self.iconname_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 70))
        self.label_2.setMaximumSize(QSize(70, 70))
        self.label_2.setPixmap(QPixmap(u":/asset/images/fhmupp.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.iconname_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: black; /* Warna default teks */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #6b80ff; /* Warna teks saat di-hover */\n"
"}\n"
"")
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setMargin(0)
        self.label_3.setIndent(-1)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_2 = QPushButton(self.iconname_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        icon1 = QIcon()
        icon1.addFile(u":/asset/images/dashboard_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/asset/images/dashboard_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_2.setIcon(icon1)
        self.dashboard_2.setIconSize(QSize(25, 25))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.pre_2 = QPushButton(self.iconname_widget)
        self.pre_2.setObjectName(u"pre_2")
        self.pre_2.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/asset/images/nlp_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/asset/images/nlp_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pre_2.setIcon(icon2)
        self.pre_2.setIconSize(QSize(30, 30))
        self.pre_2.setCheckable(True)
        self.pre_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pre_2)

        self.dataset_2 = QPushButton(self.iconname_widget)
        self.dataset_2.setObjectName(u"dataset_2")
        icon3 = QIcon()
        icon3.addFile(u":/asset/images/dataset_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/asset/images/dataset_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dataset_2.setIcon(icon3)
        self.dataset_2.setIconSize(QSize(30, 30))
        self.dataset_2.setCheckable(True)
        self.dataset_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dataset_2)

        self.ml_2 = QPushButton(self.iconname_widget)
        self.ml_2.setObjectName(u"ml_2")
        icon4 = QIcon()
        icon4.addFile(u":/asset/images/decision-tree_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/asset/images/decision-tree_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ml_2.setIcon(icon4)
        self.ml_2.setIconSize(QSize(30, 30))
        self.ml_2.setCheckable(True)
        self.ml_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.ml_2)

        self.settings_2 = QPushButton(self.iconname_widget)
        self.settings_2.setObjectName(u"settings_2")
        icon5 = QIcon()
        icon5.addFile(u":/asset/images/settinga_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/asset/images/settings_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_2.setIcon(icon5)
        self.settings_2.setIconSize(QSize(30, 30))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 391, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.logout_2 = QPushButton(self.iconname_widget)
        self.logout_2.setObjectName(u"logout_2")
        icon6 = QIcon()
        icon6.addFile(u":/asset/images/turn-off_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/asset/images/turn-off_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.logout_2.setIcon(icon6)
        self.logout_2.setIconSize(QSize(25, 25))
        self.logout_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.logout_2)


        self.gridLayout.addWidget(self.iconname_widget, 0, 1, 1, 1)

        self.icononly_widget = QWidget(self.centralwidget)
        self.icononly_widget.setObjectName(u"icononly_widget")
        self.icononly_widget.setMaximumSize(QSize(100, 16777215))
        self.icononly_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(197, 173, 237);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	text-align:center;\n"
"	height: 40px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked{	\n"
"	background-color:#F0F0F0;\n"
"	color:#8C9AFF;\n"
"	font-weight:bold;	\n"
"	\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.icononly_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icononly_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 70))
        self.label.setMaximumSize(QSize(70, 70))
        self.label.setPixmap(QPixmap(u":/asset/images/fhmupp.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_1 = QPushButton(self.icononly_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        self.dashboard_1.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika mouse hover */\n"
"}")
        self.dashboard_1.setIcon(icon1)
        self.dashboard_1.setIconSize(QSize(25, 25))
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.dataset_1 = QPushButton(self.icononly_widget)
        self.dataset_1.setObjectName(u"dataset_1")
        self.dataset_1.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika mouse hover */\n"
"}")
        self.dataset_1.setIcon(icon3)
        self.dataset_1.setIconSize(QSize(30, 30))
        self.dataset_1.setCheckable(True)
        self.dataset_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dataset_1)

        self.pre_1 = QPushButton(self.icononly_widget)
        self.pre_1.setObjectName(u"pre_1")
        self.pre_1.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika mouse hover */\n"
"}")
        self.pre_1.setIcon(icon2)
        self.pre_1.setIconSize(QSize(30, 30))
        self.pre_1.setCheckable(True)
        self.pre_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pre_1)

        self.ml_1 = QPushButton(self.icononly_widget)
        self.ml_1.setObjectName(u"ml_1")
        self.ml_1.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika mouse hover */\n"
"}")
        self.ml_1.setIcon(icon4)
        self.ml_1.setIconSize(QSize(30, 30))
        self.ml_1.setCheckable(True)
        self.ml_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.ml_1)

        self.settings_1 = QPushButton(self.icononly_widget)
        self.settings_1.setObjectName(u"settings_1")
        self.settings_1.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika mouse hover */\n"
"}")
        self.settings_1.setIcon(icon5)
        self.settings_1.setIconSize(QSize(30, 30))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 391, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logout_1 = QPushButton(self.icononly_widget)
        self.logout_1.setObjectName(u"logout_1")
        self.logout_1.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika mouse hover */\n"
"}")
        self.logout_1.setIcon(icon6)
        self.logout_1.setIconSize(QSize(25, 25))
        self.logout_1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.logout_1)


        self.gridLayout.addWidget(self.icononly_widget, 0, 0, 1, 1)

        self.mainmenu = QWidget(self.centralwidget)
        self.mainmenu.setObjectName(u"mainmenu")
        self.verticalLayout_5 = QVBoxLayout(self.mainmenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.header_widget = QWidget(self.mainmenu)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(197, 173, 237);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_13 = QPushButton(self.header_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"/* Style untuk QPushButton */\n"
"QPushButton {\n"
"    color: black; /* Ganti dengan warna teks yang diinginkan */\n"
"    text-align: center;\n"
"    height: 25px;\n"
"    border: 1px solid #8C9AFF; /* Border dengan warna tertentu */\n"
"    border-radius: 10px; /* Sudut yang melengkung */\n"
"    background-color: rgb(197, 173, 237); /* Warna latar belakang default */\n"
"    padding: 5px; /* Padding default */\n"
"}\n"
"\n"
"/* Ketika tombol di-hover (mouse di atas tombol) */\n"
"QPushButton:hover {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika mouse hover */\n"
"}\n"
"\n"
"/* Ketika tombol ditekan */\n"
"QPushButton:pressed {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika tombol ditekan */\n"
"    padding-top: 7px; /* Tambah padding di atas untuk efek 'masuk ke dalam' */\n"
"    padding-left: 7px; /* Tambah padding di kiri untuk efek 'masuk ke dalam' */\n"
"    border-style: inset; /* Ganti border style menjadi inset untuk efek 'masuk ke dalam' */\n"
"}\n"
"\n"
"/* K"
                        "etika tombol dilepaskan (unclicked), kembali ke state normal */\n"
"QPushButton:!pressed {\n"
"    background-color: rgb(197, 173, 237); /* Warna latar belakang default */\n"
"    padding-top: 5px; /* Kembali ke padding default */\n"
"    padding-left: 5px; /* Kembali ke padding default */\n"
"    border-style: outset; /* Border style normal */\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/asset/images/menus_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/asset/images/menus_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_13.setIcon(icon7)
        self.pushButton_13.setIconSize(QSize(20, 20))
        self.pushButton_13.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton_13)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(870, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.profile_btn = QPushButton(self.header_widget)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setStyleSheet(u"/* Style untuk QPushButton */\n"
"QPushButton {\n"
"    color: black; /* Ganti dengan warna teks yang diinginkan */\n"
"    text-align: center;\n"
"    height: 25px;\n"
"    border: 1px solid #8C9AFF; /* Border dengan warna tertentu */\n"
"    border-radius: 10px; /* Sudut yang melengkung */\n"
"    background-color: rgb(197, 173, 237); /* Warna latar belakang default */\n"
"    padding: 5px; /* Padding default */\n"
"}\n"
"\n"
"/* Ketika tombol di-hover (mouse di atas tombol) */\n"
"QPushButton:hover {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika mouse hover */\n"
"}\n"
"\n"
"/* Ketika tombol ditekan */\n"
"QPushButton:pressed {\n"
"    background-color: #8C9AFF; /* Warna latar belakang ketika tombol ditekan */\n"
"    padding-top: 7px; /* Tambah padding di atas untuk efek 'masuk ke dalam' */\n"
"    padding-left: 7px; /* Tambah padding di kiri untuk efek 'masuk ke dalam' */\n"
"    border-style: inset; /* Ganti border style menjadi inset untuk efek 'masuk ke dalam' */\n"
"}\n"
"\n"
"/* K"
                        "etika tombol dilepaskan (unclicked), kembali ke state normal */\n"
"QPushButton:!pressed {\n"
"    background-color: rgb(197, 173, 237); /* Warna latar belakang default */\n"
"    padding-top: 5px; /* Kembali ke padding default */\n"
"    padding-left: 5px; /* Kembali ke padding default */\n"
"    border-style: outset; /* Border style normal */\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/asset/images/myProfilePhoto-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profile_btn.setIcon(icon8)
        self.profile_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.profile_btn)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.mainmenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.stackedWidget.addWidget(self.dashboard_page)
        self.dataset_page = QWidget()
        self.dataset_page.setObjectName(u"dataset_page")
        self.opencsv_button = QPushButton(self.dataset_page)
        self.opencsv_button.setObjectName(u"opencsv_button")
        self.opencsv_button.setGeometry(QRect(20, 20, 931, 131))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.opencsv_button.setFont(font1)
        self.opencsv_button.setAcceptDrops(True)
        self.opencsv_button.setStyleSheet(u"QPushButton {\n"
"    color: black; /* Warna teks */\n"
"    text-align: center;\n"
"    height: 25px;\n"
"    border: 1px solid #8C9AFF; /* Border dengan warna tertentu */\n"
"    border-radius: 10px; /* Sudut yang melengkung */\n"
"    background-color: darkgray; /* Warna latar belakang abu-abu */\n"
"    padding: 5px; /* Padding default */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: #8C9AFF; /* Warna latar belakang saat hover */\n"
"	\n"
"    font-weight: bold; /* Menjadikan teks tebal saat hover */\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/asset/images/file_csv_format_type_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.opencsv_button.setIcon(icon9)
        self.opencsv_button.setIconSize(QSize(50, 50))
        self.opencsv_button.setCheckable(True)
        self.opencsv_button.setAutoExclusive(True)
        self.datasetview_table = QTableWidget(self.dataset_page)
        self.datasetview_table.setObjectName(u"datasetview_table")
        self.datasetview_table.setGeometry(QRect(20, 180, 1021, 551))
        self.datasetview_table.setAcceptDrops(True)
        self.datasetview_table.setStyleSheet(u"QTableWidget {\n"
"    padding: 5px;\n"
"    gridline-color: black; /* Mengatur warna garis grid antar sel */\n"
"    border: 1px solid black; /* Menambahkan border pada seluruh tabel */\n"
"    color: black; /* Mengatur warna teks di dalam tabel */\n"
"    background-color: white;\n"
"    border-bottom: 3px solid rgba(0, 0, 0, 0.25); /* Efek bayangan di bawah */\n"
"    border-right: 3px solid rgba(0, 0, 0, 0.25); /* Efek bayangan di sisi kanan */\n"
"	border-top: 3px solid rgba(0, 0, 0, 0.25); \n"
"    border-left: 3px solid rgba(0, 0, 0, 0.25); \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: lightgray; /* Warna latar belakang header kolom */\n"
"    border: 1px solid black; /* Border di sekitar header */\n"
"    color: black; /* Warna teks di header kolom */\n"
"}\n"
"\n"
"QHeaderView::section:first-of-type {\n"
"    background-color: lightgray; /* Warna latar belakang header kolom pertama */\n"
"    color: black; /* Warna teks di header kolom pertama */\n"
"}\n"
"")
        self.datasetview_table.setDragEnabled(True)
        self.do_preprocessing_button = QPushButton(self.dataset_page)
        self.do_preprocessing_button.setObjectName(u"do_preprocessing_button")
        self.do_preprocessing_button.setGeometry(QRect(960, 20, 81, 131))
        self.do_preprocessing_button.setFont(font1)
        self.do_preprocessing_button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.do_preprocessing_button.setAcceptDrops(True)
        self.do_preprocessing_button.setLayoutDirection(Qt.LeftToRight)
        self.do_preprocessing_button.setAutoFillBackground(False)
        self.do_preprocessing_button.setStyleSheet(u"QPushButton {\n"
"    color: black; /* Warna teks */\n"
"    text-align: center;\n"
"    height: 25px;\n"
"    border: 1px solid #8C9AFF; /* Border dengan warna tertentu */\n"
"    border-radius: 10px; /* Sudut yang melengkung */\n"
"    background-color: darkgray; /* Warna latar belakang abu-abu */\n"
"    padding: 5px; /* Padding default */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #8C9AFF; /* Warna latar belakang saat hover */\n"
"}")
        self.do_preprocessing_button.setText(u"")
        icon10 = QIcon()
        icon10.addFile(u":/asset/images/process.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.do_preprocessing_button.setIcon(icon10)
        self.do_preprocessing_button.setIconSize(QSize(35, 35))
        self.do_preprocessing_button.setCheckable(True)
        self.do_preprocessing_button.setAutoExclusive(True)
        self.stackedWidget.addWidget(self.dataset_page)
        self.preprocessing_page = QWidget()
        self.preprocessing_page.setObjectName(u"preprocessing_page")
        self.label_9 = QLabel(self.preprocessing_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, -10, 131, 41))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color:black;")
        self.pre_table = QTableWidget(self.preprocessing_page)
        self.pre_table.setObjectName(u"pre_table")
        self.pre_table.setGeometry(QRect(20, 40, 1021, 271))
        self.pre_table.setAcceptDrops(True)
        self.pre_table.setStyleSheet(u"QTableWidget {\n"
"    padding: 5px;\n"
"    gridline-color: black; /* Mengatur warna garis grid antar sel */\n"
"    border: 1px solid black; /* Menambahkan border pada seluruh tabel */\n"
"    color: black; /* Mengatur warna teks di dalam tabel */\n"
"    background-color: white;\n"
"    border-bottom: 3px solid rgba(0, 0, 0, 0.25); /* Efek bayangan di bawah */\n"
"    border-right: 3px solid rgba(0, 0, 0, 0.25); /* Efek bayangan di sisi kanan */\n"
"	border-top: 3px solid rgba(0, 0, 0, 0.25); \n"
"    border-left: 3px solid rgba(0, 0, 0, 0.25); \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: lightgray; /* Warna latar belakang header kolom */\n"
"    border: 1px solid black; /* Border di sekitar header */\n"
"    color: black; /* Warna teks di header kolom */\n"
"}\n"
"\n"
"QHeaderView::section:first-of-type {\n"
"    background-color: lightgray; /* Warna latar belakang header kolom pertama */\n"
"    color: black; /* Warna teks di header kolom pertama */\n"
"}\n"
"")
        self.pre_table.setDragEnabled(True)
        self.pre_table2 = QTableWidget(self.preprocessing_page)
        self.pre_table2.setObjectName(u"pre_table2")
        self.pre_table2.setGeometry(QRect(20, 360, 1021, 271))
        self.pre_table2.setAcceptDrops(True)
        self.pre_table2.setStyleSheet(u"QTableWidget {\n"
"    padding: 5px;\n"
"    gridline-color: black; /* Mengatur warna garis grid antar sel */\n"
"    border: 1px solid black; /* Menambahkan border pada seluruh tabel */\n"
"    color: black; /* Mengatur warna teks di dalam tabel */\n"
"    background-color: white;\n"
"    border-bottom: 3px solid rgba(0, 0, 0, 0.25); /* Efek bayangan di bawah */\n"
"    border-right: 3px solid rgba(0, 0, 0, 0.25); /* Efek bayangan di sisi kanan */\n"
"	border-top: 3px solid rgba(0, 0, 0, 0.25); \n"
"    border-left: 3px solid rgba(0, 0, 0, 0.25); \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: lightgray; /* Warna latar belakang header kolom */\n"
"    border: 1px solid black; /* Border di sekitar header */\n"
"    color: black; /* Warna teks di header kolom */\n"
"}\n"
"\n"
"QHeaderView::section:first-of-type {\n"
"    background-color: lightgray; /* Warna latar belakang header kolom pertama */\n"
"    color: black; /* Warna teks di header kolom pertama */\n"
"}\n"
"")
        self.pre_table2.setDragEnabled(True)
        self.label_10 = QLabel(self.preprocessing_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 310, 131, 41))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color:black;")
        self.display_res_pre_batch1 = QPushButton(self.preprocessing_page)
        self.display_res_pre_batch1.setObjectName(u"display_res_pre_batch1")
        self.display_res_pre_batch1.setGeometry(QRect(160, 0, 181, 31))
        self.display_res_pre_batch1.setFont(font1)
        self.display_res_pre_batch1.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.display_res_pre_batch1.setAcceptDrops(True)
        self.display_res_pre_batch1.setLayoutDirection(Qt.LeftToRight)
        self.display_res_pre_batch1.setAutoFillBackground(False)
        self.display_res_pre_batch1.setStyleSheet(u"QPushButton {\n"
"    color: black; /* Warna teks */\n"
"    text-align: center;\n"
"    height: 25px;\n"
"    border: 1px solid #8C9AFF; /* Border dengan warna tertentu */\n"
"    border-radius: 10px; /* Sudut yang melengkung */\n"
"    background-color: darkgray; /* Warna latar belakang abu-abu */\n"
"    padding: 5px; /* Padding default */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #8C9AFF; /* Warna latar belakang saat hover */\n"
"}")
        self.display_res_pre_batch1.setText(u"TAMPILKAN")
        self.display_res_pre_batch1.setIconSize(QSize(35, 35))
        self.display_res_pre_batch1.setCheckable(True)
        self.display_res_pre_batch1.setAutoExclusive(True)
        self.display_res_pre_batch2 = QPushButton(self.preprocessing_page)
        self.display_res_pre_batch2.setObjectName(u"display_res_pre_batch2")
        self.display_res_pre_batch2.setGeometry(QRect(160, 320, 181, 31))
        self.display_res_pre_batch2.setFont(font1)
        self.display_res_pre_batch2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.display_res_pre_batch2.setAcceptDrops(True)
        self.display_res_pre_batch2.setLayoutDirection(Qt.LeftToRight)
        self.display_res_pre_batch2.setAutoFillBackground(False)
        self.display_res_pre_batch2.setStyleSheet(u"QPushButton {\n"
"    color: black; /* Warna teks */\n"
"    text-align: center;\n"
"    height: 25px;\n"
"    border: 1px solid #8C9AFF; /* Border dengan warna tertentu */\n"
"    border-radius: 10px; /* Sudut yang melengkung */\n"
"    background-color: darkgray; /* Warna latar belakang abu-abu */\n"
"    padding: 5px; /* Padding default */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #8C9AFF; /* Warna latar belakang saat hover */\n"
"}")
        self.display_res_pre_batch2.setText(u"TAMPILKAN")
        self.display_res_pre_batch2.setIconSize(QSize(35, 35))
        self.display_res_pre_batch2.setCheckable(True)
        self.display_res_pre_batch2.setAutoExclusive(True)
        self.showcloudword_btn = QPushButton(self.preprocessing_page)
        self.showcloudword_btn.setObjectName(u"showcloudword_btn")
        self.showcloudword_btn.setGeometry(QRect(20, 640, 91, 31))
        self.showcloudword_btn.setFont(font1)
        self.showcloudword_btn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.showcloudword_btn.setAcceptDrops(True)
        self.showcloudword_btn.setLayoutDirection(Qt.LeftToRight)
        self.showcloudword_btn.setAutoFillBackground(False)
        self.showcloudword_btn.setStyleSheet(u"QPushButton {\n"
"    color: black; /* Warna teks */\n"
"    text-align: center;\n"
"    height: 25px;\n"
"    border: 1px solid #8C9AFF; /* Border dengan warna tertentu */\n"
"    border-radius: 10px; /* Sudut yang melengkung */\n"
"    background-color: darkgray; /* Warna latar belakang abu-abu */\n"
"    padding: 5px; /* Padding default */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #8C9AFF; /* Warna latar belakang saat hover */\n"
"}")
        self.showcloudword_btn.setText(u"ANALYSIS")
        self.showcloudword_btn.setIconSize(QSize(35, 35))
        self.showcloudword_btn.setCheckable(True)
        self.showcloudword_btn.setAutoExclusive(True)
        self.wordcloud_label = QLabel(self.preprocessing_page)
        self.wordcloud_label.setObjectName(u"wordcloud_label")
        self.wordcloud_label.setGeometry(QRect(120, 640, 371, 231))
        self.wordcloud_label.setScaledContents(True)
        self.distsentiment_label = QLabel(self.preprocessing_page)
        self.distsentiment_label.setObjectName(u"distsentiment_label")
        self.distsentiment_label.setGeometry(QRect(550, 640, 371, 231))
        self.distsentiment_label.setScaledContents(True)
        self.label_analysis = QLabel(self.preprocessing_page)
        self.label_analysis.setObjectName(u"label_analysis")
        self.label_analysis.setGeometry(QRect(950, 630, 191, 121))
        font3 = QFont()
        font3.setPointSize(10)
        self.label_analysis.setFont(font3)
        self.label_analysis.setStyleSheet(u"color:black;")
        self.stackedWidget.addWidget(self.preprocessing_page)
        self.ml_page = QWidget()
        self.ml_page.setObjectName(u"ml_page")
        self.label_7 = QLabel(self.ml_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 291, 41))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color:black;")
        self.stackedWidget.addWidget(self.ml_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.label_8 = QLabel(self.setting_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(340, 290, 291, 41))
        self.label_8.setFont(font2)
        self.stackedWidget.addWidget(self.setting_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.mainmenu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_13.toggled.connect(self.icononly_widget.setHidden)
        self.pushButton_13.toggled.connect(self.iconname_widget.setVisible)
        self.dataset_1.toggled.connect(self.dataset_2.setChecked)
        self.pre_1.toggled.connect(self.pre_2.setChecked)
        self.ml_1.toggled.connect(self.ml_2.setChecked)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.dataset_2.toggled.connect(self.dataset_1.setChecked)
        self.pre_2.toggled.connect(self.pre_1.setChecked)
        self.ml_2.toggled.connect(self.ml_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.logout_1.toggled.connect(MainWindow.close)
        self.logout_2.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sentiment Analysis", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ANALISIS<br/>SENTIMEN</p></body></html>", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pre_2.setText(QCoreApplication.translate("MainWindow", u"Pre-Processing", None))
        self.dataset_2.setText(QCoreApplication.translate("MainWindow", u"Dataset", None))
        self.ml_2.setText(QCoreApplication.translate("MainWindow", u"ML", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.logout_2.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.label.setText("")
        self.dashboard_1.setText("")
        self.dataset_1.setText("")
        self.pre_1.setText("")
        self.ml_1.setText("")
        self.settings_1.setText("")
        self.logout_1.setText("")
        self.pushButton_13.setText("")
        self.profile_btn.setText("")
        self.opencsv_button.setText(QCoreApplication.translate("MainWindow", u"Open CSV.\n"
"\n"
"or drop csv. here", None))
#if QT_CONFIG(tooltip)
        self.do_preprocessing_button.setToolTip(QCoreApplication.translate("MainWindow", u"Do Preprocessing", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cleaning", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Stemming", None))
#if QT_CONFIG(tooltip)
        self.display_res_pre_batch1.setToolTip(QCoreApplication.translate("MainWindow", u"Do Preprocessing", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.display_res_pre_batch2.setToolTip(QCoreApplication.translate("MainWindow", u"Do Preprocessing", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.showcloudword_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Do Preprocessing", None))
#endif // QT_CONFIG(tooltip)
        self.wordcloud_label.setText("")
        self.distsentiment_label.setText("")
        self.label_analysis.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"HASIL PENELITIAN", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
    # retranslateUi

