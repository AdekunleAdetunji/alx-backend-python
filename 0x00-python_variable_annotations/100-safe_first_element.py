#!/usr/bin/python3
"""
This module contains a duck typed function safe_first_element
"""
from typing import Any
from typing import Sequence
from typing import Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
