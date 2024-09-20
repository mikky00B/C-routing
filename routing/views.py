from django.shortcuts import render
import googlemaps
from .models import Route

# Create your views here.


def get_locations(request):
    if request.method == "POST":
        location1 = request.POST.get("location1")
        location2 = request.POST.get("location2")

        gmaps = googlemaps.Client(key="YOUR_API_KEY")
        loc1_coords = gmaps.geocode(location1)[0]["geometry"]["location"]
        loc2_coords = gmaps.geocode(location2)[0]["geometry"]["location"]

        directions_result = gmaps.directions(
            origin=loc1_coords,
            destination=loc2_coords,
            mode="driving",  # Other options: 'walking', 'bicycling', 'transit'
            optimize_waypoints=True,
        )

        route = Route.objects.create(
            start_location=location1,
            end_location=location2,
            waypoints=[location1, location2],  # Add more waypoints as needed
            optimized_route=directions_result,
        )

        return render(
            request,
            "routing/output.html",
            {
                "loc1_coords": loc1_coords,
                "loc2_coords": loc2_coords,
                "directions": directions_result,
            },
        )
    return render(request, "routing/input.html")
