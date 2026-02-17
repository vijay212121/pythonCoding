import pandas as pd
import re
from collections import Counter


def retrieve_group_data(file_path, sheet_name, group_identifier):
    """
    :param file_path: The path to the Excel file
    :param sheet_name: The name of the sheet in the Excel file
    :param group_identifier:  A keyword used to search for specific data in the sheet
    :return: dict
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name, dtype=str)

    comments_column = df['Comments and Work notes'].fillna('')

    pattern = rf"{group_identifier} : \[code\]<I>(.*?)</I>\[/code\]"

    groups_list = []
    for text in comments_column:
        matches = re.findall(pattern, text)
        for match in matches:
            groups_list.append(match)

    group_counts = Counter(group.strip() for group in groups_list)

    return dict(group_counts)


_file_path = r"C:\Users\vijay kumar\Downloads\coding challenge test (1).xlsx"
_sheet_name = "Input Data sheet"
field_search = "Groups"
result = retrieve_group_data(_file_path, _sheet_name, field_search)
print(f"Group name\t - Number of occurences")
for grp_name, grp_count in result.items():
    print(f"{grp_name}\t - {grp_count}")


