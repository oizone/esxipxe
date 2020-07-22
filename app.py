def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    file=open("/tftp"+env['PATH_INFO'],'r')
    return [file.read()]
