from datetime import date
from pathlib import Path
import os
import re
import shutil
import zipfile


def make_dir(new_dir_name):
    new_dir_path = os.path.join("./", new_dir_name)
    if Path(new_dir_path).exists() and Path(new_dir_path).is_dir():
        shutil.rmtree(new_dir_path)
    os.mkdir(Path(new_dir_path))
    return new_dir_path


def unzip_log_files(zip_file, output_dir):
    regex_log_file = r"(\d+-){3}"  # pattern of log file
    with zipfile.ZipFile(zip_file, mode="r") as archive:
        # archive.extractall(output_dir)
        for file in archive.namelist():
            if re.search(regex_log_file, file):
                archive.extract(file, output_dir)

    return "Extract files successfully!"


def get_log_file_path(parent_folder):
    regex_filename = r"(\d+-){3}"  # filename style
    file_path_list = []
    for root, _, files in os.walk(parent_folder):
        for file in files:
            if re.search(regex_filename, file):
                file_path_list.append(os.path.join(root, file))
    return file_path_list


def reorganize_log_files(log_file_list):
    organized_log_package = make_dir("./organized_log_package")

    for file_path in log_file_list:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            regex_device_name = r"<([A-Z0-9-]+)>"
            result = re.search(regex_device_name, content)
            if result is None:
                print(file_path)
                continue

            device_name = re.search(regex_device_name, content).group(1)

        today_str = date.today().strftime("%d_%m_%Y")
        new_file_name = "_".join([today_str, device_name + ".log"])
        with open(os.path.join(organized_log_package, new_file_name), "w") as f:
            f.write(content)


if __name__ == "__main__":
    zip_file_path = os.path.abspath(
        "Spain_OSP_Calzada_DS_Lite_Config_TP3_without_display_session_Report_20220914041734.zip"
    )
    extracted_content_dir = make_dir("extracted_content")
    unzip_log_files(zip_file_path, extracted_content_dir)
    log_file_list = get_log_file_path(extracted_content_dir)
    reorganize_log_files(log_file_list)
    print("Extract log file successfully!")
