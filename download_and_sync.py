from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re
from progress.bar import Bar
import shutil

def save_youtube_music_in_cache_file(youtube_title_music: str, download_folder:str):
    cache_file_name = os.path.join(download_folder, "cache.txt")
    print(" Create cache file! ",youtube_title_music, " in ", cache_file_name)
    with open(cache_file_name, 'a', encoding="utf-8") as arquivo:
        arquivo.write(youtube_title_music+'\n')

def verify_youtube_music_in_cache_file(youtube_title_music: str, download_folder:str):
    try:
        cache_file_name = os.path.join(download_folder, "cache.txt")
        print(" read cache file! ",youtube_title_music, " in ", cache_file_name)
        with open(cache_file_name, 'r', encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if youtube_title_music in conteudo:
                return True
            else:
                return False

    except FileNotFoundError:
        return False

def test_cache_manager(download_folder:str):
    if(verify_youtube_music_in_cache_file('teste', download_folder)):
        save_youtube_music_in_cache_file('teste', download_folder);

    print(verify_youtube_music_in_cache_file('teste', download_folder))
    print(verify_youtube_music_in_cache_file('teste', download_folder))

def download_if_needs_playlist(playlist_id: str, create_playlist_cache: bool, download_folder:str):
    playlist = Playlist(f'https://www.youtube.com/playlist?list={playlist_id}')
    total_playlist =  len(playlist.video_urls)

    bar = Bar('Download-Musics', max=total_playlist)

    #Download if needs
    for url in playlist:

        try:
            #If flag create_playlist_cache is true, the videos allready download, not try download again
            if create_playlist_cache:
                if verify_youtube_music_in_cache_file(url, download_folder):
                    continue
                else:
                    save_youtube_music_in_cache_file(url, download_folder)
        except Exception as erro:
            print("Erro durante a realizacao do cache, continuando o donwload como esperado:", erro)

        # Continue
        youtube_info: YouTube = YouTube(url)

        youtube_stream = youtube_info.streams.filter(only_audio=True).first()

        if youtube_stream is not None:
            youtube_stream.download(output_path = download_folder, skip_existing=True)

        bar.next()

    bar.finish()

def convert_if_needs_mp4_to_mp3(download_folder: str, folder:str):
    # Convert if needs
    count_convert = 0
    files = os.listdir(download_folder)
    bar_convert = Bar('Convert-Musics', max=len(files))

    for file in files:

        if file == 'raw':
            continue

        if re.search('mp4', file):
            # print("verificando musica: ", file)
            mp3_path = os.path.join(folder, os.path.splitext(file)[0]+'.mp3')

            if not os.path.exists(mp3_path):
                mp4_path = os.path.join(download_folder,file)
                # print("new music fould: ", mp4_path)

                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                new_file.close()

            # else:
                # print("music allready exists")

            count_convert = count_convert+1
            bar_convert.next()
            # print('Total convertidos: ', count_convert, ' DE:',  len(files))

    bar_convert.finish()



def move_if_mp3_is_conected(mp3_folder_path: str, folder:str):
    total_new_musics: int = 0
    # if mp3 is conected move musics
    if os.path.exists(mp3_folder_path):
        print("mp3 is conected, move musics!")

        files_mp3_to_sync = os.listdir(folder)
        count_move = 0

        bar_move = Bar('Move-Musics', max=len(files_mp3_to_sync))

        for file in files_mp3_to_sync:

            if re.search('mp3', file):
                mp3_path_target = os.path.join(mp3_folder_path, file)

                if not os.path.exists(mp3_path_target):
                    mp3_path_source = os.path.join(folder, file)
                    shutil.copy2(mp3_path_source, mp3_path_target)
                    total_new_musics = total_new_musics +1
                    

                count_move = count_move + 1
            bar_move.next()

        bar_move.finish()

    return total_new_musics