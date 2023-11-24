import boto3
from typing import List
from boto3.session import Session
from timestream_query.data_handle import QueryResult


class TimeStreamQuery:
    def __init__(self, session: Session = None, region="us-east-1"):
        self.session = session
        self.client = self._define_client(region)

    def _define_client(self, region):
        if self.session is None:
            return boto3.client("timestream-query", region_name=region)
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
