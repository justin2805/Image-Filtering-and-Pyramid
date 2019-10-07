import cv2
import read_disp_img
import matplotlib.pyplot as plt
import numpy as np
import statistics
import math

class Image_sharpening:
    def i_o_img(self):
        return read_disp_img.Read_display_images()

    def sharpen(self,stdX, stdY, sigma, img_choice):
        original_image = self.i_o_img().readImage(img_choice)
        intermediate_image = cv2.GaussianBlur(original_image, (stdX, stdY), sigma)
        # self.i_o_img().display_image(original_image, intermediate_image)
        final_image = cv2.addWeighted(original_image,1.5,intermediate_image,-0.5,0)
        # self.i_o_img().display_image(original_image, final_image)
        fig, ax = plt.subplots(ncols=3)
        ax[0].imshow(original_image, cmap='gray')
        ax[0].set_title("Original image")
        ax[1].imshow(intermediate_image, cmap='gray')
        ax[1].set_title("Blurred image")
        ax[2].imshow(final_image, cmap='gray')
        ax[2].set_title("Final image")
        plt.show()


    def sharpen_new(self, img_choice,k):
        # self.unsharp_masking(img_choice,k)
        self.laplacian_method(img_choice,k)

    def unsharp_masking(self,img_choice,k):
        print("Unsharp Masking :: ")
        original_image = self.i_o_img().readImage(img_choice)
        shape = original_image.shape
        rows = shape[0]
        cols = shape[1]
        print("rows : ", rows)
        print("cols : ", cols)
        k_size = 3
        sigma = 1

        Z = 1 / (2 * math.pi * sigma * sigma)
        half_k_size = k_size // 2
        gaussian_kernel = np.zeros([k_size, k_size], dtype=float)
        print("half_k_size", half_k_size)
        for i in range(k_size):
            for j in range(k_size):
                m = i - half_k_size
                n = j - half_k_size
                exp = Z * math.exp(-((m * m) + (n * n)) / (2 * sigma * sigma))
                gaussian_kernel[i, j] = exp
                print("m : " + str(m) + " : n : " + str(n) + " :: exp :: " + str(exp))

        print("gaussian kernel shape \n", gaussian_kernel.shape)
        print("gaussian kernel \n,", gaussian_kernel)

        padding = k_size - 1
        half_padding = int(padding / 2)
        new_rows = rows + padding
        new_cols = cols + padding
        print("new_rows", new_rows)
        print("new_cols", new_cols)
        # padded_image = np.zeros([new_rows, new_cols], dtype=int)
        blurred_image = np.zeros([rows, cols], dtype=int)
        mask_image = np.zeros([rows, cols], dtype=int)
        final_image = np.zeros([rows, cols], dtype=int)

        padded_image = np.pad(original_image, pad_width=half_padding, mode='constant', constant_values=0)

        # for row in range(new_rows):
        #     for col in range(new_cols):
        #         if not (
        #                 row < half_padding or col < half_padding or row >= new_rows - half_padding or col >= new_cols - half_padding):
        #             padded_image[row, col] = original_image[row - half_padding, col - half_padding]

        index_row = 0
        index_col = 0
        row = 0
        col = 0
        run_loop = True
        iii = 0
        ar1 = []

        while run_loop:
            mean_filter = 0
            if row + k_size == new_rows - 1 and col + k_size == new_cols - 1:
                # stop the outer loop
                run_loop = False
            else:
                while index_row < k_size:
                    while index_col < k_size:
                        mean_filter += int(round(
                            (padded_image[index_row + row, index_col + col]) * gaussian_kernel[index_row, index_col]))
                        index_col += 1
                    index_col = 0
                    index_row += 1
                index_row = 0
                index_col = 0
                # if row ==0 :
                # ar1.append(int(round(mean_filter / (k_size * k_size))))
                # final_image[row]
                if not (
                        row < half_padding - 1 or col < half_padding - 1 or row >= new_rows - half_padding or col >= new_cols - half_padding):
                    blurred_image[row, col - half_padding + 1] = int(round(mean_filter / (k_size * k_size)))
                    # if row == 0:
                    #     print(col-half_padding+1)
                    #     # if len(ar1) != 0 and col-1 != ar1[len(ar1) - 1]:
                    #     print(col)
                    # ar1.append(col)

                if col + k_size < new_cols - 1:
                    # slide window 1 cell to the right
                    col += 1
                elif col + k_size == new_cols - 1 and row + k_size < new_rows - 1:
                    # slide window to the left border and 1 cell below
                    col = 0
                    row += 1

        # print(len(ar1))
        # for r in range(rows-1):
        #     for c in range(cols-1):
        #         final_image[r,c] = ar1.pop(0)

        # subtract blurred image from the original
        for i in range(rows):
            for j in range(cols):
                mask_image[i,j] = original_image[i,j] - blurred_image[i,j]
                final_image[i,j] = original_image[i,j] + ( mask_image [i,j])




        print("\n *******************************\n")
        print(*original_image[iii], sep=", ")
        print(*final_image[iii], sep=", ")
        print("original_image", len(original_image[iii]))
        print("final_image", len(final_image[iii]))
        print(type(final_image))
        print(original_image.shape)
        print(final_image.shape)
        print(type(original_image))
        fig, ax = plt.subplots(ncols=3)
        ax[0].imshow(original_image, cmap='gray')
        ax[0].set_title("Original")
        ax[1].imshow(blurred_image, cmap='gray')
        ax[1].set_title("Blurred Image")
        # ax[2].imshow(mask_image, cmap='gray')
        # ax[2].set_title("Subtraction Mask Image")
        ax[2].imshow(final_image, cmap='gray')
        ax[2].set_title("Final")
        plt.show()

    def laplacian_method(self, img_choice,composite_mask_choice):
        print()
        original_image = self.i_o_img().readImage(img_choice)
        shape = original_image.shape
        rows = shape[0]
        cols = shape[1]
        print("rows : ", rows)
        print("cols : ", cols)
        k_size = 3
        sigma = 1

        Z = 1 / (2 * math.pi * sigma * sigma)
        half_k_size = k_size // 2
        if composite_mask_choice == 1:
            laplacian_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        else:
            laplacian_kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])


        padding = k_size - 1
        half_padding = int(padding / 2)
        new_rows = rows + padding
        new_cols = cols + padding
        print("new_rows", new_rows)
        print("new_cols", new_cols)
        # padded_image = np.zeros([new_rows, new_cols], dtype=int)
        laplacian_filtered_image = np.zeros([rows, cols], dtype=int)
        final_image = np.zeros([rows, cols], dtype=int)

        padded_image = np.pad(original_image, pad_width=half_padding, mode='constant', constant_values=0)

        # for row in range(new_rows):
        #     for col in range(new_cols):
        #         if not (
        #                 row < half_padding or col < half_padding or row >= new_rows - half_padding or col >= new_cols - half_padding):
        #             padded_image[row, col] = original_image[row - half_padding, col - half_padding]

        index_row = 0
        index_col = 0
        row = 0
        col = 0
        run_loop = True
        iii = 0
        ar1 = []

        while run_loop:
            sum = 0
            if row + k_size == new_rows - 1 and col + k_size == new_cols - 1:
                # stop the outer loop
                run_loop = False
            else:
                while index_row < k_size:
                    while index_col < k_size:
                        sum += int(round(
                            (padded_image[index_row + row, index_col + col]) * laplacian_kernel[index_row, index_col]))
                        index_col += 1
                    index_col = 0
                    index_row += 1
                index_row = 0
                index_col = 0
                # if row ==0 :
                # ar1.append(int(round(mean_filter / (k_size * k_size))))
                # final_image[row]
                if not (row < half_padding - 1 or col < half_padding - 1 or row >= new_rows - half_padding or col >= new_cols - half_padding):
                    final_image[row, col - half_padding + 1] = int(round(sum / (k_size * k_size)))
                    # if row == 0:
                    #     print(col-half_padding+1)
                    #     # if len(ar1) != 0 and col-1 != ar1[len(ar1) - 1]:
                    #     print(col)
                    # ar1.append(col)

                if col + k_size < new_cols - 1:
                    # slide window 1 cell to the right
                    col += 1
                elif col + k_size == new_cols - 1 and row + k_size < new_rows - 1:
                    # slide window to the left border and 1 cell below
                    col = 0
                    row += 1

        # print(len(ar1))
        # for r in range(rows-1):
        #     for c in range(cols-1):
        #         final_image[r,c] = ar1.pop(0)

        # subtract blurred image from the original
        # for i in range(rows):
        #     for j in range(cols):
        #         final_image[i, j] = original_image[i, j] + laplacian_filtered_image[i, j]

        print("\n *******************************\n")
        print(*original_image[iii], sep=", ")
        print(*final_image[iii], sep=", ")
        print("original_image", len(original_image[iii]))
        print("final_image", len(final_image[iii]))
        print(type(final_image))
        print(original_image.shape)
        print(final_image.shape)
        print(type(original_image))
        fig, ax = plt.subplots(ncols=2)
        ax[0].imshow(original_image, cmap='gray')
        ax[0].set_title("Original")
        ax[1].imshow(final_image, cmap='gray')
        ax[1].set_title("Final Image")
        # ax[2].imshow(mask_image, cmap='gray')
        # ax[2].set_title("Subtraction Mask Image")
        # ax[2].imshow(final_image, cmap='gray')
        # ax[2].set_title("Final image")
        plt.show()