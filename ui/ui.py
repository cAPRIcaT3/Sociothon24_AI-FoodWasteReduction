from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, \
    QPushButton, QFileDialog
import pandas as pd


class MainUI(QMainWindow):
    def __init__(self, gemini_handler):
        super().__init__()
        self.gemini_handler = gemini_handler
        self.setWindowTitle('Inventory Management')
        self.setGeometry(100, 100, 1000, 600)  # Increased width to accommodate the new button

        # Create table widget
        self.table = QTableWidget()
        self.table.setColumnCount(6)  # Updated number of columns to match the dataset and new button
        self.table.setHorizontalHeaderLabels(
            ['Item', 'Quantity', 'Expiration Date', 'Days Remaining', 'Action', 'Generate Response'])

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

            # Add a button to generate response
            response_button = QPushButton("Generate Response")
            # Pass data directly to avoid lambda issues
            response_button.clicked.connect(
                self.create_response_callback(row['Item'], row['Quantity'], row['Days Remaining']))
            self.table.setCellWidget(i, 5, response_button)

    def get_action(self, days_remaining):
        if days_remaining <= 0:
            return "Expired"
        elif days_remaining <= 3:
            return "Use Immediately"
        elif days_remaining <= 7:
            return "Use Soon"
        else:
            return "In Stock"

    def create_response_callback(self, item, quantity, days_remaining):
        # Returns a function that calls generate_response with the provided parameters
        def callback():
            self.generate_response(item, quantity, days_remaining)

        return callback

    def generate_response(self, item, quantity, days_remaining):
        # Generate idea based on item data
        response = self.gemini_handler.generate_idea(item, quantity, days_remaining)
        print(f"Response for {item}: {response}")  # Display response in console (can be updated to show in UI)

