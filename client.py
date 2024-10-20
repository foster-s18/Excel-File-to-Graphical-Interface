import pandas as pd

# Load sheet 1 containing client information of Excel file as DataFrame
client_info_df = pd.read_excel('CLIENT INFORMATION.xlsx', sheet_name=0)

# create a csv file and covert DataFrame to csv
csv_file = 'client_information.csv'  # Desired CSV file name
client_info_df.to_csv(csv_file, index=False)


# function for processing client information csv file.
def client():
    infile = open('client_information.csv', 'r', encoding='utf-8-sig')
    client_list = []
    data_dict = {}

    # loop to cycle through each row and process/edit information
    for row in infile:
        if not row.startswith("Client") and not row.startswith(","):
            data = row.rstrip("\n").split(",")  # store each row in variable, removing new lines and split on ','.
            key = data[0].strip()  # store index[0] as key(client name) and strip leading and trailing whitespace

            if data[1] == "ONE-ONE":
                data[1] = "1-1"
            if data[2].strip().lower() in ["", "x", "-"]:
                data[2] = "No Preference"
            elif data[2] == "FEMALE":
                data[2] = "Female Only"
            elif data[2] == "MALE":
                data[2] = "Male Only"
            if data[3].strip().lower() in ["", "x", "-"]:
                data[3] = "ETC staff allowed"
            elif data[3].strip().lower() in ["y", "yes"]:
                data[3] = "ETC staff allowed"
            elif data[3].strip().lower() in ["n", "no"]:
                data[3] = "No ETC staff"
            if data[4].strip().lower() in ["", "x", "-"]:
                data[4] = "Not Required"
            elif data[4].strip().lower() in ["n", "no"]:
                data[4] = "Not required"
            elif data[4].strip().lower() in ["y", "yes"]:
                data[4] = "Required"


            temp_list = data[1:]    # take all info for each entry bar 1st word in split string(key) and add to list
            data_dict[key] = temp_list    # store all info in my list to dict key(1st word in split string)

            for i in range(len(temp_list)):
                if temp_list[i].strip().lower() in ["", "x", "-"]:
                    temp_list[i] = 'Confirm with client'

    for k, v in data_dict.items():
        client_list.append(k)

    infile.close()
    print(data_dict)
    return client_list, data_dict

client()