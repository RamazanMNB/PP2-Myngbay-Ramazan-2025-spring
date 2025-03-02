import os

file_path = "input.txt"  


if os.path.exists(file_path):
    
    if os.access(file_path, os.R_OK | os.W_OK):
        os.remove(file_path)  
        print("Файл успешно удалён.")
    else:
        print("Нет доступа к файлу.")
else:
    print("Файл не найден.")
