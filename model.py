from google.appengine.ext import ndb

class LunchRequest(ndb.Model):
    """Models a single request to have lunch."""
    requester = ndb.UserProperty()
    target_date = ndb.DateTimeProperty()
    last_modified = ndb.DateTimeProperty(auto_now_add=True)
