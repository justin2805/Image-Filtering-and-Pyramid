import read_disp_img
import cv2

class ImageSmoothing(object):

    def i_o_img(self):
        return read_disp_img.Read_display_images()

    def mean_filtering(self,k_size):
        print("Mean Filtering")
        original_image = self.i_o_img().readImage()
        final_image = cv2.blur(original_image, (k_size, k_size))
        self.i_o_img().display_image(original_image,final_image)


    def gaussian_smoothing(self, stdX, stdY, sigma):
        print("Gaussian Smoothing")
        original_image = self.i_o_img().readImage()
        final_image = cv2.GaussianBlur(original_image,(stdX,stdY),sigma)
        self.i_o_img().display_image(original_image,final_image)

    def median_filtering(self, k_size):
        print("Median Filtering")
        original_image = self.i_o_img().readImage()
        final_image = cv2.medianBlur(original_image, k_size)
        self.i_o_img().display_image(original_image, final_image)