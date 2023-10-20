import random
import streamlit as st
import matplotlib.pyplot as plt

def monty_hall(player_choice, switch_doors):
    # initialize doors
    doors = [0, 1, 2]
    # randomly place prize behind one door
    prize = random.choice(doors)
    # host opens a non-selected door without the prize
    non_prize_doors = [door for door in doors if door != prize and door != player_choice]
    host_choice = random.choice(non_prize_doors)
    # switch doors if requested
    if switch_doors:
        player_choice = [door for door in doors if door != player_choice and door != host_choice][0]
    # determine win or lose
    if player_choice == prize:
        return True
    else:
        return False

# create streamlit app
st.title("Monty Hall Problem Simulation")
st.write("The Monty Hall problem is a probability puzzle that is named after the host of the game show let's make a deal, Monty Hall. In the game show, there are three doors, behind one of which is a valuable prize (such as a car) and behind the other two doors are less valuable prizes (such as goats). The contestant chooses one of the three doors, but before revealing what is behind the chosen door, the host (Monty Hall) opens one of the other two doors to reveal a less valuable prize. The contestant is then given the option to switch their choice to the remaining unopened door or stay with their initial choice.")
st.write("The question that arises is whether it is better for the contestant to switch their choice or stay with their initial choice. Intuitively, it may seem that the chances of winning are the same regardless of whether the contestant switches or not, but in fact, the probability of winning is higher if the contestant switches their choice. This can be explained through probability theory, where it is shown that if the contestant switches, they have a 2/3 chance of winning, whereas if they stick with their initial choice, they only have a 1/3 chance of winning. ")
name = "Gaurav Ojha"
email = "ojhagaurav36@gmail.com"

st.write("Authored by:", name)
st.write("I've developed this for a class assignment. Feel free to reach out to me at", email, "for any questions or feedback.")

# ask user to choose a door
door_choice = st.radio("Choose a door:", [0, 1, 2])

# simulate Monty Hall problem to show host's choice
doors = [0, 1, 2]
prize = random.choice(doors)
non_prize_doors = [door for door in doors if door != prize and door != door_choice]
host_choice = random.choice(non_prize_doors)

# display host's choice
st.write(f"The host opens door number {host_choice}")

# ask user if they want to switch doors
switch_doors = st.checkbox("Switch doors?")

# simulate Monty Hall problem a million times
wins = 0
losses = 0
for i in range(1000000):
    if monty_hall(door_choice, switch_doors):
        wins += 1
    else:
        losses += 1

# display results
total_games = wins + losses
win_percentage = round((wins / total_games) * 100, 2)
loss_percentage = round((losses / total_games) * 100, 2)

st.write("Results:")
st.write(f"Wins: {wins} ({win_percentage}%)")
st.write(f"Losses: {losses} ({loss_percentage}%)")

# plot results
fig, ax = plt.subplots()
ax.bar(['Staying with original choice', 'Switching doors'], [loss_percentage, win_percentage], 
       color=['red', 'green'])
ax.set_ylabel('Percentage')
ax.set_title('Monty Hall Problem Results')
st.pyplot(fig)
