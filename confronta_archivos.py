import csv


def combinar_csv(csv1, csv2, csv_merged):
    filas_combinadas = []
    encabezados = None

    with open(csv1, mode="r", encoding="utf-8") as file1:
        reader1 = csv.DictReader(file1)
        encabezados = reader1.fieldnames
        filas_combinadas.extend(reader1)

    with open(csv2, mode="r", encoding="utf-8") as file2:
        reader2 = csv.DictReader(file2)
        if reader2.fieldnames != encabezados:
            raise ValueError("No coinciden los encabezados de los archivos")
        filas_combinadas.extend(reader2)

    filas_unicas = {tuple(fila.items()): fila for fila in filas_combinadas}.values()

    with open(csv_merged, mode="w", encoding="utf-8", newline="") as file_salida:
        writer = csv.DictWriter(file_salida, fieldnames=encabezados)
        writer.writeheader()
        writer.writerows(filas_unicas)

    print("Merge file succes " + csv_merged)


def main():
    csv1 = "curps_validas.csv"
    csv2 = "curps_invalidas.csv"
    csv_merged = "curps.csv"
    combinar_csv(csv1, csv2, csv_merged)


if __name__ == "__main__":
    main()
