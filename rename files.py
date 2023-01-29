import os
def rename_files():
    list_files= os.listdir(r"C:\Users\Farzana Nipa\.PyCharmCE2018.3\config\scratches\prank")
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"C:\Users\Farzana Nipa\.PyCharmCE2018.3\config\scratches\prank")

    for file_name in list_files:
        result = ''.join(i for i in file_name if not i.isdigit())
        os.rename(file_name,result)
    os.chdir(saved_path)

rename_files()