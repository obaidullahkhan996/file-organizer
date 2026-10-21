import os
import shutil

target = r"C:\Users\OBAIDULLAH\Desktop\test_folder"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Code": [".py", ".js", ".html", ".css"],
    "Music": [".mp3", ".wav", ".m4a"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z"]
}

for file in os.listdir(target):
    path = os.path.join(target, file)

    # Skip folders
    if os.path.isdir(path):
        continue

    ext = os.path.splitext(file)[1].lower()

    for folder, exts in file_types.items():
        if ext in exts:
            dest = os.path.join(target, folder)
            os.makedirs(dest, exist_ok=True)
            shutil.move(path, os.path.join(dest, file))
            print(f"Moved: {file} -> {folder}/")
            break

print("\nOrganization complete!")