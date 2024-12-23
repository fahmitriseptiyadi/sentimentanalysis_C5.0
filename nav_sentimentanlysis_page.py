from PySide6.QtWidgets import (
    QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QProgressDialog, QApplication
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import pandas as pd
import os
from wordcloud import WordCloud, STOPWORDS
from ui_sentimentanalysis import Ui_MainWindow
from preprocessing_module import run_preprocessing_cleanning, plot_sentiment_distribution


class MyAnalysisSentiment(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sentiment Analysis")
        self.iconname_widget.setHidden(True)

        # Connect buttons
        self._connect_buttons()

        # Enable drag and drop
        self.setAcceptDrops(True)
        self.opencsv_button.setAcceptDrops(True)

    def _connect_buttons(self):
        """Connect buttons to their respective functions."""
        self.opencsv_button.clicked.connect(self.open_csv)
        self.showcloudword_btn.clicked.connect(self.show_wordcloud)
        self.do_preprocessing_button.clicked.connect(self.do_preprocessing)

        # Display results
        self.display_res_pre_batch1.clicked.connect(lambda: self.display_preprocessing_results(
            os.path.join(os.getcwd(), 'process', 'Hasil-Preprocessing-Data-Cleaning.csv'), self.pre_table
        ))
        self.display_res_pre_batch2.clicked.connect(lambda: self.display_preprocessing_results(
            os.path.join(os.getcwd(), 'process', 'Hasil-Preprocessing-Data-Steamming.csv'), self.pre_table2
        ))

        # Page switcher connections
        page_map = {
            self.dashboard_1: 0, self.dashboard_2: 0,
            self.dataset_1: 1, self.dataset_2: 1,
            self.pre_1: 2, self.pre_2: 2,
            self.ml_1: 3, self.ml_2: 3,
            self.settings_1: 4, self.settings_2: 4,
        }
        for button, index in page_map.items():
            button.clicked.connect(lambda _, idx=index: self.stackedWidget.setCurrentIndex(idx))

    def open_csv(self):
        """Handle the process of opening a CSV file and saving it to the dataset folder."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options
        )

        if file_path:
            try:
                df = pd.read_csv(file_path, encoding='latin1')
                self.update_table_widget(df)
                self.show_file_opened_message(file_path)

                if self.confirmation_savefile(file_path) == QMessageBox.Yes:
                    save_path = os.path.join(os.getcwd(), 'process')
                    os.makedirs(save_path, exist_ok=True)
                    new_file_path = os.path.join(save_path, "dataset.csv")
                    df.to_csv(new_file_path, index=False)
                    print(f"File saved to {new_file_path}")
                else:
                    print("File not saved.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file: {e}")

    def show_wordcloud(self):
        """Generate and display a WordCloud from the preprocessed data."""
        process_dir = os.path.join(os.getcwd(), 'process')
        os.makedirs(process_dir, exist_ok=True)

        file_path = os.path.join(process_dir, 'Hasil-Preprocessing-Data-Steamming.csv')
        df = pd.read_csv(file_path)
        all_words = ' '.join([str(tweet) for tweet in df['result-preprocessing']])

        wordcloud = WordCloud(
            width=800, height=600, background_color='black', colormap='Blues_r',
            collocations=False, stopwords=STOPWORDS
        ).generate(all_words)

        save_path = os.path.join(process_dir, 'wordcloud.png')
        wordcloud.to_file(save_path)
        print(f"WordCloud saved to {save_path}")

        pixmap = QPixmap(save_path)
        self.wordcloud_label.setPixmap(pixmap)
        self.wordcloud_label.setScaledContents(True)

        label_percentage, total_data = plot_sentiment_distribution(file_path)
        sentiment_image_path = os.path.join(process_dir, 'sentiment_distribution.png')
        sentiment_pixmap = QPixmap(sentiment_image_path)
        self.distsentiment_label.setPixmap(sentiment_pixmap)
        self.distsentiment_label.setScaledContents(True)

        label_analysis_text = "Persentase Sentimen:\n"
        for label, percentage in label_percentage.items():
            label_analysis_text += f"{label}: {percentage:.2f}%\n"
        label_analysis_text += f"\nDari {total_data} data"

        self.label_analysis.setText(label_analysis_text)

    def do_preprocessing(self):
        """Perform data preprocessing and display progress."""
        dataset_path = os.path.join(os.getcwd(), 'process', 'dataset.csv')

        if os.path.exists(dataset_path):
            progress = self.show_progress_dialog("Processing...", "Preprocessing data... Please wait.")

            if progress:
                translated_file_path = run_preprocessing_cleanning(dataset_path)
                progress.close()
                self.confirmation_proccess_done(translated_file_path)
        else:
            QMessageBox.critical(self, "Error", "Dataset file not found. Please load a dataset first.")

    def display_preprocessing_results(self, file_path, table_widget):
        """Display preprocessing results in the specified table widget."""
        df = pd.read_csv(file_path)
        table_widget.clear()
        table_widget.setColumnCount(len(df.columns))
        table_widget.setHorizontalHeaderLabels(df.columns)
        table_widget.setRowCount(len(df))

        for row_index, row in df.iterrows():
            for col_index, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table_widget.setItem(row_index, col_index, item)
        
        print(f"Preprocessing results displayed in {table_widget.objectName()}")

    def update_table_widget(self, df):
        """Update the table widget with data from a DataFrame."""
        self.datasetview_table.clear()
        self.datasetview_table.setColumnCount(len(df.columns))
        self.datasetview_table.setHorizontalHeaderLabels(df.columns)
        self.datasetview_table.setRowCount(len(df))

        for row_index, row in df.iterrows():
            for col_index, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.datasetview_table.setItem(row_index, col_index, item)

    # Drag and Drop Support
    def dragEnterEvent(self, event):
        """Handle drag enter event for CSV files."""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        """Handle file drop event."""
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

    # Utility Methods
    def confirmation_savefile(self, file_path):
        """Show confirmation dialog to save file."""
        file_name = os.path.basename(file_path)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText(
        f"Do you want to save the file '{file_name}' to the dataset folder & continue preprocessing?\n\n"
        "If yes, please click the 'Preprocessing' button in the top-right corner to proceed."
    )
        msg_box.setWindowTitle("Save File")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        return msg_box.exec()

    def show_file_opened_message(self, file_path):
        """Show a message when a file is successfully opened."""
        file_name = os.path.basename(file_path)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"File '{file_name}' has been opened successfully.")
        msg_box.setWindowTitle("File Opened")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def confirmation_proccess_done(self, file_path):
        """Show a message when preprocessing is complete."""
        file_name = os.path.basename(file_path)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(f"Preprocessing complete. Data has been saved to:\n{file_name}")
        msg_box.setWindowTitle("Processing Complete")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def show_progress_dialog(self, title, label_text):
        """Show a progress dialog."""
        progress = QProgressDialog(title, "Cancel", 0, 0, self)
        progress.setWindowModality(Qt.ApplicationModal)
        progress.setCancelButton(None)
        progress.setMinimumDuration(0)
        progress.setValue(0)
        progress.setLabelText(label_text)
        progress.setStyleSheet("""
            QProgressDialog { color: black; }
            QProgressBar { color: black; }
            QLabel { color: black; }
        """)
        return progress
