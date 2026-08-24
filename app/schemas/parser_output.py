from typing import Literal, Optional

from pydantic import BaseModel, Field


class FlightTicketData(BaseModel):
    travelerName: Optional[str] = None
    departureCity: Optional[str] = None
    departureAirport: Optional[str] = None
    arrivalCity: Optional[str] = None
    arrivalAirport: Optional[str] = None
    flightNumber: Optional[str] = None
    travelDate: Optional[str] = None
    departureTime: Optional[str] = None
    arrivalDate: Optional[str] = None
    arrivalTime: Optional[str] = None
    seatNumber: Optional[str] = None
    travelClass: Optional[str] = None
    airline: Optional[str] = None


class FlightParseResult(BaseModel):
    documentType: Literal["FlightTicket", "Unknown"]
    data: FlightTicketData = Field(default_factory=FlightTicketData)


class HotelInvoiceData(BaseModel):
    hotelName: Optional[str] = None
    guestName: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    checkInDate: Optional[str] = None
    checkOutDate: Optional[str] = None
    numberOfNights: Optional[int] = None
    roomType: Optional[str] = None
    invoiceNumber: Optional[str] = None
    bookingReference: Optional[str] = None
    currency: Optional[str] = None
    roomCharge: Optional[float] = None
    taxAmount: Optional[float] = None
    totalAmount: Optional[float] = None
    paymentStatus: Optional[str] = None
    paymentMethod: Optional[str] = None


class HotelParseResult(BaseModel):
    documentType: Literal["HotelInvoice", "Unknown"]
    data: HotelInvoiceData = Field(default_factory=HotelInvoiceData)
