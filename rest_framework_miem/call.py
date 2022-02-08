from tkinter.messagebox import NO
from django.core import management
import sys
import os
import re 
import enum

class FieldType(enum.Enum):
    STR = 'models.CharField'
    INT = 'models.IntegerField'
    BOOL = 'models.BooleanField'

def text_to_fields(txt):
    txt_arr = txt.split( )
    lst = []

    for field in txt_arr:
        match = re.search(r'\[\d+\]',field)
        max_length = ''

        if match is not None:
            start_index = match.start()
            max_length = field[start_index+1:match.end()-1]
            field = field[:start_index]

        field_name,field_type = field.split(":")
        field_json = {field_name:field_type}
        django_field = None

        for e in FieldType:
            if field_type == e.name.lower():
                django_field = e.value

        if django_field is None:
            raise Exception()

        field_text = ''.join(['\t',field_name,' = ',django_field,'('])

        if max_length != '':
            field_text = ''.join([field_text,max_length])
        
        field_text = ''.join([field_text,')\n'])

        lst.append(field_text)
    
    return lst

def create_model(name,fields):
    f = open("./snackfor/models.py", 'a')
    f.write(''.join(['class ',name,'(models.Model):\n']))

    for field in fields:
        f.write(field)

    f.close()

def create_serializer(name,model):
    f = open("./snackfor/serializers.py", 'w')
    f.write(f'''from rest_framework import serializers
from .models import {model}

class {name}(serializers.ModelSerializer):
    class Meta:
        model = {model}
        fields = '__all__'
    ''')
    f.close()

def create_viewset(name,filter_fields,order_fields,model,serializer):
    filter_fields.split(',')
    order_fields.split(',')
    f = open("./snackfor/views.py", 'w')
    f.write(f'''from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import {model}
from .serializers import {serializer}

class {name}(viewsets.ModelViewSet):
    serializer_class = {serializer}
    queryset = {model}.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['registration_date']
    ''')
    f.close()

if __name__ == "__main__":
    # path = os.path.join(os.getcwd(),'rest_framework_miem/src/')
    # # print(path)
    # # management.execute_from_command_line([
    # #             "C:\\git\\drf_extends_error_message\\rest_framework_miem\\call.py",
    # #             "startapp",
    # #             "call",
    # #             path
    # #         ])

    # management.execute_from_command_line([
    #             "C:\\git\\drf_extends_error_message\\rest_framework_miem\\call.py",
    #             "startapp",
    #             "snackfor"
    #         ])
    # 'name:string[50] num:int is_bool:bool'
    # model = input('model name: ')
    # fields = input('fields: ')
    # viewset = input('viewset name: ')
    # filter_fields = input('filter fields: ')
    # order_fields = input('order fields: ')
    # serializer = input('serializer name: ')

    model = 'User'
    fields = 'name:str[50] num:int is_bool:bool'
    viewset = ''
    filter_fields = ''
    order_fields = ''
    serializer = ''

    if viewset == '':
        viewset = ''.join([model,'ViewSet'])

    if serializer == '':
        serializer = ''.join([model,'Serializer'])

    fields = text_to_fields(fields)
    create_model(model,fields)
    create_serializer(serializer,model)
    create_viewset(viewset,filter_fields,order_fields,model,serializer)
    # print('done')
    # management.execute_from_command_line(sys.argv)

# python 3.6 
