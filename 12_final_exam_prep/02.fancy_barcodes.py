import re


def identifying_barcode_group(one_barcode: str):
    product_group = 'Product group: '
    barcode_group = ''
    for ch in one_barcode:
        if ch.isnumeric():
            barcode_group += ch
    if not barcode_group:
        barcode_group = '00'
    product_group += barcode_group
    return product_group


def validating_barcodes(barcodes_dict: dict):
    pattern = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])\1'
    for current_barcode in barcodes_dict.keys():
        current_match = re.search(pattern, current_barcode)
        if current_match:
            barcodes_dict[current_barcode] = identifying_barcode_group(current_barcode)
        else:
            barcodes_dict[current_barcode] = 'Invalid barcode'
        print(barcodes_dict[current_barcode])
    return barcodes_dict


all_barcodes_dict = {}
num_of_inputs = int(input())
for line in range(num_of_inputs):
    all_barcodes_dict[input()] = ''

all_barcodes_dict = validating_barcodes(all_barcodes_dict)
