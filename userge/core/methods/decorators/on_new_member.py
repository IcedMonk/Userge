# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2023 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['OnNewMember']

from pyrogram import filters
from pyrogram.filters import Filter as RawFilter

from . import RawDecorator


class OnNewMember(RawDecorator):  # pylint: disable=missing-class-docstring
    def on_new_member(self,
                      welcome_chats: RawFilter,
                      group: int = -2,
                      allow_via_bot: bool = True,
                      check_client: bool = True,
                      check_downpath: bool = False) -> RawDecorator._PYRORETTYPE:
        """\nDecorator for handling new members

        Parameters:
            welcome_chats (:obj:`~pyrogram.filters.chat`):
                Pass filters.chat to allow only a subset of
                messages to be passed in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.

            allow_via_bot (``bool``, *optional*):
                If ``True``, allow this via your bot, defaults to True.

            check_client (``bool``, *optional*):
                If ``True``, check client is bot or not before execute, defaults to True.

            check_downpath (``bool``, *optional*):
                If ``True``, check downpath and make if not exist, defaults to False.
        """
        return self.on_filters(
            filters=filters.group & filters.new_chat_members & welcome_chats,
            group=group, allow_via_bot=allow_via_bot, check_client=check_client,
            check_downpath=check_downpath)
