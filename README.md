# File Converter

A tool for converting CSV files to JSON and vice versa.

## Usage

**Convert CSV to JSON**:
```
python src/converter.py input.csv output.json
```
**Convert JSON to CSV**:
```
python src/converter.py input.json output.csv
```

## Requirements
`Python 3x`

## Install and Run the tool
```
git clone https://github.com/sekuja/file_converter.git
```
```
cd file_converter
```
**To convert a CSV file to JSON, use the following command**:
```
python src/converter.py path/to/input.csv path/to/output.json
```
**Example**:
```
python src/converter.py example.csv example.json
```
**To convert a JSON file to CSV, use the following command**:
```
python src/converter.py path/to/input.json path/to/output.csv
```
**Example**:
```
python src/converter.py example.json example.csv
```
## Explanation
• `path/to/input.csv`: Replace with the path to the CSV file you want to convert.
• `path/to/output.json`: Replace with the path where you want to save the converted JSON file.
• `path/to/input.json`: Replace with the path to the JSON file you want to convert.
• `path/to/output.csv`: Replace with the path where you want to save the converted CSV file.

## Example
If you have a CSV file named `data.csv` in the same directory as the script and want to convert it to `data.json`, you will run:
```
python src/converter.py data.csv data.json
```
If you have a JSON file named `data.json` in the same directory as the script and want to convert it to `data.csv`, you will run:
```
python src/converter.py data.json data.csv
```
## Conclusion
By following the steps above, you can easily convert CSV files to JSON and vice versa using this conversion tool.
