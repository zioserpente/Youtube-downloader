import yt_dlp

def scarica_video(url, path_destinazione=r"C:\Users\moone\Downloads"):
    try:
       
        ydl_opts = {
            'outtmpl': f'{path_destinazione}/%(title)s.%(ext)s',
            'writethumbnail': True,     
            'postprocessors': [
                {  
                    'key': 'EmbedThumbnail',
                },
                {  
                    'key': 'FFmpegMetadata',
                }
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'Video senza titolo')
            formats = info_dict.get('formats', [])
            #print(formats)



            filtered_formats = [fmt for fmt in formats if fmt.get('acodec') != 'none' and (fmt['ext'] == 'm4a' or fmt['ext'] == 'mp4')]
            

           
            print(f"Formati disponibili per il video '{video_title}':")
            for fmt in filtered_formats:
                print(f"ID: {fmt['format_id']}, Estensione: {fmt['ext']}, Risoluzione: {fmt.get('resolution', 'n/a')}, Note: {fmt.get('format_note', '')}")
            
          
            format_id = input("Inserisci l'ID del formato che desideri scaricare: ")

            
            ydl_opts['format'] = format_id

            print(f"Download iniziato: {video_title}")
            ydl = yt_dlp.YoutubeDL(ydl_opts)
            ydl.download([url])  
            print(f"Download completato: {video_title}")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

if __name__ == "__main__":
    url_video = input("Inserisci l'URL del video di YouTube: ")
    percorso_destinazione = input("Inserisci il percorso di destinazione (premi invio per default: Downloads): ") or r"C:\Users\moone\Downloads"

    scarica_video(url_video, percorso_destinazione)
