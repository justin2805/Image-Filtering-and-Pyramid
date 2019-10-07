import image_smoothing
import image_sharpening
import gaussian_pyramind

class Main(object):
    def display_options(self):
        try:
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
        except ValueError as v:
            print("Exception thrown :: "+str(v))

    def image_smoothing(self):
        ism_obj = image_smoothing.ImageSmoothing()
        img_choice = self.select_image()
        while True:
            choice = int(input("*************************************************************************\n"
                               "IMAGE SMOOTHING:\n*************************************************************************\n"
                      "      Enter choice \n      1--> Mean Filtering \n      2--> Gaussian Filtering \n      3--> Median Filtering \n"
                      "      4--> Go to main menu\n-->"))
            if choice == 1:
                k_size = int(input("Enter k_size : "))
                # ism_obj.mean_filtering(k_size,img_choice)
                ism_obj.mean_filtering_full_algo(k_size,img_choice)
            elif choice == 2:
                # stdX = int(input("Enter standard deviation in X direction : "))
                # stdY = int(input("Enter standard deviation in Y direction : "))
                k_size = int(input("Enter ksize : "))
                sigma = float(input("Enter sigma value : "))
                ism_obj.gaussian_filtering_full_algo(k_size, sigma,img_choice)
                # ism_obj.gaussian_filtering_full_algo(3, sigma,img_choice)
                # ism_obj.gaussian_smoothing(stdX,stdY, sigma,img_choice)
            elif choice == 3:
                ksize = int(input("Enter ksize : "))
                ism_obj.median_filtering_full_algo(ksize, img_choice)
            elif choice == 4:
                print("Moving back to main menu:\n*************************************************************************\n")
                break
            else:
                print("Invalid input")

    def image_sharpening(self):
        # stdX = int(input("*************************************************************************\n"
        #                        "IMAGE SHARPENING:\n*************************************************************************\n"
        #                  "Enter standard deviation in X direction : "))
        # stdY = int(input("Enter standard deviation in Y direction : "))
        # sigma = float(input("Enter sigma value : "))
        choice = self.select_image()
        print("Select composite mask choice  : \n1. | 0 -1 0| or 2. | -1 -1 -1|\n   |-1 5 -1|       | -1  9 -1|\n   | 0 -1 0|       | -1 -1 -1|\n")
        composite_mask_choice = int(input("-->"))
        sharpen_obj = image_sharpening.Image_sharpening()
        # sharpen_obj.sharpen(stdX, stdY, sigma, choice)
        sharpen_obj.sharpen_new(choice,composite_mask_choice)

    def gaussian_pyramind(self):
        print("*************************************************************************\n"
                               "GAUSSIAN PYRAMID:\n*************************************************************************\n")
        constr_pyramid_obj = gaussian_pyramind.Gaussian_pyramind()
        constr_pyramid_obj.make_pyramid()

    def select_image(self):
        choice = int(input("-------SELECT IMAGE FOR PROCESSING----------\n"
                           "1--> Kidney\n2--> Pattern blurring\n3--> Hubble\n"
                           "4--> Circuit Board\n5--> Blurry moon\n6--> Text\n7--> jack-russell-blurred\n-->"))
        if choice < 1 or choice > 7:
            print("Invalid entry")
        else:
            return choice

m = Main()
m.display_options()