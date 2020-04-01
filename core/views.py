from django.shortcuts import render
from django.http import JsonResponse


from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics



from .serializers import PostSerializer
from .models import Post

#(1)
# Here we need to implement the post and get method
class TestView(APIView):

    permission_classes = (IsAuthenticated, )


    def get(self, request, *args, **kwargs):
        # query serialize returns all the objects
        qs = Post.objects.all()
        post = qs.first()
        #serializer = PostSerializer(qs, many=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # tipically when you sent a post resquest to create something
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


#(2)
# So, we abstract (1) futher into mixins
class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#(3)
# And we abstract to a generic API, that has all the functionality that we need
# for a post method endpoint
class PostCreateView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

#(4)
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

















    #def perform_create(self, serializer):
        # send an email, implement the logic
    #    serializer.save()



