#!/usr/bin/env python3
"""Here are the questions the reporting tool should answer.

    1. What are the most popular three articles of all time? Which articles
    have been accessed the most? Present this information as a sorted list
    with the most popular article at the top.
    Example:

        "Princess Shellfish Marries Prince Handsome" — 1201 views
        "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
        "Political Scandal Ends In Political Scandal" — 553 views

    2. Who are the most popular article authors of all time? That is, when
    you sum up all of the articles each author has written, which authors get
    the most page views? Present this as a sorted list with the most popular
    author at the top.
    Example:

        Ursula La Multa — 2304 views
        Rudolf von Treppenwitz — 1985 views
        Markoff Chaney — 1723 views
        Anonymous Contributor — 1023 views

    3. On which days did more than 1% of requests lead to errors? The log
    table includes a column status that indicates the HTTP status code that
    the news site sent to the user's browser. (Refer to this lesson for more
    information about the idea of HTTP status codes.)
    Example:

        July 29, 2016 — 2.5% errors

    Rubric: https://review.udacity.com/#!/rubrics/277/view
    """

import psycopg2


db = psycopg2.connect("dbname=news")
cur = db.cursor()

# 1. What are the three most popular articles of all time?
query = """
SELECT articles.title, count(log.path) AS views
       FROM articles, log
       WHERE (log.path like '%' || articles.slug AND log.status like '200%')
       GROUP BY log.path, articles.title
       ORDER BY views DESC
       LIMIT 3
"""

cur.execute(query)
articles = cur.fetchall()

for article in articles:
    print('"{}" – {} views'.format(article[0], article[1]))


# 3. ...abs
# query = 'select id, time::date, status from log'
# select time::date, count(status) from log group by time::date limit 10;
