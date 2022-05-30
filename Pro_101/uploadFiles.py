import dropbox
import os

class TransferData:
    def __init__(self, access_token):
       self.access_token = access_token

    def uploadFiles(self, file_to,file_from,):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for name in files:
              local_path=os.path.join(root, name)

              relative_path = os.path.relpath(local_path,file_from)
              dropbox_path = os.path.join(file_to,relative_path)
        
              with open(file_from,'rb') as f:
                  dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BIiX2RiolL92tJsUeP60pbdKWZpvXamj3wBJMHqCsATeyrDBkPY_JiYZJ4ov9cAtZFrBGCWCmXUXc3jCRRgl6u6IlKGDzZZwWLgyjTM1Ow3kqUx7CvCkBZUhfuQd_FB0qK3iZVe8UfNR'
    transferData = TransferData(access_token)

    file_from = str(input("Enter file path"))
    
    file_to = str(input("Enter file path for dropbox(enter file name)"))

    transferData.uploadFiles(file_from, file_to)
    print("File has been moved!")


main()



