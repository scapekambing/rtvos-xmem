import os
import shutil

def delete_files_in_folder(folder_path):
    # check if the folder exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    # iterate through each file/subfolder in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # if it's a file or a symlink, delete it
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                #print(f"File deleted: {file_path}")
            # if it's a folder, delete it and all its contents
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Folder and its contents deleted: {file_path}")
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
    print("finish delete")

    
def main():
    folder_path = './workspace'
    delete_files_in_folder(folder_path)

    folder_path = './saving_frame'
    delete_files_in_folder(folder_path)

    
if __name__ == "__main__":
    main()

    
