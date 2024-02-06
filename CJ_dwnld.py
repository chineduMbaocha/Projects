import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

#function to trigger the command
def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()

    progress_bar.pack(pady=10, padx=5)
    prograss_label.pack(pady=10, padx=5)
    status_label.pack(pady=10, padx=5)

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()

    #download the video into a specific directory
        os.path.join("C:/Users/brosc/Desktop/project/files", f"{yt.title}.mp4")
        stream.download(output_path="C:/Users/brosc/Desktop/project/files")
   
        status_label.configure(text="video downloaded", text_color="white", fg_color="green")

    except Exception as e:

        status_label.configure(text=f"Error{str(e)}", text_color="white")

#customize the progress bar to show the percentage
def on_progress(stream, chunk, bytes_remaining):
   total_size = stream.filesize
   bytes_dowmload = total_size - bytes_remaining
   percentage_completed = bytes_dowmload / total_size *100
  
   prograss_label.configure(text= str(int(percentage_completed)) + "%")
   prograss_label.update()

   progress_bar.set(float(percentage_completed/100))


#create root window
root = ctk.CTk()
ctk.set_appearance_mode ('dark')
ctk.set_default_color_theme('green')

#title of the window
root.title('CJ youtube downloader')

#set min and max width and height
root.geometry('720x480') 
root.minsize(720, 480)
root.maxsize(1080, 720)

#create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand = True, padx=10, pady=10)

#create a label and the entry widget for the video url
url_label=ctk.CTkLabel(content_frame, text='Enter the url here : ')
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
#add placeholder to the label field
entry_url= ctk.CTkEntry(content_frame, placeholder_text='Enter Url') 

url_label.pack(pady=10, padx=5)
entry_url.pack(pady=10, padx=5)


#create download buttoon
download_button = ctk.CTkButton(content_frame, text='Download', command=download_video)
download_button.pack(pady=10, padx=5, )


#create a solution combo box
resolution = ["720p", "360p", "240p"] #this create a list in the combobox
resolution_var = ctk.StringVar()
resolution_combobox=ttk.Combobox(content_frame, values=resolution, textvariable=resolution_var)
resolution_combobox.pack(pady=10, padx=5)
resolution_combobox.set("720p") #This set a default placeholder for the lists in the combobox

#create a label and the progree bar to display the download progress
prograss_label= ctk.CTkLabel(content_frame, text="0%")
prograss_label.pack(pady=10, padx=5)

progress_bar = ctk.CTkProgressBar(content_frame, width=500)
progress_bar.set(0) #to set the % on the bar
#progress_bar.pack(pady=10, padx=5)

#create status label
status_label= ctk.CTkLabel(content_frame, text="downloading")

#To start the app
root.mainloop()