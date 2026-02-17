def write_data(_file_name, mode):
    data_list =["vijay","kumar"]
    with open(file_name, mode) as file:
        for data in data_list:
            file.writelines(f"{data}\n")
        file.seek(0)
        return file.readlines()




file_name = "practice.txt"
print(write_data(file_name, 'w+'))
#
# with open(file_name, "r") as file_r:
#     with open ("practice2.txt", "w") as file_w:
#         for line in file_r:
#             file_w.writelines(line)

