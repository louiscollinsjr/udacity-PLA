# udacity-PLA
Project: Logs Analysis

# Project: Logs Analysis

Reporting application to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

# So what are we reporting, anyway?

Here are the questions the reporting tool should answer. 

1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

## Getting Started

Will will need to have newsdata.sql.

### Connecting from your code

The database that you're working with in this project is running PostgreSQL. So in your code, you'll want to use the psycopg2 Python module to connect to it, for instance:

db = psycopg2.connect("dbname=news")

### Import using the command: psql -d news -f newsdata.sql.

The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.



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
