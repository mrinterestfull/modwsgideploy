#Test modwsgi.
#Hello world test application to make sure modwsgi runs. Uncomment only this sections below to test. Install in appropriate folders and restart apache.

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'
    #print >> sys.stderr, "sys.stderr"
    #print >> environ["wsgi.errors"], "wsgi.errors" 
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]


