from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render



from .models import Transaction 

def test_db_connection(request):
    try:

        transactions = Transaction.objects.all()
        
 
        data = list(transactions.values())
        
        return JsonResponse({'status': 'success', 'data': data})
    except Exception as e:

        return JsonResponse({'status': 'error', 'message': str(e)})

import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Transaction
from .serializer import UserSerializer, TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = serializer.save()

    
        risk_score = self.detect_fraud(transaction)
        transaction.risk_score = risk_score
        transaction.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def detect_fraud(self, transaction):
       
        response = requests.post(
            'https://gemini-ai-api.com/detect',
            json={
                'amount': transaction.amount,
                'merchant': transaction.merchant,
                'timestamp': transaction.timestamp.isoformat()
            }
        )
        return response.json().get('risk_score', 0)
from django.http import JsonResponse
from .models import Transaction
from .ai_module import predict_fraud  

def test_db_connection(request):
    try:
    
        transactions = Transaction.objects.all()
        
    
        results = []

        for transaction in transactions:
          
            risk_score = predict_fraud(transaction)
            results.append({
                'id': transaction.id,
                'user_id': transaction.user_id,
                'amount': transaction.amount,
                'merchant': transaction.merchant,
                'risk_score': risk_score,
                'timestamp': transaction.timestamp
            })

        return JsonResponse({'status': 'success', 'data': results})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
