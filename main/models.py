# #models.py
# from django.db import models


# class Document(models.Model):
#     upload_by = models.ForeignKey('auth.User', related_name='uploaded_documents', on_delete=models.PROTECT)
#     datestamp = models.DateTimeField(auto_now_add=True)
#     document = models.ImageField(upload_to='uploads/')
#     # ...
#     def __unicode__(self):
#        return self.document


# class MainModel(models.Model):
#     title = models.CharField(max_length=42)
#     document = models.ForeignKey(Document, on_delete=models.PROTECT)
#     #...