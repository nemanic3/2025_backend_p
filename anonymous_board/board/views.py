from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostListCreateAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('-create_date')
        serializer = PostSerializer(posts, many=True)
        return Response({'posts': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "성공적으로 등록됐습니다."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView):
    def get(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()
        if not post:
            return Response({
                "status_code": 404,
                "error": "POST_NOT_FOUND",
                "message": "존재하지 않는 게시글입니다."
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CommentView(APIView):
    def get(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()
        if not post:
            return Response({
                "status_code": 404,
                "error": "POST_NOT_FOUND",
                "message": "존재하지 않는 게시글입니다."
            }, status=status.HTTP_404_NOT_FOUND)

        comments = Comment.objects.filter(post=post).order_by('-create_date')
        serializer = CommentSerializer(comments, many=True)
        return Response({"comments": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()
        if not post:
            return Response({
                "status_code": 404,
                "error": "POST_NOT_FOUND",
                "message": "존재하지 않는 게시글입니다."
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response({"message": "성공적으로 등록됐습니다."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
