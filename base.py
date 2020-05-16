from PyQt5.QtWidgets import QWidget, QApplication

class Form(QWidget):
  def __init__(self, parent=None):
    QWidget.__init__(self, parent)
    self.setGeometry(0, 0, 300, 300)

if __name__ == "__main__":
    app = QApplication([])
    form = Form()
    form.show()
    app.exec_()