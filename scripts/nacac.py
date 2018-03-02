from pandas import DataFrame, read_csv

#G_SHEET_TEMPLATE = 'https://spreadsheets.google.com/feeds/cells/%s/%s/public/values?range=%s&alt=json'
G_SHEET_TEMPLATE = 'https://docs.google.com/spreadsheets/d/%s/gviz/tq?headers=2&sheet=%s&range=%s&tqx=out:csv;'
def get_sheet_url(sp_id, ws, cell_range):
    s = G_SHEET_TEMPLATE % (sp_id, ws, cell_range)
    return (s)

NACAC_SPREADSHEET = {
        'sp_id': '1M6BuL3BQQ2KufJYfpIUjDrnJSSK7zOAY4aNs0dPdKbs',
        'ws': 'Data',
        'cell_range':'A1:G500'
        }


def get():
    df = read_csv( get_sheet_url(**NACAC_SPREADSHEET), header=0)
    df = df.rename(index=str, columns={"State CategoryFilter":"State", "Country CategoryFilter":"Country"})
    return df


def main():
    df = get()
    print(df)


if __name__ == '__main__':
    main()
