#!/usr/bin/python3
"""
Create unique FileStorage
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
