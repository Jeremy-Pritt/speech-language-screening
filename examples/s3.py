### https://s3fs.readthedocs.io/en/latest/


import s3fs
import json
import pandas as pd

### creds is the key ID and the secret key from AWS Console
### json
creds = json.load(open('creds.json', 'r'))
### pandas
creds = pd.read_csv('creds.csv')

fs = s3fs.FileSystem(user=creds['id'], password=creds['secret'])

### with s3fs
with fs.open('/bucket-name/subfolder/file.txt', 'w') as f:
    f.write('some text')
    
### with native Python
# with open('file.txt', 'w') as f:
    # f.write('some text')