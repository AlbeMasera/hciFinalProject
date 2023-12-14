from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .helpers import predict

class Predict(APIView):
    """
    List all text files, or create a new text file.
    """

    def post(self, request, format=None):
        data = request.data
        text_list = []
        for text in data["text_list"]:
            text = text.replace('\n',' ')
            text_list.append(text)
        answer = predict(text_list)
        if len(answer)!=0:
            pos_count = answer.count(1)
            if pos_count >= 0.75*(len(answer)):

                return Response({"message":"Suicidal content warning"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"Safe content"}, status=status.HTTP_201_CREATED)
        return Response({"message":"Fail"}, status=status.HTTP_400_BAD_REQUEST)