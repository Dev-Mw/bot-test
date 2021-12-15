#!/usr/bin/env python
# -*- Coding: utf-8 -*-
"""
Main Application for testing...

Author: Dario sotelo
Date: 15/12/2021
"""
import re
from typing import Dict

from fastapi import FastAPI
from bot.models.query_params_model import QueryParamsModel
from bot.config import REGEX_WORD_COUNT


app = FastAPI()


def json_response(**kwargs) -> Dict:
    """
    Show anything...

    :param kwargs: anything
    :return: data dictionary
    """
    return kwargs


@app.post("/")
def root(query_params: QueryParamsModel) -> Dict:
    """
    Show anything...

    :param query_params: data model using base model
    :return: data dictionary
    """
    _, word_list = dict(), lambda r, u: re.split(r, u)
    for x in word_list(REGEX_WORD_COUNT, query_params.url):
        _ |= {x: 1} if x not in _ else {x: _[x] + 1}

    return json_response(url=query_params.url, words=_)
