from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.candidate1_count = 0
        self.candidate2_count = 0
        self.candidate3_count = 0

        self.pushButton.clicked.connect(self.vote_candidate1)
        self.pushButton_2.clicked.connect(self.vote_candidate2)
        self.pushButton_3.clicked.connect(self.vote_candidate3)
        self.pushButton_4.clicked.connect(self.exit_voting)

        self.update_vote_counts()

    def vote_candidate1(self):
        self.candidate1_count += 1
        self.update_vote_counts()

    def vote_candidate2(self):
        self.candidate2_count += 1
        self.update_vote_counts()

    def vote_candidate3(self):
        self.candidate3_count += 1
        self.update_vote_counts()

    def update_vote_counts(self):
        self.label_10.setText(f"Bianca: {self.candidate1_count}")
        self.label_11.setText(f"Edward: {self.candidate2_count}")
        self.label_12.setText(f"Felicia: {self.candidate3_count}")

    def exit_voting(self):
        print(
            f'Bianca - {self.candidate1_count}, Edward - {self.candidate2_count}, Felicia - {self.candidate3_count}, '
            f'Total - {self.candidate1_count + self.candidate2_count + self.candidate3_count}')
        sys.exit()
