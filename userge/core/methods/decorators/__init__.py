# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2023 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['Decorators']

from .raw_decorator import RawDecorator  # noqa
from .on_cmd import OnCmd
from .on_filters import OnFilters
from .on_left_member import OnLeftMember
from .on_new_member import OnNewMember


class Decorators(OnCmd, OnFilters, OnLeftMember, OnNewMember):
    """ methods.decorators """
