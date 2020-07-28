#import utils.file_operations
#utils.file_operations.save_to_file('Rolf','data.txt')

from utils.common.file_operations import save_to_file, read_file
save_to_file('Rolf','data.txt')
print(read_file('data.txt'))

print(__name__)
