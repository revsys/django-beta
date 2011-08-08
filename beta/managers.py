from django.db import models

class BetaManager(models.Manager):

    def contacted(self):
        return self.get_query_set().filter(contacted=True) 

    def not_contacted(self):
        return self.get_query_set().filter(contacted=False) 

    def registered(self): 
        return self.get_query_set().filter(registered=True) 

    def not_registered(self): 
        return self.get_query_set().filter(registered=False) 

