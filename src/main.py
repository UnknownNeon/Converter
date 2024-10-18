from PyQt6.QtWidgets import QApplication , QWidget
from PyQt6.QtWidgets import QTextEdit , QComboBox , QPushButton , QLabel , QHBoxLayout ,QVBoxLayout
from dict_1 import * 
import subprocess
import os

class Home(QWidget):

    def __init__(self):
        super().__init__()
        #self.setup_exe("Hellow World")
        self.init_ui()
        self.settings()

    def init_ui(self):

        self.input_box_1 = QTextEdit()
        self.output_box_1 = QTextEdit()
        
        self.calculate_output = QPushButton("Convert")
        self.calculate_output.clicked.connect(self.convert_click)
        
        self.option_1 = QComboBox()
        self.option_1_label = QLabel("From : " )
        self.option_2 = QComboBox()
        self.option_2_label = QLabel("To : Decimal Only for now" )

        self.option_1.addItems(index_1)
        self.option_2.addItems(["decimal"])

        self.title = QLabel("Hellow World ")

        self.master_layout = QHBoxLayout()

        col_1 = QVBoxLayout()
        col_2 = QVBoxLayout()

        col_1_subcontainer_header = QVBoxLayout()
        col_1_subcontainer_footer = QVBoxLayout()
        

        col_1_subcontainer_header.addWidget(self.title)

        col_1_subcontainer_footer.addWidget(self.calculate_output ,30)
        col_1_subcontainer_footer.addWidget(self.option_1_label, 10)
        col_1_subcontainer_footer.addWidget(self.option_1 ,25)
        col_1_subcontainer_footer.addWidget(self.option_2_label , 10)
        col_1_subcontainer_footer.addWidget(self.option_2 ,25)

        #main Layout : 
        col_1.addLayout(col_1_subcontainer_header , 1)
        col_1.addLayout(col_1_subcontainer_footer , 9)

        col_2.addWidget(self.input_box_1)
        col_2.addWidget(self.output_box_1)

        self.master_layout.addLayout(col_1,20)
        self.master_layout.addLayout(col_2,80)
        
        self.setLayout(self.master_layout)


    def settings(self):
        self.setWindowTitle("Converter ")
        self.setGeometry(300,300 , 800, 300 )

    #Button Events : 
    def button_events(self):
        pass

    def setup_exe(self, text, option_from , option_to):
        current_directory = os.getcwd()
        current_directory = os.path.join(current_directory, f"{option_from}-{option_to}.exe")
        print("Current " , current_directory)
        
        try:
             result = subprocess.run(
                  [current_directory, text],
                  stdout=subprocess.PIPE,      
                  stderr=subprocess.PIPE,      
                  text=True
             )
             print("Output:", result.stdout)
             print("Error:", result.stderr)

             return result.stdout
        
        except Exception as e:
             print("Exception",str(e))

    def convert_click(self):
         
         to_conver = self.input_box_1.toPlainText()
         selected_1 = self.option_1.currentText()
         selected_2 = self.option_2.currentText()

         text_converted = self.setup_exe(to_conver,selected_1,selected_2)

         self.output_box_1.setText(text_converted)


        

if __name__ in "__main__":
        app = QApplication([])
        main = Home()
        main.show()
        app.exec()
