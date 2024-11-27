from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QtGui, QTableWidgetItem, QProgressDialog, QGraphicsScene, QGraphicsView,QApplication,QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from matplotlib import pyplot as plt
import pandas as pd
import os
import io
from wordcloud import WordCloud, STOPWORDS
from ui_sentimentanalysis import Ui_MainWindow
from preprocessing_module import run_preprocessing  # Import the preprocessing function


class MyAnalysisSentiment(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sentiment Analysis")

        self.iconname_widget.setHidden(True)

        # Connect the open CSV button
        self.opencsv_button.clicked.connect(self.open_csv)

        # Connect button to show WordCloud
        self.showcloudword_btn.clicked.connect(self.show_wordcloud)

        # Enable drag and drop
        self.setAcceptDrops(True)
        self.opencsv_button.setAcceptDrops(True)

        # Page Switcher Connections
        self.dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard_2.clicked.connect(self.switch_to_dashboardPage)
        self.dataset_1.clicked.connect(self.switch_to_dataset)
        self.dataset_2.clicked.connect(self.switch_to_dataset)
        self.pre_1.clicked.connect(self.switch_to_preprocessing)
        self.pre_2.clicked.connect(self.switch_to_preprocessing)
        self.ml_1.clicked.connect(self.switch_to_machinelearning)
        self.ml_2.clicked.connect(self.switch_to_machinelearning)
        self.settings_1.clicked.connect(self.switch_to_settingsPage)
        self.settings_2.clicked.connect(self.switch_to_settingsPage)

        # Connect the do preprocessing button
        self.do_preprocessing_button.clicked.connect(self.do_preprocessing)

        # Connect buttons to the function with the appropriate table widget
        self.display_res_pre_batch1.clicked.connect(lambda: self.display_preprocessing_results(
            r'D:\Project\Python\TA\SentimentAnalysis\process\Hasil-Preprocessing-Data-Cleaning.csv', 
            self.pre_table))
        self.display_res_pre_batch2.clicked.connect(lambda: self.display_preprocessing_results(
            r'D:\Project\Python\TA\SentimentAnalysis\process\Hasil-Preprocessing-Data-Steamming.csv', 
            self.pre_table2))

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_dataset(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_preprocessing(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def switch_to_machinelearning(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def switch_to_settingsPage(self):
        self.stackedWidget.setCurrentIndex(4)

    def open_csv(self):
        print("Open CSV button clicked")
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_path:
            try:
                df = pd.read_csv(file_path)
                self.update_table_widget(df)
                self.show_file_opened_message(file_path)

                # Konfirmasi untuk menyimpan file
                save_confirmation = self.confirmation_savefile(file_path)
                
                if save_confirmation == QMessageBox.Yes:
                    # Tentukan path penyimpanan di direktori kerja aplikasi
                    save_path = os.path.join(os.getcwd(), 'dataset')
                    os.makedirs(save_path, exist_ok=True)  # Buat direktori jika belum ada

                    new_file_name = "dataset.csv"
                    new_file_path = os.path.join(save_path, new_file_name)

                    # Simpan DataFrame ke file CSV di path yang baru
                    df.to_csv(new_file_path, index=False)
                    print(f"File disimpan ke {new_file_path}")

                    # Lanjutkan ke proses selanjutnya jika diperlukan
                    # self.do_preprocessing()  # Menjalankan preprocessing
                else:
                    print("File tidak disimpan.")
                    
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file: {e}")

    def show_wordcloud(self):
        # Path ke file CSV hasil preprocessing
        process_dir = os.path.join(os.getcwd(), 'process')

        os.makedirs(process_dir, exist_ok=True)

       
        file_path = os.path.join(process_dir, 'Hasil-Preprocessing-Data-Steamming.csv')
        df = pd.read_csv(file_path)

        all_words = ' '.join([str(tweet) for tweet in df['result-preprocessing']])

      
        wordcloud = WordCloud(
            width=800,
            height=600,
            background_color='black',  # Ubah background menjadi putih
            colormap='Blues_r',        # Gunakan skema warna yang lebih jelas
            collocations=False,
            stopwords=STOPWORDS
        ).generate(all_words)

      
        save_path = os.path.join(process_dir, 'wordcloud.png')

        wordcloud.to_file(save_path)
        print(f"WordCloud saved to {save_path}")
    



    def update_table_widget(self, df):
        # Clear existing data
        self.datasetview_table.clear()

        # Set the column headers
        self.datasetview_table.setColumnCount(len(df.columns))
        self.datasetview_table.setHorizontalHeaderLabels(df.columns)

        # Apply the custom style to the header
        self.datasetview_table.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #2596be; color: white; font-weight: bold;}")

        # Set the row count
        self.datasetview_table.setRowCount(len(df))

        # Add data to the table widget
        for row_index, row in df.iterrows():
            for col_index, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.datasetview_table.setItem(row_index, col_index, item)
        
        print("Data ditampilkan di Tabel")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            if file_path.endswith('.csv'):
                try:
                    df = pd.read_csv(file_path)
                    self.update_table_widget(df)
                    self.show_file_opened_message(file_path)
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to open file: {e}")

    def do_preprocessing(self):
        print("Preprocessing data...")

        # Path ke file dataset yang akan diproses
        dataset_path = os.path.join(os.getcwd(), 'dataset', 'dataset.csv')
        
        if os.path.exists(dataset_path):
            # Tampilkan progress dialog
            progress = self.show_progress_dialog("Processing...", "Preprocessing data... Please wait.")
            
            # Jalankan preprocessing
            translated_file_path = run_preprocessing(dataset_path)
            
            # Tutup progress dialog setelah selesai
            progress.close()

            # Tampilkan notifikasi menggunakan confirmation_proccess_done
            self.confirmation_proccess_done(translated_file_path)

            # Pindah ke halaman preprocessing
            self.switch_to_preprocessing()
        else:
            QMessageBox.critical(self, "Error", "Dataset file not found. Please load a dataset first.")
        
    def display_preprocessing_results(self, file_path, table_widget):
        # Muat data dari file CSV hasil preprocessing
        df = pd.read_csv(file_path)
        
        # Clear existing data in the table
        table_widget.clear()

        # Set the column headers
        table_widget.setColumnCount(len(df.columns))
        table_widget.setHorizontalHeaderLabels(df.columns)

        # Set the row count
        table_widget.setRowCount(len(df))

        # Add data to the table widget
        for row_index, row in df.iterrows():
            for col_index, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table_widget.setItem(row_index, col_index, item)
        
        print("Preprocessing results displayed in", table_widget.objectName())

    # Message Box
    def confirmation_savefile(self, file_path):
        file_name = os.path.basename(file_path)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText(f"Do you want to save the file '{file_name}' to the dataset folder & continue preprocessing?")
        msg_box.setWindowTitle("Save File")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        return msg_box.exec()
    
    def show_file_opened_message(self, file_path):
        file_name = os.path.basename(file_path)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"File '{file_name}' has been opened successfully.")
        msg_box.setWindowTitle("File Opened")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
    
    def confirmation_proccess_done(self, file_path):
        file_name = os.path.basename(file_path)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"Preprocessing complete. Data has been saved to:\n{file_name}")
        msg_box.setWindowTitle("Processing Complete")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
    
    def show_progress_dialog(self, title, label_text):
        progress = QProgressDialog(title, "Cancel", 0, 0, self)
        progress.setWindowModality(Qt.ApplicationModal)  # Gunakan ApplicationModal jika WindowModal bermasalah
        progress.setCancelButton(None)
        progress.setMinimumDuration(0)  # Tampilkan segera
        progress.setValue(0)
        progress.setLabelText(label_text)

        # Terapkan stylesheet untuk mengubah warna teks menjadi hitam
        progress.setStyleSheet("""
            QProgressDialog {
                color: black;
            }
            QProgressBar {
                color: black;
            }
            QLabel {
                color: black;
            }
        """)

        progress.show()
        QApplication.processEvents()  # Pastikan untuk memproses event GUI
        return progress
