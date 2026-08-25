from typing import List, Dict


class RAGDocumentBuilder:

    @staticmethod
    def build_from_document(document: dict) -> Dict:

        parsed_data = document.get(
            "parsedData",
            {}
        )

        data = parsed_data.get(
            "data",
            {}
        )

        document_type = parsed_data.get(
            "documentType"
        )

        user_id = document.get(
            "userId"
        )

        travel_id = document.get(
            "travelId"
        )

        document_id = document.get(
            "documentId"
        )

        # --------------------------------------------------
        # Flight
        # --------------------------------------------------

        if document_type == "FlightTicket":

            content = f"""
Employee: {user_id}
Travel ID: {travel_id}
Document Type: Flight Ticket

Traveler: {data.get("travelerName")}
Airline: {data.get("airline")}
Flight Number: {data.get("flightNumber")}

Departure:
City: {data.get("departureCity")}
Airport: {data.get("departureAirport")}
Date: {data.get("travelDate")}
Time: {data.get("departureTime")}

Arrival:
City: {data.get("arrivalCity")}
Airport: {data.get("arrivalAirport")}
Date: {data.get("arrivalDate")}
Time: {data.get("arrivalTime")}

Seat: {data.get("seatNumber")}
Travel Class: {data.get("travelClass")}
""".strip()

        # --------------------------------------------------
        # Hotel
        # --------------------------------------------------

        elif document_type == "HotelInvoice":

            content = f"""
Employee: {user_id}
Travel ID: {travel_id}
Document Type: Hotel Invoice

Hotel: {data.get("hotelName")}
Guest: {data.get("guestName")}

Location:
City: {data.get("city")}
Country: {data.get("country")}

Stay:
Check-in: {data.get("checkInDate")}
Check-out: {data.get("checkOutDate")}
Number of Nights: {data.get("numberOfNights")}

Room Type: {data.get("roomType")}

Invoice Number: {data.get("invoiceNumber")}
Booking Reference: {data.get("bookingReference")}

Currency: {data.get("currency")}
Room Charge: {data.get("roomCharge")}
Tax Amount: {data.get("taxAmount")}
Total Amount: {data.get("totalAmount")}

Payment Status: {data.get("paymentStatus")}
Payment Method: {data.get("paymentMethod")}
""".strip()

        # --------------------------------------------------
        # Unknown document type
        # --------------------------------------------------

        else:

            content = f"""
Employee: {user_id}
Travel ID: {travel_id}
Document Type: {document_type}

OCR Content:

{document.get("ocrText", "")}
""".strip()

        # --------------------------------------------------
        # Metadata
        # --------------------------------------------------

        metadata = {
            "userId": user_id,
            "travelId": travel_id,
            "documentId": document_id,
            "documentType": document_type,
            "fileName": document.get("fileName")
        }

        return {
            "content": content,
            "metadata": metadata
        }

    # ------------------------------------------------------
    # Build RAG documents from MongoDB documents
    # ------------------------------------------------------

    @staticmethod
    def build_from_documents(
        documents: List[dict]
    ) -> List[Dict]:

        rag_documents = []

        for document in documents:

            rag_document = (
                RAGDocumentBuilder.build_from_document(
                    document
                )
            )

            rag_documents.append(
                rag_document
            )

        return rag_documents