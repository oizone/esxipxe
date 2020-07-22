def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    #open
    return [env['PATH_INFO']]
