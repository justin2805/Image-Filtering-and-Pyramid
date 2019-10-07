import cv2
import numpy

class Read_display_images:
    def readImage(self, use_image):
        # Select any one image path from below and  comment out the remaining paths
        #  OR add new path for separate image

        if use_image == 1:
            image_path = r'images/Fig0312(a)(kidney).tif'
        elif use_image == 2:
            image_path = r'images/Fig0333(a)(test_pattern_blurring_orig).tif'
        elif use_image == 3:
            image_path = r'images/Fig0334(a)(hubble-original).tif'
        elif use_image == 4:
            image_path = r'images/Fig0335(a)(ckt_board_saltpep_prob_pt05).tif'
        elif use_image == 5:
            image_path = r'images/Fig0338(a)(blurry_moon).tif'
        elif use_image == 6:
            image_path = r'images/Fig0340(a)(dipxe_text).tif'
        elif use_image == 7:
            image_path = r'images/jack-russell-blurred-1200x630.jpg'
        else:
            image_path = r'images/Lenna.png'
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        return image


    def display_image(self, original_image, final_image):
        # image = numpy.asarray(flat_image)
        # image = image.reshape(height, width)
        concat_image_horizontally = numpy.concatenate((original_image, final_image), axis=1)
        # print("Final image size: ", final_image.size)
        # print("Final image dimension/shape: ", final_image.shape)
        # image = numpy.array(final_image, dtype='uint8')
        # image_resized = cv2.resize(image, (700, 600))
        cv2.imshow("Output", concat_image_horizontally)
        cv2.waitKey(0)