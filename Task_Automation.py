import os
import shutil

source = input("Enter source folder path: ")
destination = input("Enter destination folder path: ")

if not os.path.exists(destination):
    os.makedirs(destination)

for file in os.listdir(source):
    if file.endswith(".jpg"):
        full_path = os.path.join(source, file)
        shutil.move(full_path, os.path.join(destination, file))

print("All JPG files moved successfully.")
