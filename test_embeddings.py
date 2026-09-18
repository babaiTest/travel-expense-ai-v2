from app.infrastructure.azure_openai import embeddings


text = """
Employee: EMP1001
Travel ID: TRV1002
Document Type: Hotel Invoice

Hotel: CHICAGO DOWNTOWN HOTEL
Location: Chicago, United States

Stay:
Check-in: 2024-10-10
Check-out: 2024-10-13
Number of Nights: 3

Room Type: Executive King Room

Currency: USD
Room Charge: 900
Tax Amount: 135
Total Amount: 1035

Payment Status: PAID
Payment Method: Credit Card
"""


vector = embeddings.embed_query(text)


print("Embedding generated successfully.")

print("Vector type:", type(vector))

print("Vector dimension:", len(vector))

print("First 10 values:")
print(vector[:10])