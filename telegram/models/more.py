"""
Model for more response container
"""

from __future__ import annotations
from typing import List

from pydantic import BaseModel

from telegram.models.post import Post
from telegram.models.meta import Meta


class More(BaseModel):
    """
    Represents additional content retrieved from a Telegram channel.

    Attributes:
        posts (List[Post]): List of posts.
        meta (Meta): Metadata associated with the additional content.
    """
    posts: List[Post]
    meta: Meta
