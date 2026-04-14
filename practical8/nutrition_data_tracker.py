class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
def calculate_daily_totals(food_list):
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0
    for item in food_list:
        total_calories = total_calories + item.calories
        total_protein = total_protein + item.protein
        total_carbohydrates = total_carbohydrates + item.carbohydrates
        total_fat = total_fat + item.fat
    print("Total calories:", total_calories)
    print("Total protein:", total_protein, "g")
    print("Total carbohydrates:", total_carbohydrates, "g")
    print("Total fat:", total_fat, "g")
    if total_calories > 2500:
        print("Warning: calorie intake is above 2500.")
    if total_fat > 90:
        print("Warning: fat intake is above 90 g.")
apple = food_item("Apple", 60, 0.3, 15, 0.5)
chicken = food_item("Chicken breast", 300, 35, 0, 8)
rice = food_item("Rice", 250, 5, 55, 1)
burger = food_item("Burger", 700, 25, 50, 35)
ice_cream = food_item("Ice cream", 350, 6, 40, 18)
foods_eaten = [apple, chicken, rice, burger, ice_cream]
calculate_daily_totals(foods_eaten)