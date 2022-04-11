import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:                   
                localPath = os.path.join(root, filename)
                relativePath = os.path.relpath(localPath, file_from)
                dropboxPath = os.path.join(file_to, relativePath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BFhngcR5doz5nJljYwLRJsOnSN6cBKn1qoOkNOLLdMAwiuCFQjND-vKjEvMslyUWBSPh3KDJ3xT23dMYCzVtkcxpbPAN5hZymYdQUPyPMV0c7ZtLdVxIhubUv2cPzppFSwgrHKiT'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : "))
    file_to = input("enter the full path: ")  
    transferData.upload_file(file_from,file_to)
    print("Folder has been uploaded.")

main()