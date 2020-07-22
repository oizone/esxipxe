def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    #open
    return [env[REQUEST_METHOD]]
