from pathlib import Path
import os

def organizeExtension(_directory, _extension):
    os.chdir(_directory)
    
    if not _extension.startswith("."):
        _extension = "." + _extension
        
    exists = any(file.is_file() and file.suffix.lower() == _extension.lower() for file in _directory.iterdir())
    if not exists:
        print(f"------------------------------\nNo '{_extension}' files found in '{_directory}'")
        return
        
    new_folder = _directory / f"{_extension[1:]}_Organization"
    new_folder.mkdir(exist_ok=True)
    
    for file in _directory.iterdir():
        if file.is_file() and file.suffix.lower() == _extension.lower():
            #new_folder = os.mkdir(f"{_directory}\\{_extension} Organization{_extension}")
            file.rename(new_folder / file.name)
            print(f"{file.name} -> {new_folder.name}")
            
            