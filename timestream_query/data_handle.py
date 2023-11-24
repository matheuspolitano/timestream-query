from dataclasses import dataclass
from typing import List, Dict, Optional, Any


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
        """
        Creates a QueryResult instance from a dictionary.
        Args:
            data (Dict): A dictionary containing the query result data.

        Returns:
            QueryResult: An instance of QueryResult populated with data from the input dictionary.

        """
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

    def get_columns_and_data(self) -> (List[str], List[List[Any]]):
        """
        Extracts columns and their corresponding data from query results.

        Returns:
            Tuple[List[str], List[List[Any]]]: A tuple containing two elements:
                - A list of column names.
                - A list of lists, where each inner list represents a row of data.
        """
        if not hasattr(self, "ColumnInfo") or not hasattr(self, "Rows"):
            raise AttributeError("ColumnInfo or Rows not found in the QueryResult")

        columns = [col.Name for col in self.ColumnInfo]

        data = [
            [self._extract_datum_value(datum) for datum in row.Data]
            for row in self.Rows
        ]

        return columns, data

    @staticmethod
    def _extract_datum_value(datum: Datum):
        """
        Extracts the value from a Datum object.

        This method checks the type of value contained in the Datum object and returns it.
        It currently supports the following types:
        - ScalarValue: Returns the scalar value if it's present.
        - ArrayValue: Returns the array value if it's present.
        If the Datum object does not contain a recognized type, None is returned.

        Args:
            datum (Datum): The Datum object from which to extract the value.

        Returns:
            Any: The extracted value from the Datum object, or None if no recognized type is found.
        """
        if datum.ScalarValue is not None:
            return datum.ScalarValue
        elif datum.ArrayValue is not None:
            return datum.ArrayValue
        return None
