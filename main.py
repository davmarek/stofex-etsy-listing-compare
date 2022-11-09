import pandas as pd

ETSY_CSV_FILEPATH = "EtsyListingsDownload.csv"
ETSY_INCLUDE_VARIANTS = True

EXPORT_NEW_CSV_FILEPATH = "SKLAD_NAPA_711.csv"
EXPORT_SKU_COLUMN_NAME = "Čárový kód"
EXPORT_QUATITY_COLUMN_NAME = "Stav zásoby"


def get_etsy_data() -> dict:
    df = pd.read_csv(ETSY_CSV_FILEPATH)

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

    for _, row in df.iterrows():
        sku_col: str = row["SKU"]

        # products with NO VARIANTS
        if "," not in sku_col:
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
            etsy_data[sku] = {
                "quantity": row["QUANTITY"],
                "title": row["TITLE"]
            }

    return etsy_data


def get_export_data(etsy_keys) -> dict:
    df = pd.read_csv(EXPORT_NEW_CSV_FILEPATH, delimiter=";")

    export_data = {}

    for _, row in df.iterrows():
        sku = row[EXPORT_SKU_COLUMN_NAME]
        if sku in etsy_keys:
            export_data[sku] = row[EXPORT_QUATITY_COLUMN_NAME]

    return export_data


def main():
    etsy_data = get_etsy_data()
    export_data = get_export_data(etsy_data.keys())

    for sku in etsy_data.keys():
        etsy_q = etsy_data[sku]["quantity"]

        try:
            export_q = export_data[sku]
        except KeyError:
            print(
                f'{sku} z Etsy není v exportu ({etsy_data[sku]["title"][:35].rstrip()})')
            continue

        if type(etsy_q) is not int:
            etsy_q = int(etsy_q.split(",")[0])

        if type(export_q) is str:
            export_q = int(export_q.split(",")[0])

        continue  # (un)comment aby (ne)vypisovalo docházení
        if (etsy_q/100) > export_q:
            print(
                f"\n{sku} dochází",
                f"\tna Etsy: {etsy_q}",
                f"\tv exportu: {export_q}",
                sep="\n",
                end="\n\n"
            )


if __name__ == "__main__":
    main()
