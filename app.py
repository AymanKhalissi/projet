from CheckId import is_valid_id_card
from utils import extract_address, compare_addresses
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QFileDialog, QWidget, QMessageBox, QProgressBar
)
from PySide6.QtCore import QTimer


class AddressVerificationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Address Verification App")
        self.setGeometry(100, 100, 600, 400)

        # Main container
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Labels
        self.label_status = QLabel("Load an ID image to start validation.")
        self.layout.addWidget(self.label_status)

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.layout.addWidget(self.progress_bar)

        # Buttons
        self.btn_load_cin = QPushButton("Load CIN Image")
        self.btn_load_cin.clicked.connect(self.load_cin_image)
        self.layout.addWidget(self.btn_load_cin)

        self.btn_load_facture = QPushButton("Load Facture Image")
        self.btn_load_facture.setEnabled(False)
        self.btn_load_facture.clicked.connect(self.load_facture_image)
        self.layout.addWidget(self.btn_load_facture)

        # File paths
        self.cin_path = None
        self.facture_path = None
        self.template_path = "cin1.jpg"  # Replace with your template file path

    def load_cin_image(self):
        self.cin_path, _ = QFileDialog.getOpenFileName(self, "Select CIN Image", "", "Images (*.png *.jpg *.jpeg)")
        if self.cin_path:
            self.label_status.setText("Validating CIN image...")
            try:
                if is_valid_id_card(self.cin_path, self.template_path, threshold=0.7):
                    QMessageBox.information(self, "Validation", "The CIN is valid.")
                    self.label_status.setText("CIN image validated successfully.")
                    self.btn_load_facture.setEnabled(True)
                else:
                    QMessageBox.warning(self, "Validation Failed", "The CIN image is NOT valid.")
                    self.label_status.setText("Invalid CIN image.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def load_facture_image(self):
        self.facture_path, _ = QFileDialog.getOpenFileName(self, "Select Facture Image", "", "Images (*.png *.jpg *.jpeg)")
        if self.facture_path:
            QMessageBox.information(self, "Facture Loaded", "The facture image has been loaded.")
            self.label_status.setText("Facture image loaded successfully.")
            self.compare_addresses_action()

    def update_progress(self, value, message):
        """Update the progress bar value and status message."""
        self.progress_bar.setValue(value)
        self.label_status.setText(message)
        QApplication.processEvents()  # Ensure UI updates immediately

    def compare_addresses_action(self):
        try:
            # Step 1: Start Address Extraction
            self.update_progress(10, "Extracting CIN address...")
            cin_address = extract_address(self.cin_path)

            self.update_progress(50, "Extracting Facture address...")
            facture_address = extract_address(self.facture_path)

            # Step 2: Compare Addresses
            self.update_progress(80, "Comparing addresses...")
            if compare_addresses(cin_address, facture_address):
                QMessageBox.information(self, "Comparison Result", "The addresses are identical or sufficiently similar.")
            else:
                QMessageBox.warning(self, "Comparison Result", "The addresses are NOT identical.")

            self.update_progress(100, "Comparison complete.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.update_progress(0, "Error occurred during comparison.")


if __name__ == "__main__":
    app = QApplication([])
    window = AddressVerificationApp()
    window.show()
    app.exec()