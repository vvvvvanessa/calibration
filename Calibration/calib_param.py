# Parameters used for camera calibration
class CalibParam:

    _vertical_corner = 0
    _horizontal_corner = 0
    _cube_width = 0
    _cube_height = 0
    _intrinsic_img_file = ""
    _extrinsic_img_file = ""


    def get_params(self):
        """
        return vertical_corner, horizontal_corner, cube_width, cube_height
        """
        return self._vertical_corner, self._horizontal_corner, self._cube_width, self._cube_height

    def get_intrisic_path(self):
        return self._intrinsic_img_file

    def get_extrisic_path(self):
        return self._extrinsic_img_file

    def set_params(self, vertical_corner, horizontal_corner, cube_width, cube_height,
                   intrinsic_img_file, extrinsic_img_file):
        self._cube_height = cube_height
        self._cube_width = cube_width
        self._vertical_corner = vertical_corner
        self._horizontal_corner = horizontal_corner
        self._intrinsic_img_file = intrinsic_img_file
        self._extrinsic_img_file = extrinsic_img_file

class CalibData:
    def __init__(self):
        self.type = None
        self.camera_mat = None
        self.dist_coeff = None
        self.rvecs = None
        self.tvecs = None
        self.map1 = None
        self.map2 = None
        self.reproj_err = None
        self.ok = False
