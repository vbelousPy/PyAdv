import csv


def csv_reader(file_name):
    my_dict = dict()
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        title = 1
        for row in reader:
            for i in range(len(row)):
                current_number = row[i]
                if my_dict.get("#" + str(title)) is None or current_number > my_dict.get("#" + str(title)):
                    my_dict.update({"#" + str(title):current_number})
            title +=1
    return my_dict

# def json_writer
# csv_reader("my. ncsv")
print(csv_reader("my.csv"))
