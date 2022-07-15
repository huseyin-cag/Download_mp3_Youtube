from pytube import YouTube
import os


while True:
    link = input("Link:") #Müziğin linki
    directory = input("Dİrectory:") #Müziğin koyualacağı klasörün adı

    if link == "exit":
        break
    

    try:
        video = YouTube(link)
    except:
        print("Hatalı link")
        exit()


    mp3 = video.streams.filter(only_audio=True).first()

    print("İndiriliyor")

    output = mp3.download(directory)

    base, ext = os.path.splitext(output)
    to_mp3 = base + ".mp3"
    os.rename(output, to_mp3)

    print("İndirme Tamamlandı")

