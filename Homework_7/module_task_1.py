from pathlib import Path


def rename_files(new_name, ext, new_ext):
    files_to_rename = [f for f in Path(Path().cwd()).iterdir() if f.suffix == f'.{ext}']
    for i, file in enumerate(files_to_rename, start=1):
        file.rename(f'{file.stem}_{new_name}_{i}.{new_ext}')
