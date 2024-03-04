import os

def split_file(input_file, output_folder, chunk_size_mb=25):
    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    with open(input_file, 'rb') as f:
        chunk_number = 1
        while True:
            chunk_data = f.read(chunk_size_bytes)
            if not chunk_data:
                break
            output_file_path = os.path.join(output_folder, f'{os.path.basename(input_file)[:-4]}_{chunk_number}.txt')
            with open(output_file_path, 'wb') as chunk_file:
                chunk_file.write(chunk_data)
            chunk_number += 1

        # Sprawdź czy istnieje jeszcze jakieś dane w buforze
        remaining_data = f.read()
        if remaining_data:
            output_file_path = os.path.join(output_folder, f'{os.path.basename(input_file)[:-4]}_{chunk_number}.txt')
            with open(output_file_path, 'wb') as chunk_file:
                chunk_file.write(remaining_data)

# Przykładowe użycie:
input_file_path = 'files_to_split/test1.txt'
output_folder_path = 'files_ready'

split_file(input_file_path, output_folder_path)
