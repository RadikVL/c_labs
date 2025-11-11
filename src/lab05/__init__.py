import argparse

from cvs_xlsx import * # include module JSON ↔ CSV
from json_csv import * # include module CSV → XLSX

def main():
    parser = argparse.ArgumentParser(description='Генерация текстовых отчетов')
    parser.add_argument('--in', dest='input_file', nargs='+', help='Входные файлы')
    parser.add_argument('--out', dest='output_file', nargs='+', help='Выходной файл для отчета')
    # parser.add_argument('--wt', dest='work_type', nargs='+', help='Mode of work')


    args = parser.parse_args()

    input_file = args.input_file[0]
    output_file = args.output_file[0]

    try:
        # csv_to_xlsx(input_file, output_file)
        json_to_csv(input_file, output_file)
        # csv_to_json(input_file, output_file)
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    main()