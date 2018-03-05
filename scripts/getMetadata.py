import na_colleges

import requests
import json
import urllib


secrets = json.loads(open('secret.json').read())

COLLEGE_SCORECARD_APIKEY = secrets.get('CSC_API_KEY')

COLLEGE_SCORECARD_BASE = (
  'https://api.data.gov/ed/collegescorecard/v1/schools?'
  'school.name=%s&_fields=school.name%2Cschool.alias%2Clocation.lat%2Clocation.lon'
  '%2Cschool.city\%2Cschool.state\%2C2015.student.size&_sort=2015.student.size\%3Adesc&_per_page=10'
  '&api_key=%s')


def get_collegescorecard_data(school):
  
  s = COLLEGE_SCORECARD_BASE % (school, COLLEGE_SCORECARD_APIKEY)
  print(s)
  r = requests.get(s)
  data = json.loads(r.text)
  
  return data
  

def main():
  
  d2 = na_colleges.get()
  
  
  data= 'San%20Diego'
  data = get_collegescorecard_data(data)
  print(data)
  

if __name__ == '__main__':
  main()