import os

main_folder = os.getcwd()

sub_folders = os.listdir(main_folder)

sub_folders.remove('rename.py')
for folder in sub_folders:
    counter = 0
    sub_folder = main_folder + '/' + folder
    for image in os.listdir(sub_folder):
        # print(folder, image)
        # break
        old_name = main_folder + '/' + folder + '/' + image
        new_name = main_folder + '/' + folder + '/' + folder +'_' + str(counter) + '.jpeg'
        
        # print("old_name: ", old_name)
        # print("new_name: ", new_name)
        # print("*"*100)
        # print(image)
        os.rename(old_name, new_name)
        counter += 1