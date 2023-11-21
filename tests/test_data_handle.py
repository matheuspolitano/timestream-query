import unittest
from timestream_query.data_handle import (
    QueryResult,
)  # Replace with the actual module name
from tests.data import query_result_data


class TestDataHandle(unittest.TestCase):
    def setUp(self):
        self.query_result = QueryResult.from_dict(query_result_data)

    def test_query_id(self):
        self.assertEqual(self.query_result.QueryId, query_result_data["QueryId"])

    def test_rows_length(self):
        self.assertEqual(len(self.query_result.Rows), len(query_result_data["Rows"]))

    def test_column_info(self):
        self.assertEqual(
            len(self.query_result.ColumnInfo), len(query_result_data["ColumnInfo"])
        )

    def test_query_status(self):
        self.assertIsInstance(self.query_result.QueryStatus.ProgressPercentage, float)
        self.assertIsInstance(self.query_result.QueryStatus.CumulativeBytesScanned, int)
        self.assertIsInstance(self.query_result.QueryStatus.CumulativeBytesMetered, int)

    # Add more tests as necessary


if __name__ == "__main__":
    unittest.main()
