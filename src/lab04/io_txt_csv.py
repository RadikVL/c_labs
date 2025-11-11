import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Reads and returns the content of a text file at the given path using the specified encoding. Default encoding is 'utf-8'.

    Parameters:
    path (str | Path): Path to the text file.
    encoding (str): Encoding to use when reading the file (default is 'utf-8').

    Returns: 
    str: Content of the text file as a string.
    '''
    file_path = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return file_path.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    ''' 
    Writes data to a CSV file at the specified path. Creates parent directories if they don't exist.

    Parameters:
    rows (Iterable[Sequence]): Iterable containing data rows to write.
    path (str | Path): Path where the CSV file will be created.
    header (tuple[str, ...] | None): Optional header row for the CSV file.

    Raises:
    ValueError: If rows have inconsistent lengths.
    '''
    file_path = Path(path)
    rows_list = list(rows)
    
    # Validate that all rows have the same length
    if rows_list:
        first_row_length = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_row_length:
                raise ValueError(f"Row {i} has length {len(row)}, expected {first_row_length}")
    
    # Create parent directories if they don't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write CSV file
    with file_path.open('w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows_list)


def ensure_parent_dir(path: str | Path) -> None:
    ''' 
    Creates parent directories for the given path if they don't exist.

    Parameters:
    path (str | Path): File path for which to create parent directories.
    '''
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)