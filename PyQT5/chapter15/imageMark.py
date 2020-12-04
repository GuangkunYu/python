# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageMark.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import os

from PIL import Image, ImageEnhance, ImageFont, ImageDraw
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontMetrics, QFontInfo
from PyQt5.QtWidgets import QApplication, QMainWindow, QFontDialog, QMessageBox, QFileDialog


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)    # 只显示关闭按钮
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 设置图片显示列表
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 256, 571))
        self.listWidget.setObjectName("listWidget")

        # 设置加载图片按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 60, 521, 191))
        self.groupBox.setObjectName("groupBox")
        # 设置文字水印单选按钮
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 115, 19))
        self.radioButton.setChecked(True)   # 默认选中
        self.radioButton.setObjectName("radioButton")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 70, 70, 21))
        self.label.setObjectName("label")

        # 设置要输入水印文字的文本框
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 310, 21))
        self.lineEdit.setObjectName("lineEdit")

        # 设置 字体设置 按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 70, 93, 21))
        self.pushButton_2.setObjectName("pushButton_2")

        # 设置图片水印单选按钮
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 110, 115, 19))
        self.radioButton_2.setChecked(False)  # 默认不选中
        self.radioButton_2.setObjectName("radioButton_2")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 70, 21))
        self.label_2.setObjectName("label_2")

        # 设置显示水印图片路径的文本框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 140, 310, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        # 设置 选择水印图片 按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 140, 93, 21))
        self.pushButton_3.setObjectName("pushButton_3")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 290, 521, 91))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 51, 21))
        self.label_3.setObjectName("label_3")

        # 设置水印透明度的滑动条
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(100, 40, 230, 22))
        self.horizontalSlider.setMaximum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(340, 40, 70, 21))
        self.label_4.setObjectName("label_4")

        # 设置水印位置选择框
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(420, 40, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['左上角', '右上角', '左下角', '右下角', '居中位置'])
        self.comboBox.setCurrentIndex(0)    # 设置默认选择第一项

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 409, 521, 91))
        self.groupBox_3.setObjectName("groupBox_3")

        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 70, 16))
        self.label_5.setObjectName("label_5")

        # 设置显示保存路径的文本框
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 40, 310, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        # 设置选择图片保存路径的按钮
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 40, 93, 21))
        self.pushButton_4.setObjectName("pushButton_4")

        # 设置执行按钮
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 540, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)

        # 设置状态栏
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        self.statusBar.showMessage('准备就绪......')    # 设置状态栏默认值
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # # 关联“加载图片”按钮的方法
        self.pushButton.clicked.connect(self.getFiles)
        # # 关联“字体设置”按钮的方法
        self.pushButton_2.clicked.connect(self.setFont)
        # # 关联“选择图片”按钮的方法
        self.pushButton_3.clicked.connect(self.setImg)
        # # 关联“选择保存路径”按钮的方法
        self.pushButton_4.clicked.connect(self.msg)
        # # 关联“执行”按钮的方法
        self.pushButton_5.clicked.connect(self.addMark)
        # # 关联列表单击方法，用来预览选中的图片
        self.listWidget.itemClicked.connect(self.itemClick)

    # 设置字体
    def setFont(self):
        self.waterfont, ok = QFontDialog.getFont()  # 显示字体对话框
        if ok:
            self.lineEdit.setFont(self.waterfont)   # 设置水印文字的字体
            self.fontSize = QFontMetrics(self.waterfont)    # 获取字体尺寸
            self.fontInfo = QFontInfo(self.waterfont)   # 获取字体信息

    # 是否为图片
    def isImg(self, file):
        file = file.lower()
        if file in ['.jpg', '.png', '.jpeg', '.bmp']:
            return True
        else:
            return False

    # 获取所有文件
    def getFiles(self):
        try:
            # 选择图片文件夹路径
            self.img_path = QFileDialog.getExistingDirectory(None, '选择图片文件夹路径', os.getcwd())
            self.list = os.listdir(self.img_path)   # 遍历选择的文件夹
            num = 0 # 记录图片数量
            self.listWidget.clear() # 清空列表项
            for i in range(0, len(self.list)):
                filepath = os.path.join(self.img_path, self.list[i])    # 记录遍历到的文件名
                if os.path.isfile(filepath):
                    imgType = os.path.splitext(filepath)[1] # 获取扩展名
                    if self.isImg(imgType):
                        num += 1
                        self.item = QtWidgets.QListWidgetItem(self.listWidget)  # 创建列表项
                        self.item.setText(self.list[i]) # 显示图片列表
            self.statusBar.showMessage(f'共有图片 {num} 张') # 显示图片总数
        except Exception as e:
            QMessageBox.warning(None, '警告', '请选择一个有效路径......', QMessageBox.Ok)

    # 预览图片
    def itemClick(self, item):
        os.startfile(self.img_path + "\\" + item.text())

    # 选择水印图片
    def setImg(self):
        try:
            # waterimg即为选择的水印图片，第二形参为对话框标题，第三个为对话框打开后默认的路径
            self.waterimg = QFileDialog.getOpenFileName(None, '选择水印图片', 'c:\\', '图片文件(*.jpeg;*.png;*.jpg;*.bmp)')
            self.lineEdit_2.setText(self.waterimg[0])   # 显示选择的水印图片
        except Exception as e:
            print(e)

    # 选择保存路径
    def msg(self):
        try:
            # dir_path即为选择的文件夹的绝对路径，第二个形参为对话框标题，第三个为对话框打开后的默认路径
            self.dir_path = QFileDialog.getExistingDirectory(None, '选择路径', os.getcwd())
            self.lineEdit_3.setText(self.dir_path)  # 显示选择的保存路径
        except Exception as e:
            print(e)

    # 文字水印
    def textMark(self, img, newImgPath):
        try:
            im = Image.open(img).convert('RGBA')  # 打开原始图片，并转换为RGBA
            newImg = Image.new('RGBA', im.size, (255, 255, 255, 0))  # 存储添加水印后的图片
            # 创建字体,说明：默认使用楷体，如果需要使用其他字体，需要将字体文件复制到当前目录中
            # 然后对下面第一个参数进行修改，可以使用self.fontInfo.family()动态获取字体名称，后面加扩展名即可
            font = ImageFont.truetype('simkai.ttf', self.fontInfo.pointSize())
            imagedraw = ImageDraw.Draw(newImg)  # 创建绘制对象
            imgwidth, imgheight = im.size  # 记录图片大小
            txtwidth = self.fontSize.maxWidth() * len(self.lineEdit.text())  # 获取字体宽度
            txtheight = self.fontSize.height()  # 获取字体高度

            # 设置水印文字位置
            if self.comboBox.currentText() == '左上角':
                position = (0, 0)
            elif self.comboBox.currentText() == '左下角':
                position = (0, imgheight - txtheight)
            elif self.comboBox.currentText() == '右上角':
                position = (imgwidth - txtwidth, 0)
            elif self.comboBox.currentText() == '右下角':
                position = (imgwidth - txtwidth, imgheight - txtheight)
            elif self.comboBox.currentText() == '居中位置':
                position = (imgwidth / 2, imgheight / 2)
            # 设置文本颜色
            imagedraw.text(position, self.lineEdit.text(), font=font, fill="#FCA454")
            # 设置透明度
            alpha = newImg.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(int(self.horizontalSlider.value()) / 10.0)
            newImg.putalpha(alpha)
            Image.alpha_composite(im, newImg).save(newImgPath)  # 保存图片
        except Exception:
            QMessageBox.warning(None, '错误', '图片格式有误，请重新选择......', QMessageBox.Ok)

    # 图片水印
    def imgMark(self, img, newImgPath):
        im = Image.open(img)  # 打开原始图片
        mark = Image.open(self.lineEdit_2.text())  # 打开水印图片
        rgbaim = im.convert('RGBA')  # 将原始图片转换为RGBA
        rgbamark = mark.convert('RGBA')  # 将水印图片转换为RGBA
        imgwidth, imgheight = rgbaim.size  # 获取原始图片尺寸
        nimgwidth, nimgheight = rgbamark.size  # 获取水印图片尺寸
        # 缩放水印图片
        scale = 10
        markscale = max(imgwidth / (scale * nimgwidth), imgheight / (scale * nimgheight))
        newsize = (int(nimgwidth * markscale), int(nimgheight * markscale))  # 计算新的尺寸大小
        rgbamark = rgbamark.resize(newsize, resample=Image.ANTIALIAS)  # 重新设置水印图片大小
        nimgwidth, nimgheight = rgbamark.size  # 获取水印图片缩放后的尺寸
        # 计算水印位置
        if self.comboBox.currentText() == '左上角':
            position = (0, 0)
        elif self.comboBox.currentText() == '左下角':
            position = (0, imgheight - nimgheight)
        elif self.comboBox.currentText() == '右上角':
            position = (imgwidth - nimgwidth, 0)
        elif self.comboBox.currentText() == '右下角':
            position = (imgwidth - nimgwidth, imgheight - nimgheight)
        elif self.comboBox.currentText() == '居中位置':
            position = (int(imgwidth / 2), int(imgheight / 2))
        # 设置透明度：img.point(function)接受一个参数，且对图片中的每一个点执行这个函数，这个函数是一个匿名函数，使用lambda表达式来完成
        # convert()函数，用于不同模式图像之间的转换，模式“L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
        # 在PIL中，从模式“RGB”转换为“L”模式是按照下面的公式转换的：L = R * 299/1000 + G * 587/1000+ B * 114/1000
        rgbamarkpha = rgbamark.convert("L").point(lambda x: x / int(self.horizontalSlider.value()))
        rgbamark.putalpha(rgbamarkpha)
        # 水印位置
        rgbaim.paste(rgbamark, position, rgbamarkpha)
        try:
            rgbaim.save(newImgPath)  # 保存水印图片
        except Exception:
            QMessageBox.warning(None, '错误', '请选择其他路径……', QMessageBox.Ok)

    # 添加水印
    def addMark(self):
        if self.lineEdit_3.text() == '':  # 判断是否选择了保存路径
            QMessageBox.warning(None, '警告', '请选择保存路径', QMessageBox.Ok)
            return
        else:
            num = 0  # 记录处理图片数量
            for i in range(0, self.listWidget.count()):  # 遍历图片列表
                # 设置原始图片路径（包括文件名）
                filepath = os.path.join(self.img_path, self.listWidget.item(i).text())
                # 设置水印图片保存路径（包括文件名）
                newfilepath = os.path.join(self.lineEdit_3.text(), self.listWidget.item(i).text())
                if self.radioButton.isChecked():  # 判断是否选择文字水印单选按钮
                    if self.lineEdit.text() == '':  # 判断是否输入了水印文字
                        QMessageBox.warning(None, '警告', '请输入水印文字', QMessageBox.Ok)
                        return
                    else:
                        self.textMark(filepath, newfilepath)  # 调用textMark方法添加文字水印
                        num += 1  # 处理图片数量加1
                else:
                    if self.lineEdit_2.text() != '':  # 判断水印图片不为空
                        self.imgMark(filepath, newfilepath)  # 调用imgMark方法添加图片水印
                        num += 1  # 处理图片数量加1
                    else:
                        QMessageBox.warning(None, '警告', '请选择水印图片', QMessageBox.Ok)
            self.statusBar.showMessage('任务完成，此次共处理 ' + str(num) + ' 张图片')  # 显示处理图片总数

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片批量添加水印"))
        self.pushButton.setText(_translate("MainWindow", "加载图片"))
        self.groupBox.setTitle(_translate("MainWindow", "水印设置"))
        self.radioButton.setText(_translate("MainWindow", "添加文字水印"))
        self.label.setText(_translate("MainWindow", "水印文字："))
        self.pushButton_2.setText(_translate("MainWindow", "字体设置"))
        self.radioButton_2.setText(_translate("MainWindow", "添加图片水印"))
        self.label_2.setText(_translate("MainWindow", "水印图片："))
        self.pushButton_3.setText(_translate("MainWindow", "浏览"))
        self.groupBox_2.setTitle(_translate("MainWindow", "透明度及位置设置"))
        self.label_3.setText(_translate("MainWindow", "透明度："))
        self.label_4.setText(_translate("MainWindow", "水印位置："))
        self.groupBox_3.setTitle(_translate("MainWindow", "路径设置"))
        self.label_5.setText(_translate("MainWindow", "保存位置："))
        self.pushButton_4.setText(_translate("MainWindow", "浏览"))
        self.pushButton_5.setText(_translate("MainWindow", "执行"))
