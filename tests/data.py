query_result_data = {
    "QueryId": "12345",
    "Rows": [
        {
            "Data": [
                {"ScalarValue": "string_example"},
                {
                    "TimeSeriesValue": [
                        {"Time": "2023-11-21T12:00:00", "Value": {"key1": "value1"}},
                        {"Time": "2023-11-21T12:01:00", "Value": {"key2": "value2"}},
                    ]
                },
                {"ArrayValue": ["item1", "item2"]},
                {"RowValue": {"subkey1": "subvalue1", "subkey2": "subvalue2"}},
                {"NullValue": True},
            ]
        },
        # More rows can be added here
    ],
    "ColumnInfo": [
        {"Name": "column1", "Type": {"keyType": "valueType"}, "ScalarType": "string"},
        # More column info can be added here
    ],
    "QueryStatus": {
        "ProgressPercentage": 75.0,
        "CumulativeBytesScanned": 1024,
        "CumulativeBytesMetered": 2048,
    },
}
