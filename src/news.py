
from db.query_operations import fetchall


def get_most_popular_articles(num, *args):

    """
     First find the slug(derived from path column) and
     number of rows for each slug in table logs
     Then join the article table on the same slug
     so that every article has the corresponding
     number of views
    """

    """
    Without using subquery - it is slower since you have to
    join every row in the log before aggregation

    SELECT articles.title, count(*) as views || ' views'
    FROM log
        JOIN articles
          ON log.path = CONCAT('/article/', articles.slug)
    GROUP BY articles.title, articles.slug
    ORDER BY views DESC LIMIT %s

    """

    query = '''
        SELECT title, article_access.views || ' views'
        FROM articles
           JOIN (
                 SELECT substring(path,10) AS slug, count(*) AS views
                 FROM log WHERE path LIKE %s GROUP BY slug
                ) AS article_access
           ON articles.slug = article_access.slug
        ORDER BY article_access.views DESC LIMIT %s
    '''

    result, time_cost = fetchall(query, '/article/%', num)

    return result, time_cost


def get_most_popular_authors(*args):

    '''
    First find views/access of each article, then join it with article table.
    Then, group the views by author. After that join the author table,
    therefore we know for each author, what the toal
    view is.

    This is one way of doing it using subquery
    SELECT authors.name,
            CAST(SUM(article_access.views) AS INT) || 'views' AS total_views
             FROM articles
               JOIN (
                  SELECT substring(path,10) AS slug, count(*) AS views
                  FROM log WHERE path LIKE '/article/%' GROUP BY slug
               ) AS article_access
                 ON articles.slug = article_access.slug
               JOIN authors
                 ON authors.id = articles.author
             GROUP BY authors.id ORDER BY total_views DESC
    '''

    # Without using subquery, it is slower than using subquery
    # since you have to join before aggregation
    query = '''
             SELECT authors.name,
                    count(*) || ' views' as views
             FROM log
                  JOIN articles
                    ON log.path = CONCAT('/article/', articles.slug)
                  JOIN authors
                    ON authors.id = articles.author
             GROUP BY authors.id
             ORDER BY views DESC
            '''

    result, time_cost = fetchall(query)

    return result, time_cost


def get_days_with_more_than_error_rate(num, *args):

    '''
    First find number of records for each day.
    Then find record in log table where the status is not 200 OK for each day.
    After that, divide number of not-OK-status records by
    total number of records for that day.
    In the end, get day where error rate is greater than num
    '''

    query = '''
            SELECT
                TO_CHAR(request.day::DATE,'Mon dd, yyyy'),
                ROUND(100.0 * (error_request.count/request.count)::NUMERIC, 2)
                    || %s || ' errors'
            FROM request
            LEFT JOIN error_request
                 ON request.day = error_request.day
            WHERE error_request.count / request.count > %s
            '''

    result, time_cost = fetchall(query, "%", num)

    return result, time_cost
