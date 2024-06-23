from rest_framework import serializers

class DecodePayloadSerializer(serializers.Serializer):
    encoded_payload = serializers.CharField()
    salt_key = serializers.CharField()
    salt_index = serializers.IntegerField()