#!/usr/env python3
# -*- coding: utf-8 -*-

import sqlite3

class DataBase(object):
    def __init__(self, db_path):
        self.db_path = db_path

    def connect_db(self):
        rv = sqlite3.connect_db(self.db_path)
        rv.row_factory = sqlite3.Row
        return rv

        location /uploads {
            root   html;
        }