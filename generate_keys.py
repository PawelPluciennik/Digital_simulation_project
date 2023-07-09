from Generator.KeyGenerator import KeyGenerator
import os


def generate_folders_with_keys():
    parent_folder = "Seeds"

    folder_prefix = "KeyFolder"
    num_folders = 10
    num_keys_per_folder = 4

    os.makedirs(parent_folder, exist_ok=True)

    for i in range(1, num_folders + 1):
        folder_name = f"{folder_prefix}{i}"
        folder_path = os.path.join(parent_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        key_file_path = os.path.join(folder_path, "keys.txt")

        with open(key_file_path, "w") as key_file:
            for j in range(num_keys_per_folder):
                key = generator.generate_key()
                key_file.write(f"{key}\n")


generator = KeyGenerator()
generate_folders_with_keys()
