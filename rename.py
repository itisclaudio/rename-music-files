# Python 3 code to rename multiple
# files in a directory or folder
 
# importing os module
import os
 
# Function to rename multiple files
def main():
   
    folder = "C:/Temp/rename"
    folder_dst = "C:/Temp/renamedone"
    for count, filename in enumerate(os.listdir(folder)):
        print("======filename: {}".format(filename))
        song_dash_artist, ext = os.path.splitext(filename)
        song_artist_list = song_dash_artist.split('-')
        if len(song_artist_list) == 2:
            new_name = song_artist_list[1].strip()+" - "+song_artist_list[0].strip()+ext
            src =f"{folder}/{filename}"
            print("src: {}".format(src))
            dst = f"{folder_dst}/{new_name}"
            print("dst: {}".format(dst))
            os.rename(src, dst)
        #songname = f""
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst1 =f"{folder_dst}/{dst}"
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()
