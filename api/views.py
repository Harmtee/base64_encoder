import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DecodePayloadSerializer
from .utils import encode_payload, decode_payload



class EncodeView(APIView):
    def post(self, request):         
        try:
            encoded_payload, salt_key, salt_index = encode_payload(request.data)
            return Response({"encoded_payload": encoded_payload, "salt_key": salt_key, "salt_index": salt_index}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class DecodeView(APIView):
    def post(self, request):
        serializer = DecodePayloadSerializer(data=request.data)
        if serializer.is_valid():
            encoded_payload = serializer.validated_data["encoded_payload"]
            salt_key = serializer.validated_data["salt_key"]
            salt_index = serializer.validated_data["salt_index"]
            
            try:
                decoded_payload = decode_payload(encoded_payload, salt_key, salt_index)
                return Response({"decoded_payload": decoded_payload}, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
