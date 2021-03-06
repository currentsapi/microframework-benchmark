from locust import HttpLocust, TaskSet, task
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

HOST = '0.0.0.0'
PORT = 8000

class JsonTasks(TaskSet):
    
    @task
    def index(self):
        self.client.get("/json")

class JsonUser(HttpLocust):
    host = "http://{}:{}".format(HOST, PORT)
    task_set = JsonTasks
    min_wait = 5000
    max_wait = 15000