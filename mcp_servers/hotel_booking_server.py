from mcp.server.fastmcp import FastMCP
from booking import HotelBookingService

mcp= FastMCP("hotel-service")
service= HotelBookingService()

@mcp.tool()
def book_hotel(stay_location):
    """
    Book a hotel for stay_location.
    Args:
        stay_location (str): The location for booking the hotel.

    Returns:
        dict: A dictionary containing hotel details.
    """
    booking_id, hotel_id= service.book_hotel(stay_location)
    print(f"booking created: {booking_id} with hotel {hotel_id} ")
    return(f"""
             'booking_id' : {booking_id},
             'hotel_details' :  {service.bookings[booking_id]}
            """
           )

@mcp.tool()
def cancel_hotel(booking_id):
    """
    Cancel a hotel.
    Args:
        booking_id (str): The ID of booking to cancel.

    Returns:
        bool: True if cancellation was successful, False otherwise.
    """
    success= service.cancel_hotel(booking_id)

    if success:
        print(f"hotel with {booking_id} cancelled successfully")
    else:
        print(f"Failed to cancel booking {booking_id}")

    return success

@mcp.tool()
def get_hotel_details(booking_id):
    """
    Get hotel details from booking id.
    Args:
        booking_id (str): The ID of booking to cancel.

    Returns:
        dict: A dict containing hotel details or None if not found
    """
    hotel_details= service.get_hotel_details(booking_id)

    if hotel_details:
        print(f"Hotel details with {booking_id} : {hotel_details}")
    else:
        print(f"No hotel details found with {booking_id}")

    return hotel_details

if __name__ == "__main__":
    mcp.run(transport="stdio")
