# Sample data for users and their movie ratings
user_ratings = {
    'User1': {'Movie1': 5, 'Movie2': 4, 'Movie3': 2, 'Movie4': 1},
    'User2': {'Movie1': 3, 'Movie2': 5, 'Movie3': 4, 'Movie5': 2},
    'User3': {'Movie2': 2, 'Movie4': 4, 'Movie5': 5},
    'User4': {'Movie1': 4, 'Movie3': 3, 'Movie4': 2, 'Movie5': 1},
}

# Function to calculate similarity between two users based on their ratings
def calculate_similarity(user1, user2):
    common_movies = set(user1.keys()) & set(user2.keys())
    
    if not common_movies:
        return 0  # No common movies
    
    numerator = sum(user1[movie] * user2[movie] for movie in common_movies)
    
    sum_of_squares_user1 = sum(user1[movie] ** 2 for movie in user1)
    sum_of_squares_user2 = sum(user2[movie] ** 2 for movie in user2)
    
    denominator = (sum_of_squares_user1 ** 0.5) * (sum_of_squares_user2 ** 0.5)
    
    if denominator == 0:
        return 0  # Avoid division by zero
    
    similarity = numerator / denominator
    return similarity

# Function to recommend movies to a user
def recommend_movies(user_id, users, ratings):
    user = users[user_id]
    recommendations = {}
    
    for other_user in users:
        if other_user != user_id:
            similarity = calculate_similarity(user, users[other_user])
            
            if similarity > 0:
                for movie in users[other_user]:
                    if movie not in user and users[other_user][movie] > 3:
                        if movie not in recommendations:
                            recommendations[movie] = 0
                        recommendations[movie] += similarity * users[other_user][movie]
    
    recommendations = [(movie, score) for movie, score in recommendations.items()]
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations

# Example: Recommend movies for 'User1'
user_to_recommend = 'User1'
recommended_movies = recommend_movies(user_to_recommend, user_ratings, user_ratings)
print(f"Top recommended movies for '{user_to_recommend}':")
for movie, score in recommended_movies[:5]:
    print(f"{movie}: {score}")