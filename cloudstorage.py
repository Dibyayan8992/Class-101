import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.BOEv0YJifs9Xnd-7DOtNteSExjEG0Adki2l3oClqqGU53zePQO-OgvIH-sYCd-OYrFP6oV4YK1mQyxhvoVoyIHiMaJhIBYXsjsct-S4N2Urqn316apYv3lVNx-JbHMWIRr1wbT9q1gRS"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("File has been moved successfully")

main()