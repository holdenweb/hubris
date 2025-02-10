import unittest
import openpyxl
from write_params import dict_to_spreadsheet
from read_params import read_file

class TestSpreadsheetFunctions(unittest.TestCase):

    def test_round_trip(self):
        test_data = {
            "products": {
                "electronics": {
                    "phones": ["iPhone 13", "Samsung Galaxy S22"],
                    "laptops": ["MacBook Pro", "Dell XPS"]
                },
                "clothing": {
                    "shirts": ["T-shirt", "Dress shirt"],
                    "pants": ["Jeans", "Dress pants"],
                    "accessories": {
                        "hats": ["Baseball Cap"],
                        "shoes": ["Sneakers"]
                    }
                }
            },
            "customer_info": {
                "name": "Jane Doe",
                "orders": [
                    {"product": "iPhone 13", "quantity": 1},
                    {"product": "MacBook Pro", "quantity": 1}
                ]
            }
        }

        output_filename = "round_trip_test.xlsx"

        dict_to_spreadsheet(test_data, output_filename)
        read_back_data = read_file(output_filename)

        self.assertEqual(test_data, read_back_data)

    def test_simple_dict(self):
        data = {"name": "Alice", "age": 30, "city": "London"}
        filename = "test_simple.xlsx"
        dict_to_spreadsheet(data, filename)
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        self.assertEqual(sheet["A1"].value, "name")
        self.assertEqual(sheet["B1"].value, "Alice")
        self.assertEqual(sheet["A2"].value, "age")
        self.assertEqual(sheet["B2"].value, 30)
        self.assertEqual(sheet["A3"].value, "city")
        self.assertEqual(sheet["B3"].value, "London")

    def test_nested_dict(self):
        data = {
            "products": {
                "electronics": {
                    "phones": ["iPhone 13", "Samsung Galaxy S22"],
                    "laptops": ["MacBook Pro", "Dell XPS"]
                }
                #... other data can be added here
            }
        }
        filename = "test_nested.xlsx"
        dict_to_spreadsheet(data, filename)
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        self.assertEqual(sheet["A1"].value, "products")
        self.assertEqual(sheet["B1"].value, "[products]")  # Check named range reference
        #... assertions to check nested data and named ranges can be added here

    def test_list_values(self):
        data = {"items": ["apple", "banana", "cherry"]}
        filename = "test_list.xlsx"
        dict_to_spreadsheet(data, filename)
        #... assertions to check list values

    def test_different_data_types(self):
        data = {"name": "Bob", "age": 25, "active": True, "height": 1.80}
        filename = "test_data_types.xlsx"
        dict_to_spreadsheet(data, filename)
        #... assertions to check different data types

if __name__ == '__main__':
    unittest.main()