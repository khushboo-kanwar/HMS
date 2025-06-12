from rest_framework import serializers # type: ignore
from .models import Accounting, Invoice, DobleEntry
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name']


class AccountingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounting
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    issued_to = UserSerializer(read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class DobleEntrySerializer(serializers.ModelSerializer):
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())
    account = AccountingSerializer()

    class Meta:
        model = DobleEntry
        fields = '__all__'
