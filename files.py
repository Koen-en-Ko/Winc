__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

cwd = os.getcwd()
cache_dir = "cache"
cache_path = os.path.join(cwd, cache_dir)


def clean_cache():
    if os.path.exists(cache_dir):
        for x in os.listdir(cache_dir):
            os.remove(f"{cache_dir}/{x}")
    else:
        os.mkdir(cache_dir)


clean_cache()


def cache_zip(zip_file_path, cache_path):
    with ZipFile(zip_file_path, "r") as zObject:
        zObject.extractall(cache_path)


cache_zip("data.zip", "cache")


def cached_files():
    list_of_filepaths = []
    files = os.listdir(cache_path)
    for file in files:
        os.path.join(cache_path, file)
    for file in os.listdir(cache_path):
        list_of_filepaths.append(os.path.join(cache_path, file))
    return list_of_filepaths


cached_files()


files_list = cached_files()


def find_password(files_list):
    for file in files_list:
        with open(file, 'r') as f:
            text = f.readlines()
            for line in text:
                if 'password' in line:
                    password = line.split(' ')[1]
                    password = password.strip('\n')
                    return password


find_password(files_list)
