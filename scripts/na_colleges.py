from pandas import DataFrame
import json
import requests

G_SHEET_TEMPLATE = 'https://spreadsheets.google.com/feeds/cells/%s/%s/public/values?range=%s&alt=json'

def get_sheet_url(sp_id, ws_id, cell_range):
    s = G_SHEET_TEMPLATE % (sp_id, ws_id, cell_range)
    return (s)

NA_COLLEGES_SPREADSHEET = {
        'sp_id': '1J2R1ABpUoFSC3USeOOv5kpmyA7Ilw1D3aFinc1pW0yg',
        'ws_id': '3',
        'cell_range':'A3:O500'
        }

NA_COLLEGES_HEADER  = {
      "1":'id',
      "2":'name',
      "3":'city',
      "4":'state',
      "5":'size',
      "6":'alias',
      "7":'location',
      "8":'photo',
      "9":'twitter',
      "10":'email',
      "11":'hasConfirm',
      "12":'link',
      "13":'tweet',
      "14":'date',
      "15":'score',
      }

def get():

    r = requests.get(get_sheet_url(**NA_COLLEGES_SPREADSHEET))
    colleges = {}
    sheet = json.loads(r.text)
    for e in sheet.get('feed').get('entry'):
        e_row = e.get('gs$cell').get('row')
        e_col = e.get('gs$cell').get('col')
        if not colleges.get(e_row):
            colleges[e_row] = {}
        colleges[e_row][NA_COLLEGES_HEADER[e_col]] = e.get('gs$cell').get('$t')
    colleges = clean(colleges)
    df = DataFrame(colleges)
    return df

def clean(colleges):

    col_list = []
    for c in colleges:
        if colleges[c].get('name') is None:
            continue
        colleges[c]['alias'] = colleges[c].get('alias').split(',')
        col_list.append(colleges[c])
    return col_list
def main():
    df = get()
    print(df)


if __name__ == '__main__':
    main()
