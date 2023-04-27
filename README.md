# Address Parser using NLP Techniques 

This Python script defines a class Address that works with different address formats and their elements. Given an address string, it extracts the street name, house number, postal code, and city name, and returns a dictionary containing these elements. The script also writes the output dictionary to a JSON file.

Address parsing is a common task in natural language processing (NLP), which involves extracting structured information from unstructured text. This script can serve as a basic example of how NLP techniques can be used to parse and extract information from addresses.

# Installation

To use this script, you need to have Python 3 installed on your computer. You can download the latest version of Python from the official website: https://www.python.org/downloads/

In addition, you need to install the json module, which is included in the standard library of Python. No other external packages or libraries are required.

# Usage

To use this script, you can clone this repository or download the address_parser.py file to your local machine.

Then, open a command prompt or terminal window and navigate to the directory where the address_parser.py file is located.

To run the script, enter the following command:

```python address_parser.py```

This will execute the script and print the output dictionary to the console. It will also write the output to a JSON file named "Output.json" in the same directory as the script.

To use this script with a different address string, you can modify the AddressObject variable in the main section of the script:

```AddressObject = Address("Berliner Straße 99, Berlin 39422")```

Replace the address string with your own address string, and then run the script as described above.

# Contributing
If you find a bug or have a suggestion for improvement, please create a new issue in the repository. If you would like to contribute code, you can create a new branch, make your changes, and submit a pull request.
