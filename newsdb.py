import psycopg2
import bleach

DBNAME = "news"


def test_connection():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from logs")
    # articles = c.fetchall()
    if c:
        print("Connected.")
        db.close
    else:
        print("connection failed.")


def popular_articles():
    db = psycopg2.connect(database=DBNAME)
    curr = db.cursor()
    curr.execute("""Select articles.title, count(articles.slug) AS COUNT
                       FROM articles INNER JOIN log
                         ON articles.slug like split_part(log.path,\'/\',3)
                   GROUP BY articles.title
                   ORDER BY COUNT DESC LIMIT 3
                 """)
    articles = curr.fetchall()
    print("What are the most popular three articles of all time?")
    for r in articles:
        print('"'+r[0]+'" -- ' + str(r[1]) + " views")
    db.close


def popular_authors():
    db = psycopg2.connect(database=DBNAME)
    curr = db.cursor()
    curr.execute("""Select authors.name, count(authors.name) AS Count
                      FROM authors INNER JOIN articles
                        ON authors.id = articles.author INNER JOIN log
                        ON articles.slug like split_part(log.path,\'/\',3)
                  GROUP BY authors.name
                  ORDER BY Count DESC
                """)
    authors = curr.fetchall()
    print("Who are the most popular article authors of all time?")
    for r in authors:
        print(r[0] + ' -- ' + str(r[1]) + "views")
    db.close


def percentage(part, whole):
    return 100 * float(part)/float(whole)


def requesrt_errors():
    db = psycopg2.connect(database=DBNAME)
    curr = db.cursor()
    curr.execute("""SELECT total_count.date, total_count.total_count_per_day
        AS Total, total_count_failed.total_count_per_day AS Failed
        FROM total_count INNER JOIN total_count_failed
        ON total_count.date = total_count_failed.date
        WHERE (total_count_failed.total_count_per_day*100)/
        total_count.total_count_per_day > 0.01
    """)
    authors = curr.fetchall()
    print("On which days did more than 1% of requests lead to errors?")
    # print(authors[0])
    for r in authors:
        print(
            r[0] + '--' + "{:4.4}".format(str(percentage(r[2], r[1]))) +
            "% errors")
    db.close
    # {:10.4f} format float

popular_articles()
print("\n")
popular_authors()
print("\n")
requesrt_errors()
