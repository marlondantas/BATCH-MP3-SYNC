from download_and_sync import *

print("Iniciando sistema!")
#parametros de configuracao
#Para o funcionamento correto do scrip é importante informar corretamente os parametros, incluindo o caminho dos diretorios.

#A Playlist precisa ser pública no youtube.
class configs():
    playlist_id: str = "PLi3hSKWGMakPLGjy2dCPL-h0Nr0urP47y"

    folder: str = "C:\\Users\\marlo\\Music\\Sync-mp3-Mar"
    download_folder: str = folder+"\\raw"
    mp3_folder_path = 'D:\\is_mar_mp3\\'

    create_playlist_cache: bool = True


if configs.create_playlist_cache:
    test_cache_manager(configs.download_folder)


download_if_needs_playlist(configs.playlist_id, configs.create_playlist_cache, configs.download_folder);
convert_if_needs_mp4_to_mp3(configs.download_folder, configs.folder);
move_if_mp3_is_conected(configs.mp3_folder_path, configs.folder);