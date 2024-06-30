import os

def combine_split_files(input_folder):
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.part1'):
                original_filename = file[:-6]  # Remove the ".part1" suffix
                combined_file_path = os.path.join(root, original_filename)
                print("Combining",combined_file_path)
                if not os.path.exists(combined_file_path):
                    with open(combined_file_path, 'ab') as combined_file:
                        chunk_number = 1
                        while True:
                            chunk_filename = os.path.join(root, f"{original_filename}.part{chunk_number}")
                            if os.path.exists(chunk_filename):
                                with open(chunk_filename, 'rb') as chunk_file:
                                    combined_file.write(chunk_file.read())
                                chunk_number += 1
                            else:
                                break  # Exit the inner loop when no more chunks are found

                    # Delete the split files
                    for i in range(1, chunk_number):
                        split_file_path = os.path.join(root, f"{original_filename}.part{i}")
                        if os.path.exists(split_file_path):
                            os.remove(split_file_path)

    print(f"Combined split files in {input_folder} and deleted split parts.")

# Usage example:
folder_path = './'
combine_split_files(folder_path)
