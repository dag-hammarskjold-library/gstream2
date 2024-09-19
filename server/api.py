from fastapi import FastAPI
from gdoc_api import Gdoc
from enum import Enum
import boto3
import datetime
import json

# Change this to reflect updates to your environment
class Config(object):
    client = boto3.client('ssm')
    api_secrets = client.get_parameter(Name='gdoc-api-secrets')['Parameter']['Value']
    connect_string = client.get_parameter(Name='prodISSU-admin-connect-string')['Parameter']['Value']
    dbname = "undlFiles"
    dlx_endpoint = 'https://metadata.un.org/editor/'
    duty_stations = [
        ('New York', 'NY'),
        ('Geneva', 'GE')
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
    "NY", "GE", "Vienna", "Beirut", "Nairobi"
]

app = FastAPI()

# Date setup
today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))

# Secrets
secrets = json.loads(Config.api_secrets)

@app.get("/")
def get_symbol_list(date: str = yesterday, duty_station = 'NY'):
    if (duty_station not in DutyStations):
        return {"msg": f"Invalid duty station. Valid values are {', '.join(DutyStations)}"}

    g = Gdoc(username=secrets["username"], password=secrets["password"])
    g.set_param('dutyStation', duty_station)
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