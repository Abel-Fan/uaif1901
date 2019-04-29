from flask import session,redirect
from functools import wraps

def authlogin(fn):
    @wraps(fn)
    def newFn(*args,**kwargs):
        username = session.get("username",None)
        print(username)
        if username:
            return fn(*args,**kwargs)
        else:
            return redirect("login")
    return newFn