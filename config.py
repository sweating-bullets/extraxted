#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "20870930"))
    API_HASH = os.environ.get("API_HASH", "d8339c188abe7b852e52ef2d0d48c770")
    AUTH_USERS = "1760032652"

