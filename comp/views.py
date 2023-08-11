from .serializers import Computerserializers
from rest_framework.views import APIView
from .models import Computers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED

class ComplistALLView(APIView):
    def get (self,request,*args,**kwargs):
        all_comps=Computers.objects.all()
        serializers=ComplistALLView(all_comps,many=True)
        return Response(serializers.data)
class CompDetalesView(APIView):
    def get (self,request,*args,**kwargs):
        comp_id=kwargs['comp_id']
        comp=get_object_or_404(Computers,id=comp_id)
        serializer=Computerserializers
        return Response(serializer.data)
class CompCreateView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=Computerserializers(data=request,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.data)
class CompUpdateView(APIView):
    def put(self,request,*args,**kwargs):
        comp=get_object_or_404(Computers,id=kwargs['comp_id'])
        serializers=Computerserializers(Computers,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
class CompDeleteView(APIView):
    def __delete__(self,request,*args,**kwargs):
        comp=get_object_or_404(Computers,id=kwargs['comp_id'])
        serializers=Computerserializers(Computers,data=request.data)
        comp.delete()
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response({"Din Don":"uje DELTED"})

