from asteroids_model import Game
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt,QTimer
 
N_COLUMNS = 4
N_ROWS = 7

game = Game(N_COLUMNS, N_ROWS)
 
class GridApp(QWidget):
    def __init__(self):
        super().__init__()
        self.COLUMNS = N_COLUMNS
        self.ROWS = N_ROWS
        self.CELL_WIDTH = 70
        self.SPACING = 5
        self.COL_BACKGROUND = QColor("black")
        self.COL_CELL_DEFAULT = QColor("white")
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(500)  # Trigger the checkSomething function every ... milliseconds
 
    def initUI(self):
        self.setWindowTitle('Grid App')
        layout = QVBoxLayout()
        self.setLayout(layout)
        grid = QWidget()
        grid.setStyleSheet("QWidget {{ background-color: {0}; }}".format(self.COL_BACKGROUND.name()))
        grid_layout = QVBoxLayout(grid)
        grid_layout.setSpacing(self.SPACING)
        layout.addWidget(grid)
 
        self.cells = []  # Store references to the cell widgets
 
        for y in range(self.ROWS):
            row_layout = QHBoxLayout()
            grid_layout.addLayout(row_layout)
            for x in range(self.COLUMNS):
                cell = QLabel()
                cell.setFixedSize(self.CELL_WIDTH,self.CELL_WIDTH)
                cell.setStyleSheet("background-color: {}".format(self.COL_CELL_DEFAULT.name()))
                row_layout.addWidget(cell)
                self.cells.append(cell)
 
        self.show()
        self.setFixedSize(self.size().width(),self.size().height()) # -> window non-resizable
 
    def draw_cell_at_position(self,x,y,color):
        """
        changes color of cell at given position
        """ 
        cell = self.cells[y*self.COLUMNS + x]
        cell.setStyleSheet("background-color: {}".format(color.name()))
 
    def draw_all_cells(self):
        for y in range(self.ROWS):
            for x in range(self.COLUMNS):
                rnd_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                self.draw_cell_at_position(x,y,rnd_color)

 
    def keyPressEvent(self, event):
        """
        deals with keypressed events
        """
        key = event.key()
        if key == Qt.Key_Up:
            game.player.update(True)
        elif key == Qt.Key_Down:
            game.player.update(False)
        self.draw_all_cells()
 
    def update(self):
        # Perform your periodic check here
        # This function will be called every ... ms (value in self.timer.start(...))
        # Update the necessary data or trigger actions as needed
        for asteroid in game.asteroids:
            GridApp.draw_cell_at_position(asteroid.x, asteroid.y, QColor("red"))
        GridApp.draw_cell_at_position(game.player.x, game.player.y, QColor("green"))
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    grid_app = GridApp()
    sys.exit(app.exec_())
