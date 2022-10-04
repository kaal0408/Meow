from pyrogram.types import Message

# a Logging class
class Logme:
    def init(self, message):
        self.chat_id = PVT_GRP
        self.message = message
    async def fwd_msg_to_log_chat(self):
        try:
            return await self.message.forward(self.chat_id)
        except BaseException as e: 
            logging.error(str(e))
            return None
