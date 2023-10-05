from rest_framework.throttling import UserRateThrottle
from data.data import admin_token

class CustomUserRateThrottle(UserRateThrottle):
    rate = "10/minute" 
       
    def allow_request(self, request, view):
        # "X-Is-Admin" başlığı kontrolü ekleyin
        is_admin = request.META.get("Ba", "false").lower()
        if is_admin == "true":
            return True
        return super().allow_request(request, view)
    

class CustomBearerTokenRateThrottle(UserRateThrottle):
    rate = '10/minute'  # Özel sınıflandırma oranını ayarlayın

    def allow_request(self, request, view):
        # İstek başlığında "Authorization" bulunmalı ve "Bearer " ile başlamalı
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')

        if auth_header.startswith('Bearer '):
            # Bearer Token'i çıkar ve kontrol et
            bearer_token = auth_header[len('Bearer '):].strip()
            if self.validate_token(bearer_token):
                return True
        
        return super().allow_request(request, view)

    def validate_token(self, bearer_token):
        if bearer_token == admin_token:
            return True

        return False