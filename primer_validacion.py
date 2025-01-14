import csv
from curp import CURP


def validar_curp(curp):
    try:
        CURP(curp)
        return True
    except Exception:
        return False


def procesar_csv(input_file, output_validas, output_invalidas):
    with (
        open(input_file, mode="r", encoding="utf-8") as infile,
        open(output_validas, mode="w", encoding="utf-8", newline="") as validas_file,
        open(
            output_invalidas, mode="w", encoding="utf-8", newline=""
        ) as invalidas_file,
    ):

        reader = csv.DictReader(infile)
        fieldNames = reader.fieldnames
        validas_writer = csv.DictWriter(validas_file, fieldnames=fieldNames)
        invalidas_writer = csv.DictWriter(invalidas_file, fieldnames=fieldNames)

        validas_writer.writeheader()
        invalidas_writer.writeheader()

        for row in reader:
            curp = row.get("curp", "").strip()
            if validar_curp(curp):
                validas_writer.writerow(row)
            else:
                invalidas_writer.writerow(row)
    print("Curps verificadas")


def main(input_file, output_validas, output_invalidas):
    input_file = ""
    output_validas = ""
    output_invalidas = ""
    procesar_csv(input_file, output_validas, output_invalidas)


if __name__ == "__main__":
    main()
