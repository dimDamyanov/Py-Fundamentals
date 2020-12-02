file_path = input()
file = file_path[file_path.rfind('\\') + 1:]
filename = file[:file.find('.')]
file_ext = file[file.find('.') + 1:]
print(f'File name: {filename}')
print(f'File extension: {file_ext}')
