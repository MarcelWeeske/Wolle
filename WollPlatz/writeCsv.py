import csv


def writeCsv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for row in data:
            csv_writer.writerow(row)