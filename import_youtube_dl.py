import youtube_dl

def download_video():
    try:
        # Get user input for video URL
        video_url = input("Enter the video URL: ")

        # Options for youtube_dl
        ydl_opts = {
            'outtmpl': '.C:\Users\brosc\Desktop\project\files/%(title)s.%(ext)s',  # Save in a 'downloads' folder
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)

        print("Download completed successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_video()
