"""
Exception extention for Jycore AI Project
"""


class QueryError(Exception):
    def __init__(self, message="Error in provided query"):
        super(QueryError).__init__()
