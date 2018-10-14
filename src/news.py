
from db.query_operations import fetchall


def get_most_popular_articles(num):

    '''
     First find the slug(derived from path column) and
     number of rows for each slug in table logs
     Then join the article table on the same slug
     so that every article has the corresponding
     number of views
    '''
    query = '''
            SELECT title, article_access.views
            FROM articles
              JOIN (
                SELECT substring(path,10) AS slug, count(*) AS views
                FROM log WHERE path LIKE %s GROUP BY slug
              ) AS article_access
                ON articles.slug = article_access.slug
            ORDER BY article_access.views DESC LIMIT %s
            '''

    result = fetchall(query, '/article/%', num)
    return result


def get_most_popular_authors():

    '''
    First find views/access of each article, then join it with article table.
    Then, group the views by author. After that join the author table,
    therefore we know for each author, what the toal
    view is.
    '''
    query = '''
             SELECT authors.name,
             CAST(SUM(article_access.views) AS INT) AS total_views
             FROM articles
               JOIN (
                  SELECT substring(path,10) AS slug, count(*) AS views
                  FROM log WHERE path LIKE %s GROUP BY slug
               ) AS article_access
                 ON articles.slug = article_access.slug
               JOIN authors
                 ON authors.id = articles.author
             GROUP BY authors.id ORDER BY total_views DESC
            '''

    result = fetchall(query, '/article/%')
    return result


def get_days_with_more_than_error_rate(num):

    '''
    First find number of records for each day.
    Then find record in log table where the status is not 200 OK for each day.
    After that, divide number of not-OK-status records by
    total number of records for that day.
    In the end, get day where error rate is greater than num
    '''

    query = '''
            CREATE VIEW request AS
                SELECT
                TO_CHAR(time::DATE,'Mon dd, yyyy') AS day,
                status,
                CAST(COUNT(*) AS FLOAT)
                FROM log GROUP BY day, status;

            SELECT request.day,
            ROUND(100.0 * (error_request.count/request.count)::NUMERIC, 1)
            || %s
            FROM request JOIN
                (
                  SELECT day, status, count FROM request
                  WHERE status != '200 OK'
                 ) AS error_request ON request.day = error_request.day
                 AND request.status != error_request.status
            WHERE error_request.count / request.count > %s
            '''
    result = fetchall(query, "%", num)

    return result
