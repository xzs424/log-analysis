#!/usr/bin/env python3

from news import get_most_popular_authors
from news import get_most_popular_articles
from news import get_days_with_more_than_error_rate

from concurrent.futures import ThreadPoolExecutor
import time

if __name__ == '__main__':

    print('Running programs to query db ...\n')

    pool = ThreadPoolExecutor(max_workers=3)

    tasks = [
     (get_most_popular_articles, 3),
     (get_most_popular_authors, None),
     (get_days_with_more_than_error_rate, 0.01)
    ]

    questions = [
        "1. What are the most popular three articles of all time?",
        "2. Who are the most popular article authors of all time?",
        "3. On which days did more than 1% of requests lead to errors?"
    ]

    # Create futures/Promises array
    futures = [pool.submit(task[0], task[1]) for task in tasks]

    answers = []
    time_costs = []

    for question, future in \
            zip(questions, futures):

        result, time_cost = future.result()

        answer = "\n".join(list(map(
            lambda record: '"{0}" - {1}'.format(*record), result)))

        answers.append(answer)
        time_costs.append(time_cost)

        print(question)
        print(answer)
        print('The query takes {0} seconds'.format(time_cost))
        print()

    with open('output.txt', 'w+') as file:

        print('writing output to output.txt ...\n')

        for question, answer, time_cost \
                in zip(questions, answers, time_costs):
            file.write(question)
            file.write('\n')
            file.write(answer)
            file.write('\n')
            file.write('The query takes {0} seconds'.format(time_cost))
            file.write('\n\n')

        print('program output has been successfully written to output.txt')
