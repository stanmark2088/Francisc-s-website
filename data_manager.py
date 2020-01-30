import csv

def read_csv(file):
    with open(file, 'r') as csv_file:
        lst = []
        reader = csv.DictReader(csv_file)
        for row in reader:
            lst.append(row)
    return lst


def append_to_csv(file, fields):
    with open(file, 'a', newline='') as csv_data:
        writer = csv.writer(csv_data)
        writer.writerow(fields)


def get_id(id):
    dict_with_products = read_csv('data/products.csv')
    for row in dict_with_products:
        if int(row['id']) == int(id):
            return row

def generate_value(type, file):
    dict_order = read_csv(file)
    lst = []
    for row in dict_order:
        lst.append(int(row[type]))
    return len(lst) + 1











