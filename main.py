from pytube import YouTube

video_url = input('Enter the video url: ')

def bytes_to_mb(bytes):
    mb = bytes / (1024.0 ** 2)
    return int(mb)

yt = YouTube(url= video_url)

streams = yt.streams.filter(progressive=True)
download_options = [{'quality' : stream.resolution, 'size' : str(bytes_to_mb(stream.filesize)) + 'mb'} for stream in streams]

i = 1  
for option in download_options:
    print(f'{i} : quality-> {option["quality"]}     size-> {option["size"]}')
    i+=1

user_choice = input('Choose the quality you want: ')
user_option = streams[int(user_choice)-1].itag
stream = streams.get_by_itag(user_option)

path = input('Enter the folder path where you want to download the video: ').replace('\\','/')
print('Loading....')
stream.download(output_path=path)

print('download completed!')