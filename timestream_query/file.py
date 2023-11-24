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

        # Write the header
        writer.writerow(columns)

        # Write the data rows
        for row in data:
            writer.writerow(row)
