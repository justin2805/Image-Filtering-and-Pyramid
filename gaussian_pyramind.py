import cv2
import numpy
import read_disp_img
import matplotlib.pyplot as plt

class Gaussian_pyramind:

    def i_o_img(self):
        return read_disp_img.Read_display_images()

    def make_pyramid(self):
        print("Gaussian pyramind")
        original_image = read_disp_img.Read_display_images().readImage()
        final_image = original_image
        image_array = [final_image]
        resized_img_array = [cv2.resize(original_image,(109,109))]
        # print(final_image[0])
        # print("\n***********************************************************\n")
        for i in range(6):
            final_image = cv2.pyrDown(final_image)
            image_array.append(final_image)
            resized_img_array.append(cv2.resize(final_image,(109,109)))
            # print(final_image[0])
            # print("\n***********************************************************\n")
            # self.i_o_img().display_image(original_image, final_image)
        print(len(image_array))
        print(len(resized_img_array))
        rows, cols = original_image.shape
        print("rows : ",rows)
        print("cols : ",cols)
        print(cols + cols // 2)
        # pyramid = tuple(pyramid_gaussian(image, downscale=2, multichannel=True))
        composite_image = numpy.zeros((rows+109, cols + cols // 2), dtype=numpy.double)
        print(composite_image.shape)
        print(resized_img_array[0].shape)
        composite_image[:109,:109] = resized_img_array[0]
        r_row = 0
        r_col = 109
        for p in resized_img_array[1:]:
            n_rows, n_cols = p.shape[:2]
            composite_image[r_row: r_row+n_rows,r_col: r_col+n_cols] = p
            r_col = r_col + 109


        row = 109
        print("row : ",row)
        composite_image[row:row+rows, :cols] = image_array[0]
        i_row = 109
        for p in image_array[1:]:
            n_rows, n_cols = p.shape[:2]
            print("n_rows n_cols ",n_rows)
            composite_image[i_row:i_row + n_rows, cols:cols + n_cols] = p
            print("n_rows : ",n_rows)
            print("i_row : ",i_row)
            print("n_cols : ",n_cols)
            print("cols : ",cols)
            i_row += n_rows
            print("irow after add: ",i_row)
            print("*********************\n\n")
        fig, ax = plt.subplots()
        ax.imshow(composite_image,cmap='gray')
        plt.show()
        # cv2.imshow("Output",image_array)
        # concat_image_horizontally = numpy.concatenate((original_image, final_image), axis=1)
        # print("Final image size: ", final_image.size)
        # print("Final image dimension/shape: ", final_image.shape)
        # image = numpy.array(final_image, dtype='uint8')
        # image_resized = cv2.resize(image, (700, 600))


        # print(type(image_array))
        # image_array = numpy.array([image_array[0],image_array[1],image_array[2]])
        # print(type(image_array))
        # print(image_array.shape)
        # print(image_array[0].shape)
        # print(image_array[1].shape)
        # cv2.imshow("Output", image_array)
        # cv2.waitKey(0)