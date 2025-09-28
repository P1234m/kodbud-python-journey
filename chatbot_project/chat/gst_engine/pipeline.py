import csv
import os

def gst_chatbot_response(user_query):
    query = user_query.lower()
    csv_path = os.path.join(os.path.dirname(__file__), '..', '..', 'gst.csv')

    matches = []

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            subcat = row['Subcategory'].lower()
            category = row['Category']
            rate = row['GST Rate']
            notes = row['Notes']

            if query in subcat or query in category.lower():
                matches.append(f"- {row['Subcategory']} ({category}): {rate} — {notes}")

    if matches:
        return "Here’s what I found:\n" + "\n".join(matches[:5])
    else:
        return "Sorry, I couldn't find GST info for that. Try asking about a product or service like 'ice cream', 'electric vehicles', or 'restaurant services'."