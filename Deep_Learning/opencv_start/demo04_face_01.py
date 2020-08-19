import cv2
import face_recognition
# 打开摄像头，读取摄像头拍摄到的画面
# 定位到画面中人的脸部，并用绿色的框框把人的脸部框住

# 1、打开摄像头，获取摄像头对象
video_capture = cv2.VideoCapture(0)     # 0代表的是第一个摄像头

# 2、循环不停的去获取摄像头拍摄到的画面，并做进一步的处理
while True:
    # 进一步处理
    # 2.1、获取摄像头拍摄到的画面
    ret, img = video_capture.read()     # img 摄像头拍摄的画面

    # 2.2、从拍摄到的画面中提取出人的脸部所在区域（可能会有多个）
    face_locations = face_recognition.face_locations(img)

    # 2.3、循环遍历人的脸部所在区域，并画框
    for top, right, bottom, left in face_locations:
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
    # 2.4、通过OpenCV把画面展示出来
    cv2.imshow("Video", img)
    # 2.5、设定按Q退出while循环，退出程序的这样一个机制
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 3、退出程序的时候，释放摄像头或其他资源
video_capture.release()
cv2.destroyAllWindows()