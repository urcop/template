from aiogram.dispatcher.filters import BoundFilter

from bot.config import Config


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin=None):
        self.is_admin = is_admin

    async def check(self, obj):
        if self.is_admin is None:
            return
        if not self.is_admin:
            return False
        config: Config = obj.bot.get('config')
        user_id = obj.from_user.id
        return user_id in config.bot.admins
