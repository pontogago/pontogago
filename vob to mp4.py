from moviepy.editor import VideoFileClip

def convert_vob_to_mp4(input_file, output_file):
    try:
        # Carrega o vídeo VOB
        video = VideoFileClip(input_file)
        
        # Salva o vídeo como MP4
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        
        print("Conversão concluída com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante a conversão: {str(e)}")

if __name__ == "__main__":
    # Caminho do arquivo de entrada VOB
    input_file = r"C:\Users\adcp church\Desktop\festa.vob"
    
    # Caminho do arquivo de saída MP4
    output_file = r"C:\Users\adcp church\Desktop\festacon.mp4"
    
    # Chama a função para converter
    convert_vob_to_mp4(input_file, output_file)
