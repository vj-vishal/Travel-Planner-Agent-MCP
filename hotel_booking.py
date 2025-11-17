from typing import Dict,Tuple, Optional
from uuid import uuid4
from datetime import datetime

class HotelBookingService:
    def __init__(self):
        self.bookings: Dict[str,dict] = {}
        self.hotels: Dict[str,dict]= {
            "hotel101": {"name": "Grand Palace Hotel", "phone": "555-1101", "city": "Mumbai", "price": 2500},
            "hotel102": {"name": "Seaside Resort", "phone": "555-1102", "city": "Goa", "price": 2000},
            "hotel103": {"name": "Mountain View Inn", "phone": "555-1103", "city": "Manali", "price": 2500},
            "hotel104": {"name": "Urban Stay Suites", "phone": "555-1104", "city": "Bangalore", "price": 3000},
            "hotel105": {"name": "Royal Heritage Lodge", "phone": "555-1105", "city": "Jaipur", "price": 2000}
        }
        self.hotel_availabity: Dict[str, bool]={
            "hotel101": True,
            "hotel102": True,
            "hotel103": True,
            "hotel104": True,
            "hotel105": True,
        }

    def book_hotel(self,stay_location: str) -> Tuple[str, dict]:
        """
        Book a hotel for stay_location
        Param: stay_location
        Return: booking_id, driver_id
        Raise: If hotel is not available
        """
        if not stay_location:
            raise ValueError("stay location not provided")

        available_hotel = None
        for hotel_id, hotel_info in self.hotels.items():
            if hotel_info["city"]==stay_location:
                for hotel_id_no, is_available in self.hotel_availabity.items():
                    if hotel_id_no==hotel_id and is_available:
                        available_hotel = hotel_id

        if not is_available:
            raise ValueError("Hotel not available at the moment")

        booking_id=str(uuid4())
        booking_details= {
            "location": stay_location,
            "hotel_id": available_hotel,
            "status": "booked",
            "booking_time": datetime.now()

        }

        self.hotel_availabity[available_hotel]= False
        self.bookings[booking_id]= booking_details


        return booking_id, available_hotel

    def cancel_hotel(self,booking_id: str) -> bool:
        """
        Cancel a booked hotel
        Param: booking_id
        Return: bool
        """
        if not booking_id in self.bookings:
            return False

        booking= self.bookings[booking_id]
        if booking["status"]!="booked":
            return False

        hotel_id= booking["hotel_id"]
        self.hotel_availabity[hotel_id]= True

        booking["status"] = "cancelled"
        booking["cancel_time"]= datetime.now()

        return True

    def get_hotel_details(self, booking_id:str) -> Optional[dict]:
        """
        Get hotel details for booking
        Param: booking_id
        Return: booked hotel details
        """
        if booking_id not in self.bookings:
            return None

        booking= self.bookings[booking_id]
        if booking["status"]!= "booked":
            return None

        hotel_id= booking["hotel_id"]
        hotel_info= self.hotels[hotel_id]

        return hotel_info

if __name__ == "__main__":
    service= HotelBookingService()

    try:
        # Book a cab
        booking_id, hotel_id = service.book_hotel("Mumbai")
        print(f"Booking created: {booking_id} with hotel {hotel_id}")

        # Get driver details
        hotel_details = service.get_hotel_details(booking_id)
        print(f"Driver details: {hotel_details}")

        # Cancel booking
        success = service.cancel_hotel(booking_id)
        print(f"Cancellation successful: {success}")

        # Try to get driver details after cancellation
        hotel_details = service.get_hotel_details(booking_id)
        print(f"Driver details after cancellation: {hotel_details}")

    except ValueError as e:
        print(f"Error: {e}")

