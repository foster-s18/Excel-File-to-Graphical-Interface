import client
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QCompleter, QTextEdit, QTableWidget
from PyQt5.QtCore import Qt
from breaks import breaks
from notes import notes

client_list, data_dict = client.client()
breaks = breaks()
notes = notes()


class UiMainWindow(object):
    def __init__(self):
        self.main_background = None
        self.logo = None
        self.statusbar = None
        self.model = None
        self.notes_text = None
        self.tab_3 = None
        self.break_table = None
        self.tab_2 = None
        self.shift_text = None
        self.tab_1 = None
        self.tabWidget = None
        self.clear_button = None
        self.dropdown = None
        self.main_widget = None

    def setup_ui(self, main_window):

        # main window settings
        main_window.setObjectName("MainWindow")
        main_window.setFixedSize(980, 660)
        self.main_widget = QtWidgets.QWidget(main_window)
        self.main_widget.setObjectName("main_widget")

        # default font settings
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(False)

        # dropdown (combobox) settings
        self.dropdown = QtWidgets.QComboBox(self.main_widget)
        self.dropdown.setGeometry(QtCore.QRect(150, 20, 500, 30))
        self.dropdown.addItem("Select Client....")
        self.dropdown.addItems(client_list)
        self.dropdown.setFont(font)
        self.dropdown.setEditable(True)
        self.dropdown.setInsertPolicy(QtWidgets.QComboBox.NoInsert)

        # Connect the ComboBox's currentIndexChanged signal to the handler method
        self.dropdown.currentIndexChanged.connect(self.perform_search)

        # searchbar auto complete
        completer = QCompleter(client_list)
        completer.setCaseSensitivity(False)
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        self.dropdown.setCompleter(completer)

        # Connect the QLineEdit's return key signal to perform_search method
        self.dropdown.lineEdit().returnPressed.connect(self.perform_search)

        # clear button settings
        self.clear_button = QtWidgets.QPushButton(self.main_widget)
        self.clear_button.setGeometry(QtCore.QRect(350, 70, 100, 30))
        self.clear_button.setFont(font)
        self.clear_button.setStyleSheet(
            """QPushButton {
                background-color: lightgrey;
                border: 1px solid;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FFD700;
                color: black;
                border: 1px solid;
                border-radius: 5px;
            }""")
        self.clear_button.setFocus()
        self.clear_button.clicked.connect(self.clear_result)
        self.clear_button.setObjectName("clear_button")

        # tab widget settings
        self.tabWidget = QtWidgets.QTabWidget(self.main_widget)
        self.tabWidget.setGeometry(QtCore.QRect(150, 140, 700, 480))
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(
            "QTabBar::tab {"
            "background: lightgrey;"
            "color: #000000;"
            "padding: 5px;"
            "border: 1px solid grey;"
            "border-top-left-radius: 5px;"
            "border-top-right-radius: 5px;"
            "margin-top: 0px;"
            "}"
            "QTabBar::tab:selected {"
            "background: #FFD700;"
            "color: #000000;"
            "}""")
        self.tabWidget.setObjectName("tabWidget")

        # shift information tab 1 settings
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tabWidget.addTab(self.tab_1, "")
        self.shift_text = QTextEdit(self.tab_1)
        self.shift_text.setGeometry(QtCore.QRect(0, 0, 700, 480))
        self.shift_text.setReadOnly(True)
        self.shift_text.setFont(font)
        self.shift_text.setObjectName("shift_text")
        self.shift_text.setText("No Results.")
        self.shift_text.setStyleSheet(
            """QTextEdit {
                border: 1px solid grey;
            }""")

        # breaks table tab 2 settings
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.break_table = QtWidgets.QTableView(self.tab_2)
        self.break_table.setGeometry(QtCore.QRect(0, 0, 694, 435))
        self.break_table.horizontalHeader().setStyleSheet(
            """QHeaderView::section {
                background-color: rgba(0, 0, 76, 255);
                color: white;
                border: 1px solid grey;
            }
                QHeaderView::section:hover {
                background-color: rgba(0, 0, 76, 255);
            }""")
        self.break_table.setSelectionMode(QTableWidget.NoSelection)
        self.break_table.setStyleSheet(
            """QTextEdit{
                border: 1px solid grey;
            }""")
        self.break_table.setFont(font)
        self.break_table.horizontalHeader().setFont(font)
        # Set up table model
        self.model = QtGui.QStandardItemModel(self.break_table)
        self.break_table.setModel(self.model)
        # Set stretch for columns to fit content
        self.break_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # remove row numbers on table
        self.break_table.verticalHeader().setVisible(False)
        # make table values un-selectable
        self.break_table.setFocusPolicy(Qt.NoFocus)
        self.populate_table("Select Client....")
        self.break_table.setObjectName("break_table")

        # notes information tab 3 settings
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.notes_text = QTextEdit(self.tab_3)
        self.notes_text.setGeometry(QtCore.QRect(0, 0, 694, 435))
        self.notes_text.setReadOnly(True)
        self.notes_text.setFont(font)
        self.notes_text.setText("No Notes.")
        self.notes_text.setStyleSheet(
            """QTextEdit {
                border: 1px solid grey;
            }""")
        self.notes_text.setObjectName("notes_text")

        # main background settings
        self.main_background = QtWidgets.QLabel(self.main_widget)
        self.main_background.setGeometry(QtCore.QRect(0, 0, 1271, 771))
        self.main_background.setStyleSheet(
            "background-color: qconicalgradient(cx:1, cy:1, angle:218.5, "
            "stop:0.738636 rgba(0, 0, 76, 255), stop:1 rgba(255, 255, 255, 255));")
        self.main_background.setText("")
        self.main_background.setObjectName("main_background")

        # company logo settings
        self.logo = QtWidgets.QLabel(self.main_widget)
        self.logo.setGeometry(QtCore.QRect(20, 15, 90, 110))
        self.logo.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(""))  # put logo in GUI
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        # bottom statusbar settings
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.setObjectName("statusbar")
        # Show version number in the status bar
        self.statusbar.showMessage("Version 1.0.0")


        # display objects
        self.main_background.raise_()
        self.dropdown.raise_()
        self.clear_button.raise_()
        self.tabWidget.raise_()
        self.logo.raise_()

        MainWindow.setCentralWidget(self.main_widget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.translate_ui(MainWindow)

    def translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Client Information"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate(
            "MainWindow", "Shift Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate(
            "MainWindow", "Break Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate(
            "MainWindow", "           Notes           "))

    def perform_search(self):
        query = self.dropdown.currentText()
        found = False

        for x in client_list:
            if x == query:
                found = True
                self.populate_client_info(query)
                self.populate_notes(query)
                self.populate_table(query)
        if not found:
            self.clear_result()

    def populate_client_info(self, data):
        prefix = ["Grade: ", "Male / Female: ", "ETC: ", "MBCAPI: ",  "RGN Day-shift: ", "RGN Night-shift: ",
                  "Day-shift: ", "Night-shift: ", "Morning-shift: ", "Afternoon-shift: ", "Twilight-shift: "]
        result_text = ""
        query = data
        client_info = data_dict[query]
        result_text += f"Client:    {query}\n"
        for prefix, data in zip(prefix, client_info):
            result_text += f"{prefix}   {data}\n"
        self.shift_text.setText(result_text)

    def populate_table(self, data):
        self.model.clear()
        query = data
        self.model.setHorizontalHeaderLabels(['Shift length (hours)', 'Break Length (minutes)'])
        # Sample data to populate the table
        hours = ["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

        if query in breaks and breaks[query]:
            for x, y in zip(hours, breaks[query]):
                # Convert Hours/Breaks to QStandardItem to display in table &
                # center content in cell and make non-editable
                hours_worked = QtGui.QStandardItem(x)
                hours_worked.setTextAlignment(Qt.AlignCenter)
                hours_worked.setEditable(False)
                min_break = QtGui.QStandardItem(y)
                min_break.setTextAlignment(Qt.AlignCenter)
                min_break.setEditable(False)
                self.model.appendRow([hours_worked, min_break])

        else:
            if query == "Select Client....":
                default = QtGui.QStandardItem(f"Please select a client.")
                self.model.appendRow([default])
            else:
                no_data = QtGui.QStandardItem(f"No data found for {query}.")
                update_message = QtGui.QStandardItem("Please update excel breaks information.")
                self.model.appendRow([no_data, update_message])

    def populate_notes(self, data):
        # Clear the current model (table data) as it may change
        self.model.clear()
        query = data  # Store the client name or query for processing

        # Check if the query exists in the notes dictionary and if it has associated notes
        if query in notes and notes[query]:
            notes_info = notes[query]  # Retrieve notes for the specific client
            self.notes_text.setText(notes_info)  # Display the notes in the text area
        else:
            # If there are no notes for the selected client, display a default message
            self.notes_text.setText("No Notes.")

    def clear_result(self):
        # Reset the dropdown selection to the default option
        self.dropdown.setCurrentIndex(0)
        self.model.clear()  # Clear any data in the model (table view)
        self.shift_text.setText("No Results.")  # Reset the shift information display
        self.notes_text.setText("No Notes.")  # Reset the notes display
        self.populate_table("Select Client....")  # Repopulate the table with a default message

if __name__ == "__main__":
    import sys  # Import the system module to handle system-level operations

    # Create an instance of the QApplication class, which manages the GUI application
    app = QtWidgets.QApplication(sys.argv)
    # Create the main window of the application
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()  # Instantiate the user interface class
    ui.setup_ui(MainWindow)  # Set up the UI components in the main window
    MainWindow.show()  # Show the main window
    sys.exit(app.exec_())  # Execute the application and wait for it to finish

