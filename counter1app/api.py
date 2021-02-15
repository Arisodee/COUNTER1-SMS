from rest_framework import generics
from rest_framework.response import Response
from .serializer import ContactSerializer
from .models import Contact


class ContactCreateApi(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactApi(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDeleteApi(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
