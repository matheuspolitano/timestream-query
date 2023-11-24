from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class TimeSeriesDataPoint:
    """
    Time (string) –
    The timestamp when the measure value was collected.

    Value (dict) –
    The measure value for the data point.
    """

    Time: str
    Value: Dict


@dataclass
class Datum:
    """
    Datum represents a single data point in a query result.

    ScalarValue (string) –
    Indicates if the data point is a scalar value such as integer, string, double, or Boolean.

    TimeSeriesValue (list) –
    Indicates if the data point is a timeseries data type.

    ArrayValue (list) –
    Indicates if the data point is an array.

    RowValue (dict) –
    Indicates if the data point is a row.

    NullValue (boolean) –
    Indicates if the data point is null.
    """

    ScalarValue: Optional[str] = None
    TimeSeriesValue: Optional[List[TimeSeriesDataPoint]] = None
    ArrayValue: Optional[List] = None
    RowValue: Optional[Dict] = None
    NullValue: Optional[bool] = None


@dataclass
class ColumnInfo:
    """
    (dict) –
    Contains the metadata for query results such as the column names, data types, and other attributes.

    Name (string) –
    The name of the result set column.

    Type (dict) –
    The data type of the result set column.

    ScalarType (string) –
    Indicates if the column is of type string, integer, Boolean, double, timestamp, date, time.

    ArrayColumnInfo (dict) –
    Indicates if the column is an array.

    TimeSeriesMeasureValueColumnInfo (dict) –
    Indicates if the column is a timeseries data type.

    RowColumnInfo (list) –
    Indicates if the column is a row.
    """

    Name: str
    Type: Dict
    ScalarType: Optional[str] = None
    ArrayColumnInfo: Optional[Dict] = None
    TimeSeriesMeasureValueColumnInfo: Optional[Dict] = None
    RowColumnInfo: Optional[List] = None


@dataclass
class QueryStatus:
    """
    QueryStatus (dict) –
    Information about the status of the query, including progress and bytes scanned.

    ProgressPercentage (float) –
    The progress of the query, expressed as a percentage.

    CumulativeBytesScanned (integer) –
    The amount of data scanned by the query in bytes.

    CumulativeBytesMetered (integer) –
    The amount of data scanned by the query in bytes that you will be charged for.
    """

    ProgressPercentage: float
    CumulativeBytesScanned: int
    CumulativeBytesMetered: int


@dataclass
class Row:
    """
    (dict) –
    Represents a single row in the query results.

    Data (list) –
    List of data points in a single row of the result set.
    """

    Data: List[Datum]


@dataclass
class QueryResult:
    """
    QueryId (string) –
    A unique ID for the given query.

    Rows (list) –
    The result set rows returned by the query.

    ColumnInfo (list) –
    The column data types of the returned result set.

    QueryStatus (dict) –
    Information about the status of the query, including progress and bytes scanned.
    """

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
