from openpyxl import Workbook
from openpyxl.workbook.defined_name import DefinedName

# Create a new workbook
workbook = Workbook()

# Create Sheet1 and add the "Parameters" data
sheet1 = workbook.active
sheet1.title = "Parameters"
sheet1.append(["Key", "Value"])
sheet1.append(["param1", 10])
sheet1.append(["param2", "[SubParameters]"])  # Use [SubParameters] to indicate a named range
sheet1.append([None, 20])
sheet1.append([None, 30])
sheet1.append(["param3", 40])

# Define the "Parameters" named range
parameters_range = DefinedName(name="Parameters", attr_text="Parameters!$A$1:$B$5")
workbook.defined_names.add(parameters_range)

# Create Sheet2 and add the "SubParameters" data
sheet2 = workbook.create_sheet("SubParameters")
sheet2.append(["Key", "Value"])
sheet2.append(["subparam1", 100])
sheet2.append(["subparam2", 200])

# Define the "SubParameters" named range (corrected range: A2:B3)
subparameters_range = DefinedName(name="SubParameters", attr_text="SubParameters!$A$2:$B$3")
workbook.defined_names.add(subparameters_range)

# Save the workbook
file_name = "example.xlsx"
workbook.save(file_name)
print(f"Excel file '{file_name}' created successfully.")