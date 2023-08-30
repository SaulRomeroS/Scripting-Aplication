#Saul Romero Soto
#A01351663

import csv



def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w', newline='') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def main(source_filename, batch_filename, output_filename):
    source_data = read_csv_to_dict(source_filename)
    batch_data = read_csv_to_dict(batch_filename)
    inventory = {item['SKU']: item for item in source_data}
    
    for item in batch_data:
        sku = item['SKU']
        if sku in inventory:
            inventory[sku]['Quantity'] = str(int(inventory[sku]['Quantity']) + int(item['Quantity']))
        else:
            inventory[sku] = item
    
    write_list_of_dicts_to_csv(output_filename, list(inventory.values()))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('sample_grocery.csv', 'grocery_batch_1.csv', 'grocery_db.csv')
