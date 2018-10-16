#!/usr/bin/env python3

from news import get_most_popular_authors
from news import get_most_popular_articles
from news import get_days_with_more_than_error_rate

from concurrent.futures import ThreadPoolExecutor


if __name__ == '__main__':

    print('Running programs to query db ...\n')
    pool = ThreadPoolExecutor(max_workers=3)

    articles_future = pool.submit(get_most_popular_articles, 3)
    authors_future = pool.submit(get_most_popular_authors)
    error_rates_future = pool.submit(get_days_with_more_than_error_rate,
                                     0.01)

    articles = articles_future.result()
    question_one = "1. What are the most popular three articles of all time?"
    answer_one = "\n".join(list(map(
                           lambda record: '"{0}" - {1} views'.format(*record),
                           articles)))
    print(question_one)
    print(answer_one)
    print()

    authors = authors_future.result()
    question_two = "2. Who are the most popular article authors of all time??"
    answer_two = "\n".join(list(map(
                           lambda record: '{0} - {1} views'.format(*record),
                           authors)))
    print(question_two)
    print(answer_two)
    print()

    error_rates = error_rates_future.result()
    question_three = "3. On which days did more than 1% of requests " + \
                     "lead to errors?"
    answer_three = "\n".join(list(map(
                             lambda record: '{0} - {1} errors'.format(*record),
                             error_rates)))

    print(question_three)
    print(answer_three)
    print()

    with open('output.txt', 'w+') as file:

        print('writing output to output.txt ...\n')

        file.write(question_one)
        file.write('\n')
        file.write(answer_one)

        file.write('\n\n')

        file.write(question_two)
        file.write('\n')
        file.write(answer_two)

        file.write('\n\n')

        file.write(question_three)
        file.write('\n')
        file.write(answer_three)

        print('program output has been successfully written to output.txt')
