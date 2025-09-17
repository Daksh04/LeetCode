# 2353. Design a Food Rating System

# Design a food rating system that can do the following:

# Modify the rating of a food item listed in the system.
# Return the highest-rated food item for a type of cuisine in the system.
# Implement the FoodRatings class:

# FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
# foods[i] is the name of the ith food,
# cuisines[i] is the type of cuisine of the ith food, and
# ratings[i] is the initial rating of the ith food.
# void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
# String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
# Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 

# Example 1:

# Input
# ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
# [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
# Output
# [null, "kimchi", "ramen", null, "sushi", null, "ramen"]

# Explanation
# FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
# foodRatings.highestRated("korean"); // return "kimchi"
#                                     // "kimchi" is the highest rated korean food with a rating of 9.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // "ramen" is the highest rated japanese food with a rating of 14.
# foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "sushi"
#                                       // "sushi" is the highest rated japanese food with a rating of 16.
# foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // Both "sushi" and "ramen" have a rating of 16.
#                                       // However, "ramen" is lexicographically smaller than "sushi".
 

# Constraints:

# 1 <= n <= 2 * 104
# n == foods.length == cuisines.length == ratings.length
# 1 <= foods[i].length, cuisines[i].length <= 10
# foods[i], cuisines[i] consist of lowercase English letters.
# 1 <= ratings[i] <= 108
# All the strings in foods are distinct.
# food will be the name of a food item in the system across all calls to changeRating.
# cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
# At most 2 * 104 calls in total will be made to changeRating and highestRated.

# Code: Python3 (O(n))
import heapq
from collections import defaultdict
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.rating = ratings

    def changeRating(self, food: str, newRating: int) -> None:
        rating_index = 0
        for item in self.foods:
            if item == food:
                self.rating[rating_index]=newRating
                break
            rating_index+=1
        return None

    def lexicographical_check(self, item1: str, item2: str) -> str:
        if item1 < item2:
            return item1
        elif item1 > item2:
            return item2
        else:
            return item1

    def highestRated(self, cuisine: str) -> str:
        max_rating = 0
        max_rated_food = ""
        index=0
        for item in self.foods:
            if(self.rating[index] >= max_rating and self.cuisines[index]==cuisine):
                if(max_rating==self.rating[index]):
                    max_rated_food=self.lexicographical_check(item,max_rated_food)
                else:
                    max_rated_food = item
                max_rating=self.rating[index]
            index+=1
        return max_rated_food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine) Time limit exceeded

# Code Python3: O(log(n)) Optimized using Heap - This class overrides previous one
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            heapq.heappush(self.cuisine_to_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        # Push new entry into heap
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]
        # Pop stale entries
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)
