# udacity-PLA
Project: Logs Analysis

# PProject: Logs Analysis

Reporting application to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Getting Started

Will will need to have newsdata.sql.

Import using the command: psql -d news -f newsdata.sql.

### You will also need to create two additonal views by running the commands:

CREATE VIEW total_count_failed AS  SELECT to_char(log."time"::timestamp without time zone::date::timestamp with time zone, 'Month DD, YYYY'::text) AS date, count(log.status) AS total_count_per_day FROM log WHERE log.status <> '200 OK'::text GROUP BY (log."time"::timestamp without time zone::date) ORDER BY (to_char(log."time"::timestamp without time zone::date::timestamp with time zone, 'Month DD, YYYY'::text));;


CREATE VIEW total_count AS  SELECT to_char(log."time"::timestamp without time zone::date::timestamp with time zone, 'Month DD, YYYY'::text) AS date, count(log.status) AS total_count_per_day FROM log GROUP BY (log."time"::timestamp without time zone::date) ORDER BY (to_char(log."time"::timestamp without time zone::date::timestamp with time zone, 'Month DD, YYYY'::text));;


### Prerequisites

Python miust be installed.

### running the application

python newsdb.py

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* udacity rocks.
