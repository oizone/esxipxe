import os
def application(env, start_response):
    filename="/tftp"+env['PATH_INFO']
    if(os.path.isfile(filename)):
       if(env['PATH_INFO'].split('/')[1]=="cd"):
           start_response('200 OK', [('Content-Type','application/x-binary')])
           return ["JOO CEEDEE"]
           file=open(filename,'r')
           return [file.read()]
       else:
           start_response('200 OK', [('Content-Type','text/plain')])
           file=open(filename,'r')
           return [file.read()]
    else:
        start_response('404 Not Found',[('Content-Type','text/plain')])
        return ["Not Found"]
        
