# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2023 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['Users']

from .get_user_dict import GetUserDict


class Users(GetUserDict):
    """ methods.users """
