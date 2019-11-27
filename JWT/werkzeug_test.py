from werkzeug.security import generate_password_hash, check_password_hash

from werkzeug.wrappers import Request, Response

from jinja2 import Environment, FileSystemLoader

@Request.application
def application(request):
    pwd = generate_password_hash('123')
    return Response(pwd)

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 5000, application)