import os
import generating_files
from generating_files import list_of_source_extensions
# generating_files.renameming( 10, list_of_source_extensions)

def renaming(desired_final_file_name: str, final_extension: str, period: range):
    count = 0
    for i in os.listdir('d:/Mytraining/Dive_into_Python/DZ_7/Task_DZ_7/Work_dir'):
        count += 1
        a = str(os.rename(i, f'{i[3:6]}{desired_final_file_name}{count}.{final_extension}'))
    return 


if __name__ == '__main__':
    
    print(renaming('file',  'txt', range(3, 6)))