import os
import sys

class CliManagement():
    def __init__(self,dir,model,fields,serializer,viewset,filter_fields,order_fields,argv):
        self.app_dir = os.path.join(os.getcwd(),sys.argv[2])
        pass

    def create_viewset(self,app_dir,name,filter_fields,order_fields,model,serializer):
        file_path = os.path.join(app_dir,'views.py')
        filter_fields = filter_fields.split(',')
        filter_fields= map(lambda x:''.join(['\'',x,'\'']),filter_fields)
        filter_fields = ','.join(list(filter_fields))

        order_fields = order_fields.split(',')
        order_fields= map(lambda x:''.join(['\'',x,'\'']),order_fields)
        order_fields = ','.join(list(order_fields))

        
        f = open(file_path, 'w')
        f.write(f'''from rest_framework import viewsets
    from rest_framework.filters import OrderingFilter
    from django_filters.rest_framework import DjangoFilterBackend
    from .models import {model}
    from .serializers import {serializer}

    class {name}(viewsets.ModelViewSet):
        serializer_class = {serializer}
        queryset = {model}.objects.all()
        filter_backends = [DjangoFilterBackend, OrderingFilter]
        ordering_fields = [{order_fields}]
        filterset_fields = [{filter_fields}]
        ''')
        f.close()
    pass
