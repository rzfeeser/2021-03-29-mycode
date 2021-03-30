#!/usr/bin/python3

import requests

API = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY"

# max number of pictures to DL
NUMTODL = 10

def main():
        counter = 0
        r = requests.get(API)

        # we want to grab the data off the 200 response
        nasadata = r.json()

        # loop across all the dictionaries within the list called "photos"
        for pic in nasadata.get("photos"):
           
            # increase the counter by 1
            counter += 1
            # we want to snag the value mapped to photos."pic".img_src
            # print(pic.get("img_src"))
            linktodownload = pic.get("img_src")

            # download the image
            imgdl = requests.get(linktodownload)
            # grab name of image
            imgNm = linktodownload.split("/")[-1]

            # show which image is about to be downloaded
            print(f"Downloading Image #{counter}: {imgNm}")

            # open the file we want to write our image to
            with open(f"/home/student/static/{imgNm}", 'wb') as f:
                # write the image
                f.write(imgdl.content)
        
            # if counter reaches the max number of photos to download
            # exit the loop (break)
            if counter == NUMTODL:
                break

if __name__ == "__main__":
    main()
