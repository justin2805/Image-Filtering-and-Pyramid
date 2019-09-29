import cv2
import numpy
import read_disp_img

class Gaussian_pyramind:

    def i_o_img(self):
        return read_disp_img.Read_display_images()

    def make_pyramid(self):
        print("Gaussian pyramind")
        original_image = read_disp_img.Read_display_images().readImage()
        final_image = original_image
        print(final_image.ndim)
        image_array = [final_image]
        # print(final_image[0])
        # print("\n***********************************************************\n")
        for i in range(6):
            final_image = cv2.pyrDown(final_image)
            image_array.append(final_image)
            # print(final_image[0])
            # print("\n***********************************************************\n")
            # self.i_o_img().display_image(original_image, final_image)
        # cv2.imshow("Output",image_array)
        # concat_image_horizontally = numpy.concatenate((original_image, final_image), axis=1)
        # print("Final image size: ", final_image.size)
        # print("Final image dimension/shape: ", final_image.shape)
        # image = numpy.array(final_image, dtype='uint8')
        # image_resized = cv2.resize(image, (700, 600))
        print(type(image_array))
        image_array = numpy.asarray(image_array,dtype=object)
        print(type(image_array))
        cv2.imshow("Output", image_array)
        cv2.waitKey(0)