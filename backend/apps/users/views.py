"""
User views for API.
"""
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import User, UserProfile, Wishlist
from .serializers import UserSerializer, UserUpdateSerializer, UserProfileSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    """Get or update current user's profile."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(generics.UpdateAPIView):
    """Update extended profile information."""
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        return profile


class WishlistView(generics.ListCreateAPIView):
    """List and add to wishlist."""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user).select_related('tour')

    def create(self, request, *args, **kwargs):
        tour_id = request.data.get('tour_id')
        if not tour_id:
            return Response({'error': 'tour_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        wishlist, created = Wishlist.objects.get_or_create(
            user=request.user,
            tour_id=tour_id
        )
        if created:
            return Response({'message': 'Added to wishlist'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Already in wishlist'}, status=status.HTTP_200_OK)


class WishlistDeleteView(generics.DestroyAPIView):
    """Remove from wishlist."""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        tour_id = kwargs.get('tour_id')
        deleted, _ = Wishlist.objects.filter(user=request.user, tour_id=tour_id).delete()
        if deleted:
            return Response({'message': 'Removed from wishlist'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Not in wishlist'}, status=status.HTTP_404_NOT_FOUND)
