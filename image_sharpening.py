import cv2
import read_disp_img
import matplotlib.pyplot as plt

class Image_sharpening:
    def i_o_img(self):
        return read_disp_img.Read_display_images()

    def sharpen(self,stdX, stdY, sigma, img_choice):
        original_image = self.i_o_img().readImage(img_choice)
        intermediate_image = cv2.GaussianBlur(original_image, (stdX, stdY), sigma)
        # self.i_o_img().display_image(original_image, intermediate_image)
        final_image = cv2.addWeighted(original_image,1,intermediate_image,-0.5,0)
        # self.i_o_img().display_image(original_image, final_image)
        fig, ax = plt.subplots(ncols=3)
        ax[0].imshow(original_image, cmap='gray')
        ax[1].imshow(intermediate_image, cmap='gray')
        ax[2].imshow(final_image, cmap='gray')
        plt.show()