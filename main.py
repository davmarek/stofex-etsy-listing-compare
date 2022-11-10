import pandas as pd

ETSY_CSV_FILEPATH = "EtsyListingsDownload.csv"
ETSY_INCLUDE_VARIANTS = True

EXPORT_NEW_CSV_FILEPATH = "SKLAD_NAPA_9.11.csv"
EXPORT_SKU_COLUMN_NAME = "Čárový kód"
EXPORT_QUATITY_COLUMN_NAME = "Stav zásoby"


def get_etsy_data() -> dict[str, int]:
    try:
        df = pd.read_csv(ETSY_CSV_FILEPATH)
    except Exception:
        print(f"Soubor \"{ETSY_CSV_FILEPATH}\" nenalezen")
        exit(1)

    df.pop("DESCRIPTION")
    df.pop("PRICE")
    df.pop("CURRENCY_CODE")
    df.pop("TAGS")
    df.pop("MATERIALS")
    df.pop("IMAGE1")
    df.pop("IMAGE2")
    df.pop("IMAGE3")
    df.pop("IMAGE4")
    df.pop("IMAGE5")
    df.pop("IMAGE6")
    df.pop("IMAGE7")
    df.pop("IMAGE8")
    df.pop("IMAGE9")
    df.pop("IMAGE10")

    etsy_data = {}
    duplicate_sku = []

    for _, row in df.iterrows():
        sku_col: str = row["SKU"]

        # products with NO VARIANTS
        if "," not in sku_col:
            if sku_col in etsy_data.keys():
                duplicate_sku.append(
                    f'{sku_col} je v Etsy vícekrát\n' +
                    f'\t{row["TITLE"]}\n' +
                    f'\t{etsy_data[sku_col]["title"]}'
                )

            etsy_data[sku_col] = {
                "quantity": row["QUANTITY"],
                "title": row["TITLE"]
            }
            continue

        # products WITH VARIANTS
        if not ETSY_INCLUDE_VARIANTS:
            continue

        sku_list = sku_col.split(",")
        for sku in sku_list:
            if sku in etsy_data.keys():
                # print(sku)
                # print(etsy_data.keys())
                duplicate_sku.append(
                    f'{sku} je v Etsy vícekrát\n' +
                    f'\t{row["TITLE"]}\n' +
                    f'\t{etsy_data[sku]["title"]}'
                )

            etsy_data[sku] = {
                "quantity": row["QUANTITY"],
                "title": row["TITLE"]
            }

    for dupl in duplicate_sku:
        print(dupl)

    return etsy_data


def get_export_data(etsy_keys) -> dict[str, int]:
    try:
        df = pd.read_csv(EXPORT_NEW_CSV_FILEPATH, delimiter=";")
    except Exception:
        print(f"Soubor \"{EXPORT_NEW_CSV_FILEPATH}\" nenalezen")
        exit(1)

    export_data = {}

    for _, row in df.iterrows():
        sku = row[EXPORT_SKU_COLUMN_NAME]
        if sku in etsy_keys:
            q = int(row[EXPORT_QUATITY_COLUMN_NAME].split(",")[0])
            export_data[sku] = q

    return export_data


def report_etsy_sku_problems(etsy_data, export_data):
    sku_problems: list[str] = []

    for etsy_sku in etsy_data.keys():
        # quantity of current Etsy product
        etsy_q = etsy_data[etsy_sku]["quantity"]

        # try getting quantity of the same product from export data
        try:
            export_q = export_data[etsy_sku]
        except KeyError:
            # error raised if the SKU IS NOT in export
            # title of the Etsy product
            title = etsy_data[etsy_sku]["title"][:35].rstrip()
            sku_problems.append(
                f'{etsy_sku:<13} z Etsy není v exportu ({title})'
            )
            continue

        """
        if type(etsy_q) is not int:
            etsy_q = int(etsy_q.split(",")[0])

        continue  # (un)comment aby (ne)vypisovalo docházení
        if (etsy_q/100) > export_q:
            print(
                f"\n{etsy_sku} dochází",
                f"\tna Etsy: {etsy_q}",
                f"\tv exportu: {export_q}",
                sep="\n",
                end="\n\n"
            )
        """

    for problem in sku_problems:
        print(problem)
    print("Celkem SKU problémů:", len(sku_problems))


def main():
    etsy_data = get_etsy_data()
    export_data = get_export_data(etsy_data.keys())

    report_etsy_sku_problems(etsy_data, export_data)


if __name__ == "__main__":
    main()
