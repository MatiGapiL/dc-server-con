import os
def create_text_file_2(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Plik tekstowy o nazwie '{file_path}' został pomyślnie utworzony.")
    except Exception as e:
        print(f"Wystąpił błąd podczas tworzenia pliku: {e}")

# Ścieżka i nazwa pliku, który chcesz utworzyć
file_path = "files_to_split/example.txt"

# Zawartość pliku
content = """ngml""" * (6553599 * 1 + 500) # o jedno mniej żeby nie było 25mb
for i in range(1, 2):
    file_path = f"files_to_split/test{i}.txt"
    create_text_file_2(file_path, content)

#kawałek kodu do sprawdzania 1 pliku (chyba)
folder_path_to_c = "files_to_split"
files = os.listdir(folder_path_to_c)
if files:
    first_file_name = files[0]

print(first_file_name)


