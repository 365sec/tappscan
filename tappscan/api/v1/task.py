from flask_restplus import Namespace, Resource


task_namespace = Namespace("task", description="Endpoint to retrieve task")

@task_namespace.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
        