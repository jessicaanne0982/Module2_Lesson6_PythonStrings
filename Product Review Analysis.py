# Task 1:

customer_reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
keywords = ["good", "excellent", "bad", "poor", "average"]
         

for review in customer_reviews:
    for keyword in keywords:
        if keyword in review.lower():
            print(review.replace(keyword, keyword.upper()))
 

# # Task # 2: Sentiment Tally

customer_review = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def find_positive():
    positive_count = 0
    for review in customer_review:
        for word in positive_words:
            if word in review.lower():
                positive_count+=1
    return positive_count

def find_negative():
    negative_count = 0
    for review in customer_review:
        for word in negative_words:
            if word in review.lower():
                negative_count+=1
    return negative_count
 
for review in customer_review:
    for word in positive_words:
        count_positive = find_positive()  

for word in negative_words:
        count_negative = find_negative()

print(f"There were {count_positive} positive words and {count_negative} negative words found in the reviews.")


# Task 3: Review Summary

customer_reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

for review in customer_reviews:
    find_space = review[:30].rfind(" ")
    print(review[:find_space] + "...")
