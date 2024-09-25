from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, \
    QPushButton, QFileDialog
import pandas as pd


class MainUI(QMainWindow):
    def __init__(self, gemini_handler):
        super().__init__()
        self.gemini_handler = gemini_handler
        self.setWindowTitle('Inventory Management')
        self.setGeometry(100, 100, 800, 600)

        # Create table widget
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Adjust the number of columns as needed
        self.table.setHorizontalHeaderLabels(['Item', 'Quantity', 'Expiration Date', 'Days Remaining'])

        # Add a button for uploading Excel file
        self.upload_button = QPushButton('Upload Excel File')
        self.upload_button.clicked.connect(self.upload_excel_file)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.upload_button)
        layout.addWidget(self.table)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def upload_excel_file(self):
        # Open file dialog to select Excel file
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            # Read the data using the gemini handler
            data = self.gemini_handler.get_inventory_data_from_excel(file_path)
            if data is not None:
                self.load_data_into_table(data)
            else:
                print("Failed to load data from Excel file.")

    def load_data_into_table(self, data):
        self.table.setRowCount(len(data))
        for i, row in data.iterrows():
            self.table.setItem(i, 0, QTableWidgetItem(row['Item']))
            self.table.setItem(i, 1, QTableWidgetItem(str(row['Quantity'])))
            self.table.setItem(i, 2, QTableWidgetItem(row['Expiration Date'].strftime('%Y-%m-%d')))
            self.table.setItem(i, 3, QTableWidgetItem(str(row['Days Remaining'])))
