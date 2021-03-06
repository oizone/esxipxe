import os
def application(env, start_response):
    filename="/tftp/config/"+env['PATH_INFO']
    host=env['PATH_INFO'].split('/')[1]
    if(os.path.isfile(filename)):
        start_response('200 OK', [('Content-Type','text/plain')])
        file=open(filename,'r').read()
        os.remove("/tftp/pxelinux.cfg/"+host)
        os.remove("/tftp/"+host+"/boot.cfg")
        os.remove(filename)
        return [file]
    else:
        start_response('404 Not Found',[('Content-Type','text/plain')])
        return ["Not Found"]
        
