def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    if(env['PATH_INFO'].split('/')[1]=="cd"):
        return ["JOO CEEDEE"]
    else:
        file=open("/tftp"+env['PATH_INFO'],'r')
        return [file.read()]
