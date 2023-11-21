from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class TimeSeriesDataPoint:
    Time: str
    Value: Dict


@dataclass
class Datum:
    ScalarValue: Optional[str] = None
    TimeSeriesValue: Optional[List[TimeSeriesDataPoint]] = None
    ArrayValue: Optional[List] = None
    RowValue: Optional[Dict] = None
    NullValue: Optional[bool] = None


@dataclass
class ColumnInfo:
    Name: str
    Type: Dict
    ScalarType: Optional[str] = None
    ArrayColumnInfo: Optional[Dict] = None
    TimeSeriesMeasureValueColumnInfo: Optional[Dict] = None
    RowColumnInfo: Optional[List] = None


@dataclass
class QueryStatus:
    ProgressPercentage: float
    CumulativeBytesScanned: int
    CumulativeBytesMetered: int


@dataclass
class Row:
    Data: List[Datum]


@dataclass
class QueryResult:
    QueryId: str
    Rows: List[Row]
    ColumnInfo: List[ColumnInfo]
    QueryStatus: QueryStatus

    @staticmethod
    def from_dict(data: Dict) -> "QueryResult":
        rows = [
            Row([Datum(**datum) for datum in row_data["Data"]])
            for row_data in data["Rows"]
        ]
        column_info = [ColumnInfo(**info) for info in data["ColumnInfo"]]
        query_status = QueryStatus(**data["QueryStatus"])

        return QueryResult(
            QueryId=data["QueryId"],
            Rows=rows,
            ColumnInfo=column_info,
            QueryStatus=query_status,
        )
