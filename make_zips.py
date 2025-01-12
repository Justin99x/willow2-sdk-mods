import zipfile
import os


def zip_dir(dir_name: str):
    zip_file_name = os.path.join(dir_name, f"{dir_name}.zip")
    sdkmod_name = os.path.join(dir_name, f"{dir_name}.sdkmod")
    zip_file = zipfile.ZipFile(zip_file_name, mode='w')

    try:
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                if ".zip" not in file:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path)
    finally:
        zip_file.close()

    if os.path.exists(sdkmod_name):
        os.remove(sdkmod_name)
    os.rename(zip_file_name, sdkmod_name)



if __name__ == '__main__':
    zip_dir("save_file_organizer")
    zip_dir("speedrun_practice")



