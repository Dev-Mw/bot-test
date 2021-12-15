#!/usr/bin/env python
# -*- Coding: utf-8 -*-
"""
Query params model info...

Author: Dario sotelo
Date: 15/12/2021
"""
from pydantic import BaseModel


class QueryParamsModel(BaseModel):
    """Class Model for query params"""
    url: str = None
