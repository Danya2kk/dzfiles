import os


def name_of_system():
    return os.name


def current_directory():
    return os.getcwd()


def make_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)
    else:
        print("Данная папка уже существует")


def size_of_files(path):
    files = os.listdir(path)
    sum = 0
    for file in files:
        info = os.stat(os.path.join(path, file))
        sum += info[6]

    return sum


print(f"Имя операционной системы: {name_of_system()}")
print(f"Путь: {current_directory()}")

text_folder = os.path.join(current_directory(), "TXT Folder")
make_folder(text_folder)

csv_folder = os.path.join(current_directory(), "CSV Folder")
make_folder(csv_folder)

json_folder = os.path.join(current_directory(), "JSON Folder")
make_folder(json_folder)


files = os.listdir(current_directory())
for file in files:
    if os.path.isfile(file):
        if file.endswith(".txt"):
            os.replace(file, os.path.join(text_folder, file))
        elif file.endswith(".json"):
            os.replace(file, os.path.join(json_folder, file))
        elif file.endswith(".csv"):
            os.replace(file, os.path.join(csv_folder, file))

print(f"В папке ({text_folder}) перемещено {len(os.listdir(text_folder))} файлов."
      f" Их суммарный размер {size_of_files(text_folder)} байт")

print(f"В папке ({csv_folder}) перемещено {len(os.listdir(csv_folder))} файлов."
      f" Их суммарный размер {size_of_files(csv_folder)} байт")

print(f"В папке ({json_folder}) перемещено {len(os.listdir(json_folder))} файлов"
      f". Их суммарный размер {size_of_files(json_folder)} байт")

rename = input("Введите новое название файла: ")
rename += '.txt'

os.rename(os.path.join(text_folder, 'test1.txt'), rename)
os.replace(rename, os.path.join(text_folder, rename))

print(f"В папке ({text_folder}) файл test1.txt был переименован в {rename}")

