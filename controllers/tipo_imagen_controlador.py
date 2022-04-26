def tipo_archivo(tipo_archivo,ruta_archivo):
    vista = './static/images/tipo_archivos/file_desconocido.jpg'
    
    if tipo_archivo in ['jpg','png','gif','tiff','psd','bmp','eps','svg']:
        vista = './static/images/' + ruta_archivo
    if tipo_archivo in ['html','htm']:
        vista = './static/tipo_archivos/file_html.png'
    if tipo_archivo == 'exe':
        vista = './static/tipo_archivos/file_exe.png'
    if tipo_archivo == 'accdb':
        vista = './static/tipo_archivos/file_access.png'
    if tipo_archivo == 'apk':
        vista = './static/tipo_archivos/file_apk.png'
    if tipo_archivo == 'xlsx':
        vista = './static/tipo_archivos/file_excel.png'
    if tipo_archivo == 'exe':
        vista = './static/tipo_archivos/file_exe.png'
    if tipo_archivo == 'gif':
        vista = './static/tipo_archivos/file_gif.png'
    if tipo_archivo == 'html':
        vista = './static/tipo_archivos/file_html.png'
    if tipo_archivo == 'mp3':
        vista = './static/tipo_archivos/file_mp3.png'
    if tipo_archivo == 'mp4':
        vista = './static/tipo_archivos/file_mp4.png'
    if tipo_archivo == 'pdf':
        vista = './static/tipo_archivos/file_pdf.png'
    if tipo_archivo == 'pptx':
        vista = './static/tipo_archivos/file_powerpoint.png'
    if tipo_archivo == 'wav':
        vista = './static/tipo_archivos/file_wav.png'
    if tipo_archivo == 'docx':
        vista = './static/tipo_archivos/file_word.png'
    return vista