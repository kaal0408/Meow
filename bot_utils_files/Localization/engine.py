

import logging
import yaml     
import pathlib
from Main import Meow

language_string = {}

class Engine:
    def __init__(self):
        self.path = "./bot_utils_files/Localization/strings/"
        
    def get_all_files_in_path(self, path):
        path = pathlib.Path(path)
        return [i.absolute() for i in path.glob("**/*")]

    def load_language(self):
        all_files = self.get_all_files_in_path(self.path)
        for filepath in all_files:
            with open(filepath, encoding='utf-8') as f:
                data = yaml.safe_load(f)
                language_to_load = data.get("language")
                logging.debug(f"Loading : {language_to_load}")
                language_string[language_to_load] = data
        logging.debug("All language Loaded.")
        
    def get_string(self, string):
        lang_ = Friday.selected_lang
        return (
            language_string.get(lang_).get(string)
            or f"**404_STRING_NOT_FOUND :** `String {string} Not Found in {lang_} String 	File. - Please Report It To @Murat_30`"
        )
