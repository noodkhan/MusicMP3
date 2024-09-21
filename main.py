# Developed by Noodkhan Navin 
import os
import webbrowser 
from pytube import YouTube


array = [
         "htps://www.youtube.com/watch?v=mM6GhN4jdn0&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=1&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=3Nf5HriW9XA&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=2&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=1xW8ykYdHV4&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=3&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=bYGfv-q8ECE&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=4&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=5xYlc4OBnPg&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=5&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=1aokooixKIo&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=6&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=u5CVsCnxyXg&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=7&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=BbWBRnDK_AE&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=8&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=cWGE9Gi0bB0&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=9&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=3basVsq1VnY&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=10&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=Rxy-1VK22Ms&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=11&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=Ovo1y7Pllt8&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=12&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=lpwnzItInBo&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=13&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=dWUCwWWI7CU&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=14&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=_cZUUL6QJdM&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=15&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=_L0925nP0RI&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=16&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=Ab1nJg4RKw0&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=17&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=ENJh3qecaN4&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=18&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=nGt_JGHYEO4&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=19&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=5XK4v2fgMPU&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=20&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=hkSYfVC2Wcs&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=21&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=d41Rsaauj3A&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=22&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=6B84ng6UAKI&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=23&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=K4yT6u4TTjI&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=24&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=BUD0m11eKMU&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=25&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=FlZzhi2usVI&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=26&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=3sVMUUFjzgQ&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=27&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=qmddCVn-O80&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=28&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=-gg5ns2fd4U&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=29&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=8qgUKzLDYrM&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=30&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=EM-i_s03Uc4&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=31&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=rc7KnQAh_1I&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=32&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=RaLwQ_32NDU&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=33&pp=gAQBiAQB8AUB",
         "htps://www.youtube.com/watch?v=trbwqF0d7NA&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=34&pp=gAQBiAQB8AUB"
]


def openBrowser():
    url = 'https://www.youtube.com/watch?v=_L0925nP0RI&list=PLB0Hai3X9228X3JQN_NxAHBMiySPNe5CL&index=16' 
    webbrowser.open(url)


def downloadMP3():
    yt = YouTube(
        str(input('Enter Your URL : \n >> '))
    ) 
    video = yt.streams.filter(only_audio=True).first()
    destination = str(input('Enter File Directory or Leave it Blank >> ')) or '.'
    out_file = video.download(output_path=destination)
    base , ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file , new_file)
    print(yt.title + " has been downloaded from Youtube")


def downloadArrayMP3(array):
    for i in range(0 , len(array)):
        print(i , array[i])
        yt = YouTube(array[i]) 
        video = yt.streams.filter(only_audio=True).first()
        destination = './music'
        out_file = video.download(output_path=destination)
        base , ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file , new_file)
        print(yt.title + " has been downloaded from Youtube")


# downloadMP3()
downloadArrayMP3(array)
