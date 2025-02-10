import write_params  # Your module
import read_params  # Your module

def test_round_trip():
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

    write_params.dict_to_spreadsheet(test_data, output_filename)
    read_back_data = read_params.read_file(output_filename)
    try:
        assert test_data == read_back_data, "Round-trip data mismatch!"
    except AssertionError:
        from pprint import pprint
        print("Test Data")
        pprint(test_data)
        print("Read back data")
        pprint(read_back_data)

    print("Round-trip test passed!")

test_round_trip()