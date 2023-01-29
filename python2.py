import os

def rename_file():

    for count , file_name in enumerate(os.listdir("prank")):
        dst ="Hostel" + str(count) + ".jpg"
        src ='xyz'+ file_name
        dst ='xyz'+ dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    rename_file()