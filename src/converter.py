import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        if len(data) > 0:
            csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(data)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert CSV to JSON and JSON to CSV.")
    parser.add_argument("input_file", help="Path to the input file (CSV or JSON).")
    parser.add_argument("output_file", help="Path to the output file (JSON or CSV).")
    args = parser.parse_args()

    if args.input_file.endswith('.csv') and args.output_file.endswith('.json'):
        csv_to_json(args.input_file, args.output_file)
    elif args.input_file.endswith('.json') and args.output_file.endswith('.csv'):
        json_to_csv(args.input_file, args.output_file)
    else:
        print("Invalid file types. Please provide a CSV file as input and a JSON file as output or vice versa.")
