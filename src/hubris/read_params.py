import sys

import openpyxl

def extract_values(sheet, range_spec):
    result = []
    for row in sheet[range_spec]:
        result.append([c.value for c in row])
    return result

def named_range_values(wb, range_name):
    range_def = wb.defined_names[range_name]
    reference = range_def.attr_text
    sheet_name, range_spec = reference.split("!")
    return extract_values(wb[sheet_name], range_spec)

def dict_range(workbook,range_name):
    # Get the named range
    if range_name not in workbook.defined_names:
        raise ValueError(f"Named range '{range_name}' not found in the workbook.")

    # Get the rows in the named range
    rows = named_range_values(workbook, range_name)

    # Initialize the result dictionary
    result = {}
    i = 0

    while i < len(rows):
        # Get the current row
        key, value = rows[i]

        # Skip empty rows, but complain about floating values
        if key is None:
            if value is None:
                i += 1
                continue
            else:
                raise ValueError("Empty key not expected on value {value!r}: programming error?")

        # Check if the value is a range name enclosed in braces: dictionary
        if value.startswith("{") and value.endswith("}"):
            # Extract the named range name (e.g., "SubParameters" from "{SubParameters}")
            ref_range_name = value[1:-1]
            if ref_range_name in workbook.defined_names:
                # Recursively process the referenced named range
                result[key] = named_range_values(workbook, ref_range_name)
                i += 1  # Ensure the loop advances after processing the nested range
            else:
                raise ValueError(f"Named range {ref_range_name!r} not found in the workbook.")
        # Otherwise "[name]" references a list or matrix "name"
        elif value.startswith("[") and value.endswith("]"):
            ref_range_name = value[1:-1]
            result[key] = named_range_values(workbook, ref_range_name)
            i += 1
        else:
            # Single value
            result[key] = value
            i += 1

    return result

def read_file(file_name, range_name="Parameters"):
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(file_name, data_only=False)
    return dict_range(workbook, range_name)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Requires spreadsheet arguments")
    if len(sys.argv) > 3:
        sys.exit("Sorry, only handling one or two arguments for now")
    from pprint import pprint
    data = read_file(*sys.argv[1:])
    pprint(data)
