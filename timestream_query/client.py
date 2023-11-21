import boto3
from typing import List
from boto3.session import Session
from timestream_query.data_handle import QueryResult


class TimeStreamQuery:
    def __init__(self, session: Session = None):
        self.session = session
        self.client = self._define_client()

    def _define_client(self):
        if self.session is None:
            return boto3.client("timestream-query")
        return self.session.client("timestream-query")

    def execute_query(self, query: str) -> QueryResult:
        rows = []
        paginator = self.client.get_paginator("query")

        for page in paginator.paginate(QueryString=query):
            last_page = page
            for row in page["Rows"]:
                rows.append(row)
        last_page["Rows"] = rows
        return QueryResult.from_dict(last_page)
