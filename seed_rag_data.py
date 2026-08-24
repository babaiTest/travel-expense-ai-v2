from datetime import datetime

from app.infrastructure.mongodb import database


# ============================================================
# Collections
# ============================================================

documents_collection = database["documents"]
expenses_collection = database["expenses"]
fraud_results_collection = database["fraud_results"]
travel_collection = database["travel"]
travel_history_collection = database["travel_history"]


# ============================================================
# Helper
# ============================================================

def insert_if_not_exists(
    collection,
    filter_query,
    document
):
    existing = collection.find_one(filter_query)

    if existing:
        print(
            f"Already exists in {collection.name}: "
            f"{filter_query}"
        )
        return

    collection.insert_one(document)

    print(
        f"Inserted into {collection.name}: "
        f"{filter_query}"
    )


# ============================================================
# TRAVEL 1
# EMP1001
# Paris -> New York
# ============================================================

insert_if_not_exists(
    travel_collection,
    {
        "travelId": "TRV1001"
    },
    {
        "travelId": "TRV1001",
        "userId": "EMP1001",
        "status": "COMPLETED",

        "documentSummary": {
            "totalDocuments": 3,
            "processedDocuments": 3,
            "validDocuments": 3,
            "invalidDocuments": 0
        },

        "timeline": [
            {
                "eventType": "Flight",
                "date": "2024-08-24",
                "time": "11:30",
                "title": "Flight",
                "description": "Paris -> Los Angeles"
            },
            {
                "eventType": "Hotel",
                "date": "2024-08-23",
                "time": "15:00",
                "title": "Hotel Stay",
                "description": "The Gotham Grand Luxury Hotel & Suites"
            }
        ],

        "fraudAnalysis": {
            "riskLevel": "LOW",
            "fraudScore": 5,
            "recommendation": "APPROVE"
        },

        "createdAt": datetime.utcnow(),
        "modifiedAt": datetime.utcnow()
    }
)


# ============================================================
# TRAVEL 2
# EMP1001
# New York -> Chicago
# ============================================================

insert_if_not_exists(
    travel_collection,
    {
        "travelId": "TRV1002"
    },
    {
        "travelId": "TRV1002",
        "userId": "EMP1001",
        "status": "COMPLETED",

        "documentSummary": {
            "totalDocuments": 3,
            "processedDocuments": 3,
            "validDocuments": 3,
            "invalidDocuments": 0
        },

        "timeline": [
            {
                "eventType": "Flight",
                "date": "2024-10-10",
                "time": "09:30",
                "title": "Flight",
                "description": "New York -> Chicago"
            },
            {
                "eventType": "Hotel",
                "date": "2024-10-10",
                "time": "14:00",
                "title": "Hotel Stay",
                "description": "Chicago Downtown Hotel"
            }
        ],

        "fraudAnalysis": {
            "riskLevel": "LOW",
            "fraudScore": 10,
            "recommendation": "APPROVE"
        },

        "createdAt": datetime.utcnow(),
        "modifiedAt": datetime.utcnow()
    }
)


# ============================================================
# TRAVEL 3
# EMP1002
# London -> New York
# ============================================================

insert_if_not_exists(
    travel_collection,
    {
        "travelId": "TRV2001"
    },
    {
        "travelId": "TRV2001",
        "userId": "EMP1002",
        "status": "COMPLETED",

        "documentSummary": {
            "totalDocuments": 4,
            "processedDocuments": 4,
            "validDocuments": 3,
            "invalidDocuments": 1
        },

        "timeline": [
            {
                "eventType": "Flight",
                "date": "2024-09-05",
                "time": "10:15",
                "title": "Flight",
                "description": "London -> New York"
            },
            {
                "eventType": "Hotel",
                "date": "2024-09-05",
                "time": "16:00",
                "title": "Hotel Stay",
                "description": "Manhattan Business Hotel"
            }
        ],

        "fraudAnalysis": {
            "riskLevel": "MEDIUM",
            "fraudScore": 55,
            "recommendation": "MANUAL_REVIEW"
        },

        "createdAt": datetime.utcnow(),
        "modifiedAt": datetime.utcnow()
    }
)


# ============================================================
# DOCUMENTS
# ============================================================

# ------------------------------------------------------------
# EMP1001 / TRV1002 - Flight
# ------------------------------------------------------------

insert_if_not_exists(
    documents_collection,
    {
        "documentId": "DOC-1002-FLIGHT"
    },
    {
        "documentId": "DOC-1002-FLIGHT",
        "userId": "EMP1001",
        "travelId": "TRV1002",

        "fileName": "NewYork_Chicago_Flight.pdf",

        "contentType": "application/pdf",

        "status": "PARSED",

        "ocrText": """
        UNITED AIRLINES
        BOARDING PASS

        Passenger: John Voyage
        From: New York (JFK)
        To: Chicago (ORD)

        Flight: UA204
        Date: 10 October 2024
        Departure: 09:30 AM

        Seat: 18A
        Class: Economy

        Total Paid: USD 425.00
        """,

        "parsedData": {
            "documentType": "FlightTicket",
            "data": {
                "travelerName": "John Voyage",
                "departureCity": "New York",
                "departureAirport": "JFK",
                "arrivalCity": "Chicago",
                "arrivalAirport": "ORD",
                "flightNumber": "UA204",
                "travelDate": "2024-10-10",
                "departureTime": "09:30",
                "arrivalDate": None,
                "arrivalTime": None,
                "seatNumber": "18A",
                "travelClass": "ECONOMY",
                "airline": "UNITED AIRLINES"
            }
        },

        "validation": {
            "isValid": True,
            "reason": "Flight matches travel itinerary."
        },

        "processing": {
            "ocrCompleted": True,
            "parserCompleted": True,
            "validationCompleted": True,
            "timelineCompleted": True,
            "fraudCompleted": True,
            "embeddingCompleted": False
        },

        "createdAt": datetime.utcnow(),
        "modifiedAt": datetime.utcnow()
    }
)


# ------------------------------------------------------------
# EMP1001 / TRV1002 - Hotel
# ------------------------------------------------------------

insert_if_not_exists(
    documents_collection,
    {
        "documentId": "DOC-1002-HOTEL"
    },
    {
        "documentId": "DOC-1002-HOTEL",
        "userId": "EMP1001",
        "travelId": "TRV1002",

        "fileName": "Chicago_Hotel.pdf",

        "contentType": "application/pdf",

        "status": "PARSED",

        "ocrText": """
        CHICAGO DOWNTOWN HOTEL

        HOTEL INVOICE

        Guest: John Voyage
        Invoice: CHI-2024-7712

        Check-in: 10 October 2024
        Check-out: 13 October 2024

        Room: Executive King Room
        Nights: 3

        Room Charges: USD 900.00
        Taxes: USD 135.00

        Total: USD 1035.00

        Payment: Credit Card
        Status: PAID
        """,

        "parsedData": {
            "documentType": "HotelInvoice",
            "data": {
                "hotelName": "CHICAGO DOWNTOWN HOTEL",
                "guestName": "John Voyage",
                "city": "Chicago",
                "country": "United States",
                "checkInDate": "2024-10-10",
                "checkOutDate": "2024-10-13",
                "numberOfNights": 3,
                "roomType": "Executive King Room",
                "invoiceNumber": "CHI-2024-7712",
                "bookingReference": None,
                "currency": "USD",
                "roomCharge": 900,
                "taxAmount": 135,
                "totalAmount": 1035,
                "paymentStatus": "PAID",
                "paymentMethod": "Credit Card"
            }
        },

        "validation": {
            "isValid": True,
            "reason": "Hotel stay dates and amount are consistent."
        },

        "processing": {
            "ocrCompleted": True,
            "parserCompleted": True,
            "validationCompleted": True,
            "timelineCompleted": True,
            "fraudCompleted": True,
            "embeddingCompleted": False
        },

        "createdAt": datetime.utcnow(),
        "modifiedAt": datetime.utcnow()
    }
)


# ------------------------------------------------------------
# EMP1002 / TRV2001 - Hotel
# ------------------------------------------------------------

insert_if_not_exists(
    documents_collection,
    {
        "documentId": "DOC-2001-HOTEL"
    },
    {
        "documentId": "DOC-2001-HOTEL",
        "userId": "EMP1002",
        "travelId": "TRV2001",

        "fileName": "Manhattan_Hotel.pdf",

        "contentType": "application/pdf",

        "status": "PARSED",

        "ocrText": """
        MANHATTAN BUSINESS HOTEL

        HOTEL INVOICE

        Guest: Michael Smith
        Invoice: MAN-2024-8821

        Check-in: 5 September 2024
        Check-out: 9 September 2024

        Room: Business Deluxe
        Nights: 4

        Accommodation: USD 1600.00
        Taxes: USD 240.00

        Total: USD 1840.00

        Payment: Credit Card
        Status: PAID
        """,

        "parsedData": {
            "documentType": "HotelInvoice",
            "data": {
                "hotelName": "MANHATTAN BUSINESS HOTEL",
                "guestName": "Michael Smith",
                "city": "New York",
                "country": "United States",
                "checkInDate": "2024-09-05",
                "checkOutDate": "2024-09-09",
                "numberOfNights": 4,
                "roomType": "Business Deluxe",
                "invoiceNumber": "MAN-2024-8821",
                "bookingReference": "MBH-77219",
                "currency": "USD",
                "roomCharge": 1600,
                "taxAmount": 240,
                "totalAmount": 1840,
                "paymentStatus": "PAID",
                "paymentMethod": "Credit Card"
            }
        },

        "validation": {
            "isValid": True,
            "reason": "Hotel document is structurally valid."
        },

        "processing": {
            "ocrCompleted": True,
            "parserCompleted": True,
            "validationCompleted": True,
            "timelineCompleted": True,
            "fraudCompleted": True,
            "embeddingCompleted": False
        },

        "createdAt": datetime.utcnow(),
        "modifiedAt": datetime.utcnow()
    }
)


# ============================================================
# EXPENSES
# ============================================================

# EMP1001 / TRV1002

insert_if_not_exists(
    expenses_collection,
    {
        "expenseId": "EXP-1002-001"
    },
    {
        "expenseId": "EXP-1002-001",
        "userId": "EMP1001",
        "travelId": "TRV1002",

        "expenseType": "Flight",

        "description": "New York to Chicago flight",

        "expenseDate": "2024-10-10",

        "amount": 425.00,
        "currency": "USD",

        "documentId": "DOC-1002-FLIGHT",

        "status": "VALIDATED"
    }
)


insert_if_not_exists(
    expenses_collection,
    {
        "expenseId": "EXP-1002-002"
    },
    {
        "expenseId": "EXP-1002-002",
        "userId": "EMP1001",
        "travelId": "TRV1002",

        "expenseType": "Hotel",

        "description": "Chicago hotel stay",

        "expenseDate": "2024-10-10",

        "amount": 1035.00,
        "currency": "USD",

        "documentId": "DOC-1002-HOTEL",

        "status": "VALIDATED"
    }
)


# EMP1002 / TRV2001

insert_if_not_exists(
    expenses_collection,
    {
        "expenseId": "EXP-2001-001"
    },
    {
        "expenseId": "EXP-2001-001",
        "userId": "EMP1002",
        "travelId": "TRV2001",

        "expenseType": "Hotel",

        "description": "Manhattan hotel accommodation",

        "expenseDate": "2024-09-05",

        "amount": 1840.00,
        "currency": "USD",

        "documentId": "DOC-2001-HOTEL",

        "status": "VALIDATED"
    }
)


# ============================================================
# FRAUD RESULTS
# ============================================================

insert_if_not_exists(
    fraud_results_collection,
    {
        "travelId": "TRV1001"
    },
    {
        "travelId": "TRV1001",
        "userId": "EMP1001",

        "riskLevel": "LOW",
        "fraudScore": 5,
        "recommendation": "APPROVE",

        "summary": (
            "Travel documents and expenses are consistent "
            "with the employee itinerary."
        ),

        "observations": [
            "Flight expense matches the travel document.",
            "Hotel stay dates are consistent with the itinerary.",
            "No duplicate expenses detected.",
            "No unsupported expenses detected."
        ],

        "potentialIssues": [],

        "confidence": 0.95,

        "createdAt": datetime.utcnow()
    }
)


insert_if_not_exists(
    fraud_results_collection,
    {
        "travelId": "TRV1002"
    },
    {
        "travelId": "TRV1002",
        "userId": "EMP1001",

        "riskLevel": "LOW",
        "fraudScore": 10,
        "recommendation": "APPROVE",

        "summary": (
            "The New York to Chicago business trip is "
            "supported by flight and hotel documents."
        ),

        "observations": [
            "Flight expense matches the itinerary.",
            "Hotel dates match the trip.",
            "All submitted expenses have supporting documents."
        ],

        "potentialIssues": [],

        "confidence": 0.93,

        "createdAt": datetime.utcnow()
    }
)


insert_if_not_exists(
    fraud_results_collection,
    {
        "travelId": "TRV2001"
    },
    {
        "travelId": "TRV2001",
        "userId": "EMP1002",

        "riskLevel": "MEDIUM",
        "fraudScore": 55,
        "recommendation": "MANUAL_REVIEW",

        "summary": (
            "The travel claim contains a hotel expense "
            "requiring additional review."
        ),

        "observations": [
            "Hotel document is available.",
            "Hotel stay is within the reported travel period."
        ],

        "potentialIssues": [
            "Hotel expense amount is relatively high.",
            "Additional policy verification is recommended."
        ],

        "confidence": 0.82,

        "createdAt": datetime.utcnow()
    }
)


# ============================================================
# TRAVEL HISTORY
# ============================================================

insert_if_not_exists(
    travel_history_collection,
    {
        "travelId": "TRV1001",
        "eventType": "Flight"
    },
    {
        "travelId": "TRV1001",
        "userId": "EMP1001",
        "eventType": "Flight",
        "date": "2024-08-24",
        "from": "Paris",
        "to": "Los Angeles",
        "flightNumber": "AF006"
    }
)


insert_if_not_exists(
    travel_history_collection,
    {
        "travelId": "TRV1001",
        "eventType": "Hotel"
    },
    {
        "travelId": "TRV1001",
        "userId": "EMP1001",
        "eventType": "Hotel",
        "date": "2024-08-23",
        "hotel": "THE GOTHAM GRAND LUXURY HOTEL & SUITES",
        "city": "New York",
        "checkInDate": "2024-08-23",
        "checkOutDate": "2024-09-20"
    }
)


insert_if_not_exists(
    travel_history_collection,
    {
        "travelId": "TRV1002",
        "eventType": "Flight"
    },
    {
        "travelId": "TRV1002",
        "userId": "EMP1001",
        "eventType": "Flight",
        "date": "2024-10-10",
        "from": "New York",
        "to": "Chicago",
        "flightNumber": "UA204"
    }
)


insert_if_not_exists(
    travel_history_collection,
    {
        "travelId": "TRV1002",
        "eventType": "Hotel"
    },
    {
        "travelId": "TRV1002",
        "userId": "EMP1001",
        "eventType": "Hotel",
        "date": "2024-10-10",
        "hotel": "CHICAGO DOWNTOWN HOTEL",
        "city": "Chicago",
        "checkInDate": "2024-10-10",
        "checkOutDate": "2024-10-13"
    }
)


insert_if_not_exists(
    travel_history_collection,
    {
        "travelId": "TRV2001",
        "eventType": "Flight"
    },
    {
        "travelId": "TRV2001",
        "userId": "EMP1002",
        "eventType": "Flight",
        "date": "2024-09-05",
        "from": "London",
        "to": "New York",
        "flightNumber": "BA117"
    }
)


insert_if_not_exists(
    travel_history_collection,
    {
        "travelId": "TRV2001",
        "eventType": "Hotel"
    },
    {
        "travelId": "TRV2001",
        "userId": "EMP1002",
        "eventType": "Hotel",
        "date": "2024-09-05",
        "hotel": "MANHATTAN BUSINESS HOTEL",
        "city": "New York",
        "checkInDate": "2024-09-05",
        "checkOutDate": "2024-09-09"
    }
)


print()
print("======================================")
print("RAG dummy data seeding completed.")
print("======================================")