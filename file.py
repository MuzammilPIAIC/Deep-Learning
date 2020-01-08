from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os

try:
    import argparse
    flags=argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags=None
    
SCOPES="https://www.googleapis.com/auth/drive"
store=file.Storage("storage.json")
creds=store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow=client.flow_from_clientsecrets("client_secrets.json",SCOPES)
    creds=tools.run_flow(flow, store, flags)\
        if flags else tools.run(flow, store)
    
DRIVE=build("drive","v3", http=creds.authorize(Http()))
arr = os.listdir("F:\\NED\\file_to_drive\\car_images")
pk = tuple(arr)
Files=(
    str(pk),
      
)

for file_title in Files:
    file_name=file_title
    folder_id = "1CY9SD8LMAXzKC9yMTEyy6SB9JGQ_Vz6V"
    metadata={"name": file_name,
             "mimeType": None,
             "parent": [folder_id]
             }
    res=DRIVE.files().create(body=metadata, media_body=file_name).execute()
    if res:
        print("Uploaded ")

def createfolder(name):
    file_metadata = {
        "name":name,
        "mimetype":"application/vnd.google-api.folder"
    }
    files=DRIVE.files().create(body=file_metadata, fields="id").execute()
    print("Folder ID ",files.get("id"))

#createfolder("emotion")