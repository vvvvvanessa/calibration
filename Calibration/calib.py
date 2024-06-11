import cv2
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from UI.main_ui import Ui_Dialog
from Calibration.calib_param import *
import numpy as np
import glob
import os


class Calibration(QDialog, Ui_Dialog):
    calib_param = CalibParam()
    calib_result = CalibResult()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_params()
        self.make_connections()
        self.show()
    def init_params(self):
        self.cube_size.setValue(15)
        self.verti_corner.setValue(7)
        self.horiz_corner.setValue(10)
    def select_path_in(self):
        img_dir = QFileDialog.getExistingDirectory(self, caption="open intrinsic image file directory", dir="./")
        self.img_file_in.setText(img_dir)

    def select_path_ex(self):
        img_dir = QFileDialog.getOpenFileName(self, caption="open extrinsic image file", dir="./")
        self.img_file_ex.setText(img_dir[0])

    def process_calib(self):
        # Requires different values for vertical and horizontal
        if self.verti_corner.value() == self.horiz_corner.value():
            QMessageBox.warning(self, "warning", "vertical and horizontal corner numbers should be different")
            return

        self.calib_param.set_params(vertical_corner=self.verti_corner.value(), horizontal_corner=self.horiz_corner.value(),
                                    cube_size=self.cube_size.value(), intrinsic_img_file=self.img_file_in.text(),
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
        _, _, cube_size = self.calib_param.get_params()
        # top left corner of the intersection point on the calibration board as the center of the world coordinate
        obj_point = obj_point * cube_size

        # save all the object points in world coordinate and image coordinates
        obj_points = []
        img_points = []

        img_path = self.calib_param.get_intrisic_path()
        # read images only
        images = [os.path.join(img_path, x) for x in os.listdir(img_path)
                    if any(x.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])
                    ]
        initiated = False
        for img in images:
            cv_img = cv2.imread(img)
            gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
            # find inner corners of the chessboard
            ret, corners = cv2.findChessboardCorners(gray, (chessboard_params[0], chessboard_params[1]), None)
            if ret:
                # get a more precise corner
                corners = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1),
                                           (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.01))
                img_points.append(corners)
                obj_points.append(obj_point)
                cv2.drawChessboardCorners(cv_img, (chessboard_params[0], chessboard_params[1]), corners, ret)
        #         cv2.imshow("img", cv_img)
        #         cv2.waitKey(500)
        # cv2.destroyAllWindows()

        # mtx is the intrinsic parameter matrix and dist is the distortion vector
        # rvecs & tvecs are the extrinsic parameters for camera
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)
        self.calib_result.set_int_calib_result(mtx, dist)
        print("相机内参矩阵：\n", mtx)
        print("畸变系数：\n", dist)

        for i in range(0, len(img_points)):
            img = img_points[i]
            # for pt in img:
            pt = img[0]
            # corner points on the images with distortion corrected
            dst = cv2.undistortPoints(pt, mtx, dist, P = mtx)
            z = 1.0
            dst = dst[0, 0]
            # interprete the point on the image coordinate to the camera coordinate
            # (z represents the distance between image coordinate to the camera coordinate)
            camera_points = np.array([[dst[0] * z], [dst[1] * z], [z]])
            # rotation matrix
            R, _ = cv2.Rodrigues(rvecs[i])
            # image point in world coordinate
            world_points = np.dot(R.T, camera_points - tvecs[i])
            camera_origin_in_world = -np.dot(R.T, tvecs[i])

            t = -camera_origin_in_world[2]/(camera_origin_in_world[2] - camera_points[2])
            x = camera_origin_in_world[0] + t * (camera_origin_in_world[0] - camera_points[0])
            y = camera_origin_in_world[1] + t * (camera_origin_in_world[1] - camera_points[1])
            z = camera_origin_in_world[2]+ t * (camera_origin_in_world[2] - camera_points[2])
            a = 0

    def Extrinsic(self):
        extrinsic_img_path = self.calib_param.get_extrisic_path()
        img = cv2.imread(extrinsic_img_path)
        camera_mat, dist_coeff = self.calib_result.get_int_calib_result()
        corrected_img = cv2.undistort(img, camera_mat, dist_coeff, dst = None)

        chessboard_params = self.calib_param.get_params()
        # world coordinate for the chessboard
        obj_point = np.zeros((chessboard_params[0] * chessboard_params[1], 3), np.float32)
        obj_point[:, :2] = np.mgrid[0:chessboard_params[0], 0:chessboard_params[1]].T.reshape(-1, 2)
        _, _, cube_size = self.calib_param.get_params()
        # top left corner of the intersection point on the calibration board as the center of the world coordinate
        obj_point = obj_point * cube_size

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # find inner corners of the chessboard
        ret, corners = cv2.findChessboardCorners(gray, (chessboard_params[0], chessboard_params[1]), None)
        if ret:
            ret, rvec, tvec = cv2.solvePnP(obj_point, corners, camera_mat, dist_coeff)
            rotation_matrix, _ = cv2.Rodrigues(rvec)

            # 测试一个点
            test = corners[0]
            dst = cv2.undistortPoints(corners[0], camera_mat, dist_coeff, P = camera_mat)
            a = (corners[0][0][0] - camera_mat[0][2])/camera_mat[0][0]
            b = (corners[0][0][1] - camera_mat[1][2])/camera_mat[1][1]
            z = 1.0
            dst = dst[0, 0]
            # interprete the point on the image coordinate to the camera coordinate
            # (z represents the distance between image coordinate to the camera coordinate)
            # camera_points = np.array([[dst[0] * z], [dst[1] * z], [z]])
            camera_points = np.array([[a * z], [b * z], [z]])
            X_c = a * z
            Y_c = b * z
            Z_c = 1

            R, _ = cv2.Rodrigues(rvec)

            world_points = np.dot(np.linalg.inv(R),
                                 np.array([X_c - tvec[0], Y_c - tvec[1], Z_c - tvec[2]]))
            # rotation matrix
            # image point in world coordinate
            # world_points = np.dot(R.T, camera_points - tvec)
            camera_origin_in_world = -np.dot(R.T, tvec)

            t = -camera_origin_in_world[2]/(camera_origin_in_world[2] - camera_points[2])
            x = camera_origin_in_world[0] + t * (camera_origin_in_world[0] - camera_points[0])
            y = camera_origin_in_world[1] + t * (camera_origin_in_world[1] - camera_points[1])
            z = camera_origin_in_world[2] + t * (camera_origin_in_world[2] - camera_points[2])
            print("ttt")











