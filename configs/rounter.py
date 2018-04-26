from handles.MainHandler import MainHandler

from handles.LoginHandler import LoginHandler

from handles.Api.H5testHandler import H5testHandler

from handles.Api.QaHandler import QaHandler
def rounterConfig():
    return [
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/api/h5test", H5testHandler),
        (r"/api/qa", QaHandler)
        ]
