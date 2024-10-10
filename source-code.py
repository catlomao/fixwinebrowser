import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  # Import QUrl

class SimpleBrowser(QMainWindow):
    def __init__(self, initial_url=None):
        super().__init__()

        # Set up the main window
        self.setWindowTitle('Simple PyQt Browser')
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a vertical layout
        self.layout = QVBoxLayout(self.central_widget)

        # Create the URL input field
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText('Enter URL and press Enter...')
        self.url_input.returnPressed.connect(self.load_url)

        # Create the web view
        self.web_view = QWebEngineView(self)

        # Add widgets to the layout
        self.layout.addWidget(self.url_input)
        self.layout.addWidget(self.web_view)

        # Load initial URL if provided
        if initial_url:
            self.url_input.setText(initial_url)
            self.load_url()

    def load_url(self):
        # Get the URL from the input field and load it in the web view
        url = self.url_input.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        # Convert string URL to QUrl
        self.web_view.setUrl(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Get URL from command line arguments
    initial_url = sys.argv[1] if len(sys.argv) > 1 else None

    browser = SimpleBrowser(initial_url)
    browser.show()
    sys.exit(app.exec_())
