import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    qw = QWidget()
    # 设置窗口的大小
    qw.resize(400, 200)
    # 移动窗口
    qw.move(300, 300)
    # 设置窗口的标题
    qw.setWindowTitle('第一个基于PyQt5的桌面应用')
    # 显示窗口
    qw.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
