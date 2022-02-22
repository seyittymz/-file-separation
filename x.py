import os 
import shutil


dosya_yolu = os.path.dirname(os.path.realpath(__file__))
files = os.listdir(f"{dosya_yolu}")
def dosya_olustur(files):
    listem = []
    uzanti_listen =[]
    file_name=[]
    a=0

    for get in files:  
        listem.append(get.split(".")) #uzantıyı almak için "."'dan ayırıyoruz  .
        
        if "." in get:
            uzanti_listen.append(listem[a][1])
            file_name.append(get)

            for new_folder in list(set(uzanti_listen)):
                if not os.path.exists(fr"{dosya_yolu}\{new_folder}"):
                    os.mkdir(fr"{dosya_yolu}\{new_folder}")#uzantısı neyse o şekilde bir klasör açıldı
                    print(f"{new_folder} adında bir klasör açıldı.")

        a+=1
    
    
    for x in range (len(uzanti_listen)):
        if file_name[x]=="x.py":#çalışmakta olduğumuz dosyanın adını yazıyoruz .
            pass
        else:
            shutil.move(fr"{dosya_yolu}\{file_name[x]}",fr"{dosya_yolu}\{uzanti_listen[x]}")

dosya_olustur(files)



