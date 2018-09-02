import json
import random
import string

import sys
from locust import TaskSet, task, HttpLocust, main


# run 'locust --host=http://{server url:port}' in terminal, and go to http://localhost:8089
# must set gevent compatible in pycharm settings and add `--host http://localhost:5000` to run config
class AutoScalingTasks(TaskSet):

    @task
    def reverse_strings(self):
        # generate a random 124 character string and POST it
        original = ''.join(random.choices(string.ascii_uppercase, k=124))
        with self.client.post('/reverse', json={'string': original},
                              catch_response=True) as response:
            try:
                original_reversed = json.loads(response.text)['reversed']
                if original[::-1] != original_reversed:
                    response.failure('reversed string')
            except:
                e = sys.exc_info()[0]
                response.failure(str(e))


class MeasureAutoScaling(HttpLocust):
    task_set = AutoScalingTasks


if __name__ == '__main__':
    main.main()
