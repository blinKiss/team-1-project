import os

folder_path = './team-1-project/data/tags'  # 폴더 경로를 지정해주세요
file_names = []

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'): 
        name = os.path.splitext(filename)[0] 
        file_names.append(name)

print(file_names)