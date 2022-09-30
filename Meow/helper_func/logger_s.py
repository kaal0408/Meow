

import os
import logging
import traceback
from Main import Config
from Main.helper_func.basic_helpers import edit_or_send_as_file


class LogIt:
    def __init__(self, message):
        self.chat_id = Config.LOG_GRP
        self.message = message

    async def log_msg(self, client, text: str = "?"):
        if len(text) > 1024:
            try:
                Hitler = await client.send_document(self.chat_id, make_file(text))
            except BaseException as e:
                logging.error(str(e))
                return None
            os.remove("logger.log")
            return Hitler
        else:
            try:
                return await client.send_message(self.chat_id, text)
            except Exception as e:
                traceback.print_exc()
                logging.error(str(e))
                return None

    async def fwd_msg_to_log_chat(self):
        try:
            return await self.message.forward(self.chat_id)
        except BaseException as e:
            traceback.print_exc()
            logging.error(str(e))
            return None


def make_file(text):
    open("logger.log", "w", encoding='utf-8').write(text)
    return "logger.log"
