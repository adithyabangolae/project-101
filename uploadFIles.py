import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access= access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        
        for root, dirs, files in os.walk(file_from):

             for filename in files:

                 local_path = os.path.join(root, filename)


                 relative_path = os.path.realpath(local_path,file_from)
                 dropbox_path = os.path.join(file_to, relative_path)

                 with open(local_path,'rb') as f:
                     dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'aIr2b9NS6rUAAAAAAAAAAZagNl6vEPGqBhIOohR6-Dm0qm9Lj3b-JUF3KA9rvUr0'
    transferData = TransferData(access_token)

    file_from =str(input("Enter folder path:"))
    file_to = input("enter full path:")

    transferData.upload_file(file_from,file_to)
    print("file has been moved")


main()




