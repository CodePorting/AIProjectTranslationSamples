from django.shortcuts import render
from django.views import View
from django.http import HttpResponseServerError

class CrashView(View):
    def get(self, request):
        raise RuntimeError("Expected: controller used to showcase what happens when an exception is thrown")
