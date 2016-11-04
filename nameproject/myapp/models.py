from django.db import models
from mongoengine import Document, fields

class grades(Document):
    student_id = fields.IntField()
    type = fields.StringField()
    score = fields.DecimalField()
    more = fields.StringField()
    one = fields.StringField()


    def __repr__(self):
        return 'Studen id: ' + str(self.studen_id)


