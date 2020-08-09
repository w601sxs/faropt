print(" Starting FarOpt backend")
print("---------------------------------------------------------------")
print('Downloading source')
import os
print('Looking for source.zip in ',os.environ['s3bucket'],'/',os.environ['s3key'])

import boto3

s3 = boto3.client('s3')
s3.download_file(os.environ['s3bucket'], os.environ['s3key']+'/source.zip', 'source.zip')

print('Downloaded zip, uncompressing')


import zipfile
with zipfile.ZipFile('source.zip', 'r') as zip_ref:
    zip_ref.extractall('/tmp/')

print(os.listdir("/tmp/"))

print("---------------------------------------------------------------")
# print('Checking script with modulefinder...')
# from modulefinder import ModuleFinder

# finder = ModuleFinder()
# finder.run_script('/tmp/main.py') #This will also determine if there is no main function

# print('Loaded modules:')
# for name, mod in finder.modules.items():
#     print('%s: ' % name, end='')
#     print(','.join(list(mod.globalnames.keys())[:3]))

# print('-'*50)
# print('Modules not imported:')
# print('\n'.join(finder.badmodules.keys()))


import main