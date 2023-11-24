import csv


def generate_csv(columns, data, path, delimiter=","):
    """
    Generate a CSV file using the csv module.

    :param columns: List of column headers for the CSV.
    :param data: List of rows, where each row is a list of values corresponding to the columns.
    :param path: Path where the CSV file will be saved.
    :param delimiter: Delimiter used to separate values in the CSV. Default is comma (',').
    """
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)

        writer.writerow(columns)

        for row in data:
            writer.writerow(row)


def read_text_file(file_path: str) -> str:
    """
    Reads the contents of a text file and returns it as a string.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The contents of the file as a string.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If an error occurs during file reading.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")
