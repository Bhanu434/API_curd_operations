from django.shortcuts import render

# Create your views here.

from app.serializers import *
from rest_framework.response import Response
from app.models import *
from rest_framework.decorators import APIView

class Emp_curd(APIView):
    def get(self,request,empno):
        #EDO=Emp.objects.get(empno=empno)#retrive only perticuler data
        #JEDO=EmpModelSerializer(EDO)#return only on object 
        EDO=Emp.objects.all()# retrive all the data
        JEDO=EmpModelSerializer(EDO,many=True)# serializers the data(coverted ORM objects to Json Data),many=True is used for allowing the multipule rows od data 
        Jsondata=JEDO.data# converting objects to data
        return Response(Jsondata)
    def post(self,request,empno):# even though we not using empno we should give that variable other wise it wii through an error
        ESO=request.data # collect the data from user
        DSEO=EmpModelSerializer(data=ESO) # de-serializers the data(converting json data into ORM code)
        if DSEO.is_valid():
            DSEO.save() # save the data
            return Response({'data':'inserted Successfully'})
        else:
            return Response({'Error':' Data Not inserted '})
    def put(self,request,empno):
        EO=Emp.objects.get(empno=empno)
        JEDO=EmpModelSerializer(EO,data=request.data)#in this put method we should provide all the column data even though your not updated 
        if JEDO.is_valid():
            JEDO.save()
            return Response({'data':'data updated successfully'})
        else:
            return Response({'error':'data not updated '})
    def patch(self,request,empno):
        EO=Emp.objects.get(empno=empno)
        JEDO=EmpModelSerializer(EO,data=request.data,partial=True)# in the patch method we no need to provide all the column data . We should provide only what we want to update trhat column only provided.it will accept if you give all the collumns data
        if JEDO.is_valid():
            JEDO.save()
            return Response({'data':'data updated successfully'})
        else:
            return Response({'error':'data not updated '})
    def delete(self,request,empno):
        Emp.objects.get(empno=empno).delete()
        return Response({'data': 'data deleted succefully'})



        
    
