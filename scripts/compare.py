
# Script to find differences between #NeverAgainColleges and NACAC list

from difflib import SequenceMatcher
import re

import nacac
import na_colleges
from pandas import DataFrame
from pandas import concat 



def str_compare(a,b):
    return SequenceMatcher(None, a,b).ratio() * 100



"""
General methodology:

1. Get both data sources in two dataframes
2. For each college in NACAC
    2a. Find "SequenceMatcher" score of NACAC college compared to everything in #NeverAgainColleges
    2b. If top match is 100%, don't worry about it
    2c. If not, ask user to choose from top 5
    2d. If no close matches, write to compare.csv

3. In end, compare.csv has all NACAC colleges that #NeverAgainColleges doesnt
"""
def main():
    
    d1 = nacac.get()
    d2 = na_colleges.get()
    df = DataFrame(columns=['nacac_name', 'link'])
    
    for index, row in d1.iterrows():
        
        col = row['Institution ']
        a = []
        for x in d2['name']:
            x_clean = re.sub(r' *university *| *colleges* *', '', x, flags=re.IGNORECASE)
            col_clean = re.sub(r' *university *| *colleges* *', '', col, flags=re.IGNORECASE)
            
            a.append({
                    'score':str_compare(col_clean, x_clean),
                    'other_col':x
                })
            
        a = sorted(a, key=lambda x: x.get('score'), reverse=True)
        
        if a[0].get('score') == 100 and str_compare(a[0].get('other_col'), col) == 100:
            
            print('Perfect match: "%s" & "%s"' % (col, a[0].get('other_col')))
            
            """
            ans = raw_input('Press "y" to continue, "n" to flag\t')
            
            if ans.lower() is not 'y':
                df = df.append({'nacac_name':col, 'link': row['Web Address ']}, ignore_index=True) # inefficient but doesnt matter
                print('Added, continuing...')
            else:
                print('Continuing...')
            """
        else:
            
            print('Which one looks correct?')
            
            for x in range(5):
                print('%d - "%s" | "%s"' %(x+1, col, a[x].get('other_col')))
            print('6 - none of these')
            
            try:
                ans = int(raw_input('Which college matches %s the best?\t' % (col))) - 1 
            except:
                ans = 100
                
            if ans < 5:
                print('Continuing...')
            else:
                df = df.append({'nacac_name':col, 'link': row['Web Address ']}, ignore_index=True) # inefficient but doesnt matter
                print('Added, continuing...')
        
        df.to_csv('compare.csv') #Extremely ineffiecient, but nice since less writing
            
    df.to_csv('compare.csv')
    
if __name__ == '__main__':
    main()