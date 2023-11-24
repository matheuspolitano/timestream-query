# Timestream Project

## Overview
The Timestream project is designed to handle Amazon Timestream, a time-series database built for scale. This project is currently under development and aims to provide robust and efficient tools for managing and querying time-series data in Amazon Timestream.

## Developer
- **Name:** Matheus Politano
- **LinkedIn:** [Matheus Politano](https://www.linkedin.com/in/matheus-politano-08b762123/)
 


## Configuring credentials

There are two types of configuration data in application: credentials and non-credentials. Credentials include items such as aws-access-key-id, aws-secret-access-key, and aws-session-token on CLI. Non-credential configuration . For more information on how to configure non-credential configurations, see the [Configuration](https://boto3.amazonaws.com/v1/documentation/api/1.18.4/guide/configuration.html#guide-configuration) guide.

The application will look in several locations when searching for credentials. The mechanism in which The application looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. The order in which Boto3 searches for credentials is:

- Passing credentials as parameters in the CLI method
- Passing credentials as parameters when creating a Session object
- Environment variables
- Shared credential file (~/.aws/credentials)
- AWS config file (~/.aws/config)
- Assume Role provider
- Boto2 config file (/etc/boto.cfg and ~/.boto)
- Instance metadata service on an Amazon EC2 instance that has an IAM role configured.



## CLI Interface

Command: generate-csv

The generate-csv command is a part of a CLI tool designed to execute SQL queries on Amazon Timestream and export the results to a CSV file.

```
python main.py generate-csv --sql-file <path-to-sql-file> --csv-file <path-for-csv-output> --region <table-region> [OPTIONS]

```

## Development Status
The project is in the development phase. Regular updates will be made to this repository as the project progresses.


## Features (Planned/Current)
- [ ] Interface for querying Amazon Timestream data.
- [ ] Tools for efficient data ingestion and management.
- [ ] (Add more as they become relevant)

## Contributing
As this project is in its early stages, contributions, ideas, and feedback are highly welcome. Please feel free to reach out through the contact information provided or submit an issue/pull request in this repository.

## License
MIT License

Copyright (c) 2023 Matheus Politano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This README will be updated as the project develops further.
