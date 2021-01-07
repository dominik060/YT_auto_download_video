from pytube import YouTube
import os
import subprocess

def get_download_path():
    #windows
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    #linux
    else:
        print(os.getenv('LANGUAGE'))
        l = subprocess.check_output()
        #languages
        if l == "cs":
            return os.path.join(os.path.expanduser('~'), 'Stažené')

        if l == "en":
            return os.path.join(os.path.expanduser('~'), 'download')

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

yt = input("YouTube video url: ")

try:
    downloadYouTube(f'{yt}', f'{get_download_path()}')
    print("Your video was downloaded")
    input("")
except:
    print("This url is incorrect")
    input("")

