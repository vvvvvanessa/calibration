import cv2
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from UI.main_ui import Ui_Dialog
from Calibration.calib_param import CalibParam
import numpy as np
import glob
import os


class Calibration(QDialog, Ui_Dialog):
    calib_param = CalibParam()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.make_connections()
        self.show()

    def select_path_in(self):
        img_dir = QFileDialog.getExistingDirectory(self, caption="open intrinsic image file directory", dir="./")
        self.img_file_in.setText(img_dir)

    def select_path_ex(self):
        img_dir = QFileDialog.getExistingDirectory(self, caption="open extrinsic image file directory", dir="./")
        self.img_file_ex.setText(img_dir)

    def process_calib(self):
        # Requires different values for vertical and horizontal
        if self.verti_corner.value() == self.horiz_corner.value():
            QMessageBox.warning(self, "warning", "vertical and horizontal corner numbers should be different")
            return

        self.calib_param.set_params(vertical_corner=self.verti_corner.value(), horizontal_corner=self.horiz_corner.value(),
                                    cube_width=self.cube_wid.value(), cube_height=self.cube_hei.value(),
                                    intrinsic_img_file=self.img_file_in.text(),
                                    extrinsic_img_file=self.img_file_ex.text())

        self.Intrinsic()
        self.Extrinsic()

    def make_connections(self):
        self.open_file_in.clicked.connect(self.select_path_in)
        self.open_file_ex.clicked.connect(self.select_path_ex)
        self.buttonBox.accepted.connect(self.process_calib)


    def Intrinsic(self):
        """
        camera intrinsic parameter calibration
        :return:
        """
        chessboard_params = self.calib_param.get_params()
        # world coordinate for the chessboard
        obj_point = np.zeros((chessboard_params[0] * chessboard_params[1], 3), np.float32)
        obj_point[:, :2] = np.mgrid[0:chessboard_params[0], 0:chessboard_params[1]].T.reshape(-1, 2)
        _, _, cube_wid, _ = self.calib_param.get_params()
        # top left corner of the intersection point on the calibration board as the center of the world coordinate
        obj_point = obj_point * cube_wid

        # save all the object points in world coordinate and image coordinates
        obj_points = []
        img_points = []

        img_path = self.calib_param.get_intrisic_path()

        images = [os.path.join(img_path, x) for x in os.listdir(img_path)
                    if any(x.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])
                    ]
        # images = glob.glob(img_path + "/*")
        for img in images:
            cv_img = cv2.imread(img)
            gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

            ret, corners = cv2.findChessboardCorners(gray, (chessboard_params[0], chessboard_params[1]), None)
            if ret:
                img_points.append(corners)
                obj_points.append(obj_point)
                cv2.drawChessboardCorners(cv_img, (chessboard_params[0], chessboard_params[1]), corners, ret)
                cv2.imshow("img", cv_img)
                cv2.waitKey(500)

        cv2.destroyAllWindows()

        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)
        print("相机内参矩阵：\n", mtx)
        print("畸变系数：\n", dist)
        print("旋转向量：\n", rvecs)
        print("平移向量：\n", tvecs)

        img = cv2.imread('calibration_images/example.jpg')
        h, w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

        # 使用内参和畸变系数来校正图像
        dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
        print("this is the intrinsic process")



    def Extrinsic(self):
        print("this is extrinsic process")

