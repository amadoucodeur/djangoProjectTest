from rest_framework import generics
from .models import Model3d, Badge, UserProfile
from .serializers import Model3dSerializer, BadgeSerializer, UserProfileSerializer
from pprint import pprint


class Model3dListCreateView(generics.ListCreateAPIView):
    queryset = Model3d.objects.all()
    serializer_class = Model3dSerializer

class Model3dDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Model3d.objects.all()
    serializer_class = Model3dSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        
        if instance.views >= 1000:
            user_profile = instance.user.userprofile
            badge = Badge.objects.get(name="Star")  

            if badge not in user_profile.badge.all():
                user_profile.badge.add(badge)
                print("badge ajouté")
        return super().retrieve(request, *args, **kwargs)

class BadgeListCreateView(generics.ListCreateAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class BadgeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Vérifiez depuis combien de temps l'utilisateur est inscrit
        from datetime import datetime
        from dateutil.relativedelta import relativedelta
        current_date = datetime.now()
        registration_date = instance.account.date_joined
        time_difference = relativedelta(current_date, registration_date)

        if time_difference.years >= 1:
            pioneer_badge = Badge.objects.get(name="Pioneer")  

            if pioneer_badge not in instance.badge.all():
                instance.badge.add(pioneer_badge)  

        return super().retrieve(request, *args, **kwargs)