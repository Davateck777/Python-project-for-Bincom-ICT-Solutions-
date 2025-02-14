# MY NAME: DAVE ADEMOLA
# ROLE: AUTHOR OF THIS CODE

import collections
import random
import psycopg2

# TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT 
colors_data = {
    "MONDAY": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "TUESDAY": ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
    "WEDNESDAY": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
    "THURSDAY": ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "FRIDAY": ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
}

# A single list containing all the colors
all_colors = []
for day_colors in colors_data.values():
    all_colors.extend(day_colors)

# Color of shirt That is the mean color
color_counts = collections.Counter(all_colors)
most_frequent_color = color_counts.most_common(1)[0][0]
print(f"1. The mean color is: {most_frequent_color}")

# Color  mostly worn throughout the week
print(f"2. The color mostly worn throughout the week is: {most_frequent_color}")

# The color is the median 
sorted_colors_by_frequency = color_counts.most_common()
median_index = len(sorted_colors_by_frequency) // 2
median_color = sorted_colors_by_frequency[median_index][0]
print(f"The median color is: {median_color}")


# Color Variance 
frequencies = list(color_counts.values())
mean_frequency = sum(frequencies) / len(frequencies)
variance = sum([(f - mean_frequency) ** 2 for f in frequencies]) / len(frequencies)
print(f"Variance of the color: {variance}")


# The probability that the color is red?
red_count = color_counts.get("RED", 0)
total_colors = len(all_colors)
probability_red = red_count / total_colors if total_colors > 0 else 0
print(f"Probability of choosing a red color: {probability_red:.4f}")


#  Saving the colours to postgresql database
def save_to_postgres(color_counts):
    try:
        # Replace with your actual database credentials
        conn = psycopg2.connect("dbname= dava_db user= dave password= dava123 host= http://localhost:3000")
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS color_frequencies (
                color VARCHAR(50) PRIMARY KEY,
                frequency INTEGER
            );
        """)

        for color, frequency in color_counts.items():
            cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s) ON CONFLICT (color) DO UPDATE SET frequency = %s", (color, frequency, frequency))

        conn.commit()
        print("6. Colors and frequencies saved to PostgreSQL database.")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if conn:
            cur.close()
            conn.close()

save_to_postgres(color_counts) 


# A Recursive searching algorithm to search a list of numbers for a number entered by a user.
def recursive_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return recursive_search(arr, low, mid - 1, x)
        else:
            return recursive_search(arr, mid + 1, high, x)
    else:
        return -1

# Testing the recursive search algorithm
sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
search_number = 23
result_index = recursive_search(sorted_numbers, 0, len(sorted_numbers)-1, search_number)
if result_index != -1:
    print(f" This {search_number} is present at index {result_index}")
else:
    print(f"7. This {search_number} is not present in array")


# A program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
def binary_to_base10():
    binary_string = ''.join(random.choice(['0', '1']) for _ in range(4))
    base10_number = int(binary_string, 2)
    print(f" Binary number: {binary_string}, Base 10 Version: {base10_number}")

binary_to_base10()

# A program to sum the first 50 fibonacci sequence.
def sum_my_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        total_sum = 1
        for _ in range(2, n + 1):
            c = a + b
            total_sum += c
            a = b
            b = c
        return total_sum

fibonacci_sum = sum_my_fibonacci(50)
print(f" Sum of the first 50 Fibonacci numbers: {fibonacci_sum}")