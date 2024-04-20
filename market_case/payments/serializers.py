from rest_framework import serializers


class MailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=200)
    message = serializers.CharField()
    recipient_list = serializers.ListField()


