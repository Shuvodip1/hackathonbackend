from rest_framework import views, response
from . import serializer, models

# Create your views here.


class AppointmentView(views.APIView):
    def get(self, request):
        try:
            serialized = serializer.AppointmentSerializer(
                models.Appointment.objects.all(), many=True)
            return response.Response({
                'appointments': serialized.data,
                'bed_no': models.Bed.objects.all().first().bed_no
            }, status=200)
        except Exception as e:
            return response.Response({'error': str(e)}, status=400)

    def post(self, request):
        try:
            serialized = serializer.AppointmentSerializer(
                data=request.data)
            if serialized.is_valid():
                serialized.save()
                if serialized.data['is_book'] == True:
                    bed = models.Bed.objects.all().first()
                    bed.bed_no += 1
                    bed.save()
                return response.Response(serialized.data, status=201)
            else:
                return response.Response(serialized.errors, status=400)
        except Exception as e:
            return response.Response({'error': str(e)}, status=400)


class ContactView(views.APIView):
    def get(self, request):
        try:
            serialized = serializer.ContactSerializer(
                models.Contact.objects.all(), many=True)
            return response.Response(serialized.data, status=200)
        except Exception as e:
            return response.Response({'error': str(e)}, status=400)

    def post(self, request):
        try:
            serialized = serializer.ContactSerializer(
                data=request.data)
            if serialized.is_valid():
                serialized.save()
                return response.Response(serialized.data, status=201)
            else:
                return response.Response(serialized.errors, status=400)
        except Exception as e:
            return response.Response({'error': str(e)}, status=400)
