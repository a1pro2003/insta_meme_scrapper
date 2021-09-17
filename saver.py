import instaloader
import datetime
import os
from time import sleep
from instaloader.structures import load_structure_from_file
from instapy_cli import client
import pandas as pd
import uploader
import csv
import schedule
import time


downloads = "downloads/"

L = instaloader.Instaloader()

#login to account
L.load_session_from_file("broisjokes")


def download_post():
    #get shrotcode from link
    #url1 = input("Url: ")#asks for input link

    with open('to_download.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        url1 = header[0]
        comment = header[1]

    with open('to_download.csv', 'w') as f:
        file = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([])


    shortcode = str()
    count = 0
    for char in url1:
        if char == '/' and count == 4:
            break
        elif  count == 4:
            shortcode += char
            if char == '/':
                count += 1
        elif char == '/':
            count += 1
            pass

    #download and move post
    now = datetime.datetime.now()
    timespam = now.strftime("%Y-%m-%d_%H-%M-%S")
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    L.download_post(post, timespam)
    username = post.owner_username
    return(shortcode, post, timespam, username, comment)

def clean_dir(timespam, username, comment):
    #if there isan .mp4 file delete anything else
    filenames = []

    for fname in os.listdir(timespam):
        if fname.endswith('.jpg'):# or fname.endswith('.mp4'):
            filenames += fname
            print(fname)
            pass
        elif fname.endswith('.mp4'):
            filenames += fname
            os.remove("{}".format(timespam + "/" + fname[:-4] + ".jpg"))
            print(fname)
        else:
            pass
            os.remove("{}".format(timespam + "/" + fname))


    #copies presaved caption and included account name
    caption = str()
    with open("tags.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            caption += line

    with open(timespam + "/" + "caption.txt", "w") as f:
        f.write(caption.format(username, "#", comment))
    # print("f nameee is: {0}".format(filename))
    os.system("mkdir downloads")
    os.system("move {0} {1}".format(timespam , downloads))
    return filenames


def main():
    while True:
        sleep(3)
        schedule.run_pending()

        try:
            schedule.every().day.at("10:00").do(uploader.insta_post,os.path.abspath(downloads + os.listdir("downloads/")[-1]))
            schedule.every().day.at("14:30").do(uploader.insta_post,os.path.abspath(downloads + os.listdir("downloads/")[-1]))
            schedule.every().day.at("19:00").do(uploader.insta_post,os.path.abspath(downloads + os.listdir("downloads/")[-1]))
            schedule.every().day.at("22:00").do(uploader.insta_post,os.path.abspath(downloads + os.listdir("downloads/")[-1]))
            schedule.every().day.at("20:15").do(uploader.insta_post,os.path.abspath(downloads + os.listdir("downloads/")[-1]))
        except:
            pass

        try:
            if pd.read_csv('to_download.csv').empty == True: # will return True if the dataframe is empty or False if not.
                check = False
                with open('to_download.csv', 'r') as f:
                    reader = csv.reader(f)
                    header = next(reader)
                    try:
                        checkbox = header[2]
                        check = True
                    except:
                        check = False
                print("Not empty")
                if check == True:
                    try:
                        shortcode, post, timespam, username, comment = download_post()

                        clean_dir(timespam, username, comment)

                        sleep(4)

                        #uploader.insta_post(os.path.abspath(downloads + os.listdir("downloads/")[0]))
                    
                    except:
                        print("error getting post")
                        pass
                if check == False:
                    try:
                        shortcode, post, timespam, username, comment = download_post()

                        clean_dir(timespam, username, comment)

                        sleep(4)

                        uploader.insta_post(os.path.abspath(downloads + os.listdir("downloads/")[-1]))
                    
                    except:
                        print("error getting post")
                        pass
            else:
                pass
        except:
            
            print("Empty")
            pass

if __name__ == "__main__":
    main()

