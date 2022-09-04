#!/usr/bin/python3
'''Initialize the model'''
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
