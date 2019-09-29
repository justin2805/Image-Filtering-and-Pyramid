import cv2
import numpy

class Read_display_images:
    def readImage(self):
        # Select any one image path from below and  comment out the remaining paths
        #  OR add new path for separate image

        # image_path = r'images/Fig0312(a)(kidney).tif'
        # image_path = r'images/Fig0333(a)(test_pattern_blurring_orig).tif'
        # image_path = r'images/Fig0334(a)(hubble-original).tif'
        # image_path = r'images/Fig0335(a)(ckt_board_saltpep_prob_pt05).tif'
        # image_path = r'images/Fig0338(a)(blurry_moon).tif'
        # image_path = r'images/Fig0340(a)(dipxe_text).tif'
        image_path = r'images/Lenna.png'
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        return image


    def display_image(self, original_image, final_image):
        # image = numpy.asarray(flat_image)
        # image = image.reshape(height, width)
        concat_image_horizontally = numpy.concatenate((original_image, final_image), axis=1)
        print("Final image size: ", final_image.size)
        print("Final image dimension/shape: ", final_image.shape)
        # image = numpy.array(final_image, dtype='uint8')
        # image_resized = cv2.resize(image, (700, 600))
        cv2.imshow("Output", concat_image_horizontally)
        cv2.waitKey(0)