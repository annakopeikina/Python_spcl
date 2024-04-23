import os
from gen_name import generate_scenic_names
from rnd_num import generate_number_file
from numb_name_multiply import multiply_and_save 

if __name__ == '__main__':
    directory = "C:\\Users\\akopeikina\\OneDrive\\Desktop\\Python_spcl\\seminar7_files"
    names_file = "scenic_names.txt"
    numbers_file = "random_numbers.txt"
    output_file = "multiplication_names_numbers.txt"
    print(multiply_and_save(os.path.join(directory, names_file), os.path.join(directory, numbers_file), os.path.join(directory, output_file)))
