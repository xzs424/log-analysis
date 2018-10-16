CREATE VIEW request AS
      SELECT
        time::DATE AS day,
        CAST(COUNT(*) AS FLOAT)
      FROM log
      GROUP BY day;

CREATE VIEW error_request AS
      SELECT
        time::DATE AS day,
        CAST(COUNT(*) AS FLOAT)
      FROM log WHERE status != '200 OK'
      GROUP BY day;
