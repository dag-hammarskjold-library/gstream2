from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from gdoc_api import Gdoc
from enum import Enum
from urllib.parse import unquote
import boto3
import datetime
import json
import os
import requests
from dlx import DB as DLX
from dlx.file import File as DLXFile, Identifier
from xml.dom import minidom

# Change this to reflect updates to your environment
class Config(object):
    client = boto3.client('ssm')
    env = os.getenv('GDOC_ENV', "qa")
    api_secrets = json.loads(client.get_parameter(Name=f'gdoc-{env}-api-secrets')['Parameter']['Value'])
    connect_string_param = api_secrets['connect_string_param']
    #connect_string = client.get_parameter(Name=connect_string_param)['Parameter']['Value']
    # Normally we should be able to get this from the above value, but
    # this is in a hybrid configuration at the moment.
    connect_string = client.get_parameter(Name='prodISSU-admin-connect-string')['Parameter']['Value']
    dbname = api_secrets['database_name']
    dlx_endpoint = 'https://metadata.un.org/editor/'
    # Bibs search only
    dlx_api_endpoint = 'https://metadata.un.org/editor/api/marc/bibs/records'
    duty_stations = [
        ('New York', 'NY'),
        ('Geneva', 'GE'),
        ('Vienna', 'Vienna'),
        ('Nairobi', 'Nairobi'),
        ('Beirut', 'Beirut')
    ]

class MetadataObject(object):
    def __init__(self, metadata):
        # metadata that's common to all of the files in the object
        self.agendaNo = metadata['agendaNo']
        self.jobId = metadata['jobId']  # English jobid only
        self.symbol1 = metadata['symbol1']
        self.symbol2 = metadata['symbol2']
        self.area = metadata['area']
        self.sessionNo = metadata['sessionNo']
        self.distributionType = metadata['distributionType']
        self.title = metadata['title']
        self.files = []
        self.links = []

    def __str__(self):
        return str({
            'agendaNo': self.agendaNo,
            'jobId': self.jobId,
            'symbol1': self.symbol1,
            'symbol2': self.symbol2,
            'area': self.area,
            'sessionNo': self.sessionNo,
            'distributionType': self.distributionType,
            'title': self.title,
            'files': self.files
        })

class FileObject(object):
    def __init__(self, metadata):
        self.embargo = metadata['embargo']
        self.languageId = metadata['languageId']
        self.odsNo = metadata['jobId']
        self.registrationDate = metadata['registrationDate']
        self.officialSubmissionDate = metadata['officialSubmissionDate']

DutyStations = [
    "New York", "NY", "Geneva", "Vienna", "Beirut", "Nairobi"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://0.0.0.0:3000"],  
 
  # Replace with your Nuxt app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Date setup
today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))

# Secrets
secrets = Config.api_secrets

db_client = DLX.connect(Config.connect_string, database=Config.dbname)
print(f"Connected to: {Config.connect_string.split('@')[1].split('/')[0]}")

@app.get("/")
def get_symbol_list(date: str = yesterday, dutyStation: str = 'NY'):
    print(unquote(dutyStation))
    if (dutyStation not in DutyStations):
        return {"msg": f"Invalid duty station. Valid values are {', '.join(DutyStations)}"}
    if (unquote(dutyStation) == "New York"):
        dutyStation = "NY"
    if (dutyStation == "Geneva"):
        dutyStation = "GE"


    g = Gdoc(client_id=secrets["client_id"], client_secret=secrets["client_secret"], token_url=secrets['token_url'], api_url=secrets['api_url'], ocp_apim_subscription_key=secrets['ocp_apim_subscription_key'], scope=secrets['scope'])
    g.set_param('dutyStation', dutyStation)
    g.set_param('dateFrom', str(date))
    g.set_param('dateTo', str(date))
    g.set_param('DownloadFiles', 'N')

    symbol_objects = {}
    for d in g.data:
        m = MetadataObject(d)
        f = FileObject(d)
        if m.symbol1 not in symbol_objects:
            m.files.append(f)
            symbol_objects[m.symbol1] = m
        else:
            symbol_objects[m.symbol1].files.append(f)

    #return symbol_objects

    return_data = []
    for s in symbol_objects:
        return_data.append(symbol_objects[s])

    return return_data

@app.get("/symbol")
def get_symbol_data(symbol: str):
    return_data = []
    this_symbol = Identifier('symbol',symbol)
    dlx_url = None
    for f in DLXFile.find_by_identifier_language(this_symbol, 'en'):
        dlx_url = f'{Config.dlx_endpoint}api/files/{f.id}?action=open'
    if dlx_url is not None:
        return_data.append({'name': 'dlx', 'url': dlx_url})
        
    print(return_data)
    return return_data