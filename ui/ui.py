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
        self.table.setColumnCount(5)  # Updated number of columns to match dataset
        self.table.setHorizontalHeaderLabels(['Item', 'Quantity', 'Expiration Date', 'Days Remaining', 'Action'])

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
        # Check the data being passed
        print("Data being loaded into table:\n", data)
        self.table.setRowCount(len(data))
        for i, row in data.iterrows():
            self.table.setItem(i, 0, QTableWidgetItem(row['Item']))
            self.table.setItem(i, 1, QTableWidgetItem(str(row['Quantity'])))
            self.table.setItem(i, 2, QTableWidgetItem(row['Expiration Date'].strftime('%Y-%m-%d')))
            self.table.setItem(i, 3, QTableWidgetItem(str(row['Days Remaining'])))
            self.table.setItem(i, 4, QTableWidgetItem(self.get_action(row['Days Remaining'])))

    def get_action(self, days_remaining):
        if days_remaining <= 0:
            return "Expired"
        elif days_remaining <= 3:
            return "Use Immediately"
        elif days_remaining <= 7:
            return "Use Soon"
        else:
            return "In Stock"
