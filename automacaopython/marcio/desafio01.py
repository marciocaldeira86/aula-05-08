#crie automaticamennte as seguintes pastas:
#fotos, video, pdf, planilha, texto, backup


import os

listas = ["fotos", "video", "pdf", "planilha","texto", "backup"
          ]
for lista in listas:

    os.mkdir(lista)
    

