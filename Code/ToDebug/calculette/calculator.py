import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# --- Configuration ---
class Style:
    COLOR_BACKGROUND = "#1c1c1c"
    COLOR_DISPLAY_BG = "#1c1c1c"
    COLOR_DISPLAY_FG = "#ffffff"
    
    COLOR_BTN_BG_NUM = "#505050"
    COLOR_BTN_FG_NUM = "#ffffff"
    COLOR_BTN_HOVER_NUM = "#6a6a6a"

    COLOR_BTN_BG_OP = "#ff9500"
    COLOR_BTN_FG_OP = "#ffffff"
    COLOR_BTN_HOVER_OP = "#ffab3e"

    COLOR_BTN_BG_MISC = "#d4d4d2"
    COLOR_BTN_FG_MISC = "#1c1c1c"
    COLOR_BTN_HOVER_MISC = "#e8e8e8"

    FONT_DISPLAY = QFont("Helvetica", 48, QFont.Bold)
    FONT_BUTTON = QFont("Helvetica", 20, QFont.Bold)

# --- Graphing Window ---
class GraphingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Grapher")
        self.setGeometry(150, 150, 600, 600)
        self.setStyleSheet(f"background-color: {Style.COLOR_BACKGROUND};")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.create_widgets()

    def create_widgets(self):
        input_layout = QHBoxLayout()
        
        self.function_entry = QLineEdit()
        self.function_entry.setFont(Style.FONT_BUTTON)
        self.function_entry.setStyleSheet(f"background-color: {Style.COLOR_BTN_BG_NUM}; color: {Style.COLOR_DISPLAY_FG}; border: none; padding: 5px;")
        input_layout.addWidget(self.function_entry)

        plot_button = QPushButton("Plot")
        plot_button.setFont(Style.FONT_BUTTON)
        plot_button.setStyleSheet(f"background-color: {Style.COLOR_BTN_BG_OP}; color: {Style.COLOR_BTN_FG_OP}; border: none; padding: 5px;")
        plot_button.clicked.connect(self.plot_function)
        input_layout.addWidget(plot_button)

        self.layout.addLayout(input_layout)

        self.fig = plt.figure(figsize=(5, 4), dpi=100, facecolor=Style.COLOR_BACKGROUND)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)

    def plot_function(self):
        function_str = self.function_entry.text()
        if not function_str:
            return

        try:
            x = np.linspace(-10, 10, 400)
            safe_dict = {"x": x, "np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan, "sqrt": np.sqrt}
            y = eval(function_str, {"__builtins__": {}}, safe_dict)

            self.ax.clear()
            self.ax.plot(x, y, color=Style.COLOR_BTN_BG_OP)
            self.ax.grid(True, linestyle='--', color='#404040')
            self.ax.set_title(f"Graph of f(x) = {function_str}", color='white')
            self.ax.set_xlabel("x", color='white')
            self.ax.set_ylabel("f(x)", color='white')
            self.canvas.draw()
        except Exception as e:
            self.ax.clear()
            self.ax.text(0.5, 0.5, f"Error: {e}", ha='center', va='center', color='red')
            self.canvas.draw()

# --- Main Application ---
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculette")
        self.setGeometry(100, 100, 350, 550)
        self.setStyleSheet(f"background-color: {Style.COLOR_BACKGROUND};")

        self.expression = ""
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.create_widgets()

    def create_widgets(self):
        self.display = QLineEdit()
        self.display.setFont(Style.FONT_DISPLAY)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(f"background-color: {Style.COLOR_DISPLAY_BG}; color: {Style.COLOR_DISPLAY_FG}; border: none;")
        self.display.setText("0")
        self.layout.addWidget(self.display)

        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        buttons = [
            ('C', 0, 0, Style.COLOR_BTN_BG_MISC, self.clear), ('Graph', 0, 1, Style.COLOR_BTN_BG_MISC, self.open_graphing_window), ('%', 0, 2, Style.COLOR_BTN_BG_MISC, self.percentage), ('/', 0, 3, Style.COLOR_BTN_BG_OP, lambda: self.append_operator('/')),
            ('7', 1, 0, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('7')), ('8', 1, 1, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('8')), ('9', 1, 2, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('9')), ('*', 1, 3, Style.COLOR_BTN_BG_OP, lambda: self.append_operator('*')),
            ('4', 2, 0, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('4')), ('5', 2, 1, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('5')), ('6', 2, 2, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('6')), ('-', 2, 3, Style.COLOR_BTN_BG_OP, lambda: self.append_operator('-')),
            ('1', 3, 0, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('1')), ('2', 3, 1, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('2')), ('3', 3, 2, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('3')), ('+', 3, 3, Style.COLOR_BTN_BG_OP, lambda: self.append_operator('+')),
            ('0', 4, 0, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('0'), 1, 2), ('.', 4, 2, Style.COLOR_BTN_BG_NUM, lambda: self.append_number('.')), ('=', 4, 3, Style.COLOR_BTN_BG_OP, self.calculate)
        ]

        for btn_text, row, col, color, cmd, *args in buttons:
            button = QPushButton(btn_text)
            button.setFont(Style.FONT_BUTTON)
            button.setStyleSheet(f"background-color: {color}; color: {Style.COLOR_BTN_FG_NUM if color == Style.COLOR_BTN_BG_NUM else Style.COLOR_BTN_FG_OP if color == Style.COLOR_BTN_BG_OP else Style.COLOR_BTN_FG_MISC}; border: none; padding: 10px;")
            button.clicked.connect(cmd)
            if args:
                grid_layout.addWidget(button, row, col, args[0], args[1])
            else:
                grid_layout.addWidget(button, row, col)

    def open_graphing_window(self):
        self.graphing_window = GraphingWindow()
        self.graphing_window.show()

    def update_display(self):
        if self.expression == "":
            self.display.setText("0")
        else:
            self.display.setText(self.expression)

    def append_number(self, number):
        self.expression += number
        self.update_display()

    def append_operator(self, operator):
        if self.expression and self.expression[-1] not in "+-*/":
            self.expression += operator
            self.update_display()

    def clear(self): 
        self.expression = ""
        self.update_display()

    def calculate(self):
        try:
            expression_to_eval = self.expression.replace('%', '/100')
            result = str(eval(expression_to_eval))
            self.expression = result
        except (SyntaxError, ZeroDivisionError):
            self.expression = "Error"
        self.update_display()

    def percentage(self):
        if self.expression:
            try:
                result = str(eval(self.expression) / 100)
                self.expression = result
            except (SyntaxError, ZeroDivisionError):
                self.expression = "Error"
            self.update_display()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())