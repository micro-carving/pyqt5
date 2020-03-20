import sys

# 当导入ui转换成的py文件时，会提示红色下划线，解决方式为：选择该py文件的当前目录，右击Mark Directory as选择Sources Root即可
import GridLayout

from PyQt5.QtWidgets import QApplication, QMainWindow

# if __name__ == '__main__':

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = GridLayout.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())