import image_smoothing
import image_sharpening
import gaussian_pyramind

class Main(object):
    def display_options(self):
        # try:
            while True:
                main_choice = int(input("MAIN MENU :\nEnter choice\n1. Image Smoothing\n2. Image Sharpening\n3. Gaussian Pyramid\n4. Exit program\n -->"))
                if main_choice == 1:
                    self.image_smoothing()
                elif main_choice == 2:
                    self.image_sharpening()
                elif main_choice == 3:
                    self.gaussian_pyramind()
                elif main_choice == 4:
                    print("Exiting program...")
                    break
                else: print("Invalid input")
        # except ValueError as v:
        #     print("Exception thrown :: "+str(v))

    def image_smoothing(self):
        ism_obj = image_smoothing.ImageSmoothing()
        while True:
            choice = int(input("*************************************************************************\n"
                               "IMAGE SMOOTHING:\n*************************************************************************\n"
                      "      Enter choice \n      1--> Mean Filtering \n      2--> Gaussian Filtering \n      3--> Median Filtering \n"
                      "      4--> Go to main menu\n-->"))
            if choice == 1:
                k_size = int(input("Enter k_size : "))
                ism_obj.mean_filtering(k_size)
            elif choice == 2:
                stdX = int(input("Enter standard deviation in X direction : "))
                stdY = int(input("Enter standard deviation in Y direction : "))
                sigma = float(input("Enter sigma value : "))
                ism_obj.gaussian_smoothing(stdX, stdY, sigma)
            elif choice == 3:
                ksize = int(input("Enter ksize : "))
                ism_obj.median_filtering(ksize)
            elif choice == 4:
                print("Moving back to main menu:\n*************************************************************************\n")
                break
            else:
                print("Invalid input")

    def image_sharpening(self):
        print("Image Sharpening")
        sharpen_obj = image_sharpening.Image_sharpening()
        sharpen_obj.sharpen()

    def gaussian_pyramind(self):
        print("gaussian pyramid")
        constr_pyramid_obj = gaussian_pyramind.Gaussian_pyramind()
        constr_pyramid_obj.make_pyramid()

m = Main()
m.display_options()