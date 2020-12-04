from PyQt5.QtCore import QThread


class Thread(QThread):
    def __init__(self):
        super(Thread, self).__init__()

    def run(self):
        num = 0
        while True:
            num = num + 1
            print(num)
            Thread.sleep(1)
            if num == 10:
                Thread.quit()


if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    thread = Thread()
    thread.start()
    sys.exit(app.exec_())
