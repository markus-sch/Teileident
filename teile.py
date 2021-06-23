import csv


def main():
    part_number = ''
    file_name = ''

    # with open('TeileIdent_20210520104152.CSV') as handle:
    #     for line in handle:
    #         split_line = line.split(';')
    #         file_name = f'TeileIdent_{split_line[1]}'
    #         if part_number != split_line[1]:
    #             part_number = split_line[1]
    #             print('Hier muss eine neue Datei erzeugt werden')
    #             file_name = f'Teileident_{split_line[1]}'
    #             print(f'Der Dateiname lautet {file_name}')
    #
    #         print(line)

    with open('TeileIdent_20210520104152.CSV') as handle:
        for line in handle:
            print(type(line))
            print(f'ohne csv: {line}')


    with open('TeileIdent_20210520104152.CSV', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            with open('markus.csv','w', newline='') as csvwritefile:
                csvwriter = csv.writer(csvwritefile, delimiter='\n')
                csvwriter.writerow(row)
            # print(type(row))
            # print(f'csv-Modul: {row}')


    for row in csv.reader(['one,two,three']):
        print(row)

main()

# TODO: Verzeichnis nach Dateien scannen (ohne Unterverzeichnisse)
# TODO: Originaldatei nach Verarbeitung löschen
# TODO: Daten in die unterschiedlichen Zieldateien schreiben.
