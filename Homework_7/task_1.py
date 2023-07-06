# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени
# добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла. Переименование должно работать только
# для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extension>
import module_task_1 as mt1

updated_name = 'updated'
extension = 'png'
new_extension = 'jpeg'
mt1.rename_files(updated_name, extension, new_extension)
