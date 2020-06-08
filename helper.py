import os


class Helper:

    def get_bot_token(self, root):
        """Return telegram bot token"""

        file_path = os.path.join(root, 'teletoken.txt')
        with open (file_path, 'r') as file:
            token = file.read()

        return token

    def send_message(self, bot, chat_id, message, **kwargs):
        """Function to sending message tp user channel
        :param bot - telegramm bot instance
        :param chat_id - id of user channel
        :param message - message to user from bot
        """

        bot.send_message(chat_id, message, **kwargs)