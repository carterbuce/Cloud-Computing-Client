import json
import random
import string

import sys
from locust import TaskSet, task, HttpLocust, main
from locust.events import quitting


# run 'locust --host=http://{server url:port}' in terminal, and go to http://localhost:8089
# must set gevent compatible in pycharm settings and add `--host http://localhost:5000` to run config
class AutoScalingTasks(TaskSet):

    @task
    def reverse_strings(self):
        # generate a random 124 character string and POST it
        original = ''.join(random.choices(string.ascii_uppercase, k=124))
        self.client.post('/reverse', json={'string': original})


class MeasureAutoScaling(HttpLocust):
    task_set = AutoScalingTasks


if __name__ == '__main__':
    main.main()
