import os

def split_large_file(input_file, chunk_size=100 * 1024 * 1024):
    # Get the file size
    file_size = os.path.getsize(input_file)

    # Calculate the number of chunks needed
    num_chunks = (file_size + chunk_size - 1) // chunk_size

    # Read and split the file
    with open(input_file, 'rb') as infile:
        for chunk_number in range(num_chunks):
            chunk_data = infile.read(chunk_size)
            chunk_filename = f"{input_file}.part{chunk_number + 1}"
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(chunk_data)

    os.remove(input_file)
    print(f"Split {input_file} into {num_chunks} chunks.")

# Usage example:
folder_path = './'
for root, _, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.getsize(file_path) > 100 * 1024 * 1024:
            split_large_file(file_path)
