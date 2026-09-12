import os
import shutil

Downloads = r"C:\Users\batco\Downloads"
AreaDTrabalho = r"C:\Users\batco\Desktop"

#Este mapa extensão deixei apenas PDF para fins de teste no meu computador, mas pode ser adicionado outras extensões de arquivos e suas respectivas pastas, como por exemplo: 
# "Imagens": [".jpg", ".png", ".jpeg"], "Documentos": [".docx", ".txt"], etc.
mapa_extensoes = {
    "PDF": [".pdf"],
}

itens = os.listdir(Downloads)

for item in itens:  
    caminho_item = os.path.join(Downloads, item)
    
    if os.path.isfile(caminho_item):
        extensao = os.path.splitext(item)[1].lower()
        
        for pasta, extensoes in mapa_extensoes.items():
            if extensao in extensoes:
                caminho_destino = os.path.join(AreaDTrabalho, pasta)
                
                if not os.path.exists(caminho_destino):
                    os.makedirs(caminho_destino)
                
                shutil.move(caminho_item, caminho_destino)
                print(f"Arquivo '{item}' movido para a pasta '{pasta}'.")
                break