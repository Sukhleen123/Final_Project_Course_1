# Ritti Bhogal
# Software Development Fundamentals Final Project
# This is the back-end programming for a zombie survival game

from flask import Flask, render_template
import random

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("main_page.html")

# Instructions page
@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

# First page of game: initial reaction
@app.route("/secondary_main")
def secondary_main():
    return render_template("secondary_main.html")

# Page after initial reaction
@app.route('/story_1')
def story_1():
    return render_template("story_1.html")

# Page if you chose to ignore knocks on door
@app.route("/s1_a")
def story_1_a():
    rand = random.randint(1, 10)
    # 50% chance of person leaving
    if 5 < rand <= 10:
        return render_template("story_1_A.html")
    # 50% chance of person breaking in
    elif 1 <= rand <= 5:
        return render_template("story_1_B.html")

# Page if the person who knocks leaves and you go outside
@app.route("/s1_a_a")
def story_1_a_a():
    rand = random.randint(1, 15)
    # 33% chance of encountering zombie
    if 10 < rand <= 15:
        return render_template("story_1_A_A.html")
    # 67% chance of travelling to supermarket safely
    elif 1 <= rand <= 10:
        return render_template("story_1_A_B.html")

# Page if the person who knocks leaves and you choose to stay home
@app.route("/s1_a_b")
def story_1_a_b():
    rand = random.randint(1, 15)
    # 33% of dying due to starvation
    if 10 < rand <= 15:
        return render_template("story_1_A_C.html")
    # 67% chance of living to the next week and hearing another knock
    elif 1 <= rand <= 10:
        return render_template("story_1_A_D.html")

# Page if you live until next week and open the door the 2nd time
@app.route("/s1_a_safe")
def story_1_a_safe():
    return render_template("story_1_D.html")

# Page if you live until next week and do not open door the 2nd time
@app.route("/s1_a_died")
def story_1_a_died():
    return render_template("story_1_A_C.html")

# Page if you reach the supermarket safely and hide there, leads to death
@app.route("/s1_a_b_a")
def story_1_a_b_a():
    return render_template("story_1_A_B_end.html")

# End page if you hide in the supermarket
@app.route("/s1_a_b_a_ending1")
def story_1_a_b_a_ending1():
    return render_template("story_1_A_B_ending1.html")

# End page if you try to fight the zombies
@app.route("/s1_a_b_a_ending2")
def story_1_a_b_a_ending2():
    return render_template("story_1_A_B_ending2.html")

# Page if you reach the supermarket safely and venture outside or are saved by authorities
@app.route('/s1_a_b_b')
def story_1_a_b_b():
    return render_template("saved.html")

# Page if you ignore knocks and try to exit house through another door
@app.route("/s1_a_died2")
def story_1_a_died2():
    return render_template("story_1_A_died.html")

# Page if you chose to answer the door
@app.route("/s1_b")
def story_1_b():
    rand = random.randint(1, 10)
    # 50% chance it's a zombie and you die
    if 5 < rand <= 10:
        return render_template("story_1_C.html")
    # 50% chance it's your neighbor
    elif 1 <= rand <= 5:
        return render_template("story_1_D.html")

# Page if you and neighbor decide to go to the tallest building
@app.route("/s1_b_a")
def story_1_b_a():
    rand = random.randint(1, 10)
    # 70% chance you run into a zombie and you die
    if 3 < rand <= 10:
        return render_template("story_1_A_A.html")
    # 30% chance you guys make it and are saved
    elif 1 <= rand <= 3:
        return render_template("saved.html")

# Page if you and neighbor decide to check if others are alive
@app.route("/s1_b_b")
def story_1_b_b():
    rand = random.randint(1, 10)
    # 70% you guys don't die on your trip
    if 3 < rand <= 10:
        return render_template("story_1_D_B.html")
    # 30% chance you run into a zombie and you die
    elif 1 <= rand <= 3:
        return render_template("story_1_A_A.html")

# Page if you decide not to check out the red light with your neighbor
@app.route("/s1_b_b_a")
def story_1_b_b_a():
    rand = random.randint(1, 10)
    # 70% you guys don't die on your way back
    if 3 < rand <= 10:
        return render_template("story_1_D_B_A.html")
    # 30% chance you run into a zombie and you die
    elif 1 <= rand <= 3:
        return render_template("story_1_A_A.html")


if __name__ == "__main__":
    app.run()
