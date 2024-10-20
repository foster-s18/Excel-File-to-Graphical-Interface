import pandas as pd

# Load sheet 2 containing breaks information of Excel file as DataFrame
break_info_df = pd.read_excel('CLIENT INFORMATION.xlsx', sheet_name=1)

# create a csv file and covert DataFrame to csv
csv_file = 'break_information.csv'  # Desired CSV file name
break_info_df.to_csv(csv_file, index=False)

# function to process breaks csv file
def breaks():
    infile = open('break_information.csv', 'r', encoding='utf-8-sig')
    data_dict = {}
    in_quotes = False

    # loop to cycle through each row and process/edit information
    for row in infile:
        if not row.startswith("Client") and not row.startswith(","):
            row = row.rstrip("\n")

            # Custom split function to handle commas inside quotes
            parts = []
            current_part = ''

            for char in row:
                if char == '"':
                    in_quotes = not in_quotes
                elif char == ',' and not in_quotes:
                    parts.append(current_part)
                    current_part = ''

                else:
                    current_part += char

            parts.append(current_part)

            # Extracting client name and info
            key = parts[0].strip()
            my_list = parts[1:]

            data_dict[key] = my_list

            for i in range(len(my_list)):
                if my_list[i] == 'ZERO':
                    my_list[i] = '0'
                if my_list[i] == '':
                    my_list[i] = '-'
                if my_list[i].__contains__("ZERO"):
                    my_list[i] = my_list[i].replace("ZERO", "0")

    return data_dict
