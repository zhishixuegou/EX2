participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90


# Make sure the lists have the same number of elements

print(f"Length participants: {len(participants)}, Length scores: {len(scores)}")

# First, display all the current participants with their scores. Use zip()

print("\n--- Current participants and scores ---")
for name, score in zip(participants, scores):
    print(f"{name}: {score}")

# Write the logic to accept a new participant's name and their score. 
# While entering, also check if they are already in the list of participants. 
# If the participant is already registered, display a message and do not add them to the list.
# If the name is empty, then print an error saying that the name cannot be empty, and don't add them to the list.
# If the score is not a number, then print an error saying that the score must be a number, and don't add them to the list.
# If the score is less than 0 or greater than 100, then print an error saying that the score must be between 0 and 100, and don't add them to the list.
# Otherwise, add the participant and their score to the lists and display a message saying that they have been successfully registered.

print("\n--- Add new participant ---")
new_name = input("Enter new participant name: ").strip()
if new_name == "":
    print("Error: the name cannot be empty.")
else:
    if new_name in participants:
        print(f"Message: {new_name} is already registered. Do not add.")
    else:
        score_input = input("Enter participant score: ").strip()
        try:
            new_score = int(score_input)
        except ValueError:
            print("Error: the score must be a number.")
        else:
            if new_score < 0 or new_score > 100:
                print("Error: the score must be between 0 and 100.")
            else:
                participants.append(new_name)
                scores.append(new_score)
                print(f"Message: {new_name} has been successfully registered.")


# Write the logic to search for a specific participant.
# If the participant is found, display their name, score, and whether they are qualified or not.
# If the score is more than the distinction score, display that they have a DISTINCTION.
# If the score is more than the qualification score, display that they are QUALIFIED.
# Otherwise, display that they are NOT QUALIFIED.
# If the participant is not found, display a message saying that they are not found.

print("\n--- Search participant ---")
search_name = input("Enter participant name to search: ").strip()
if search_name in participants:
    index = participants.index(search_name)
    found_score = scores[index]
    print(f"Name: {search_name}, Score: {found_score}")
    if found_score > distinction_score:
        print("DISTINCTION")
    elif found_score > qualification_score:
        print("QUALIFIED")
    else:
        print("NOT QUALIFIED")
else:
    print(f"Message: {search_name} are not found.")


# Display every participant's name, score, and whether they are qualified or not. 

print("\n--- All participants qualification status ---")
for name, s in zip(participants, scores):
    if s > distinction_score:
        status = "DISTINCTION"
    elif s > qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    print(f"Name: {name}, Score: {s}, Status: {status}")





# Write the logic to find if there's even one participant that has a distinction, and if all the participants have passed (i.e., scored 50 or more).
print("\n--- Check distinction and all pass ---")
has_distinction = any(s > distinction_score for s in scores)
all_pass_50 = all(s >= 50 for s in scores)
print(f"At least one participant has distinction: {has_distinction}")
print(f"All participants scored 50 or more: {all_pass_50}")

# Write the logic to update a participant's score.
# Ensure that the participant exists in the list before updating their score. 
# Also ensure that the new score is a valid number between 0 and 100.

print("\n--- Update participant score ---")
update_name = input("Enter participant name to update score: ").strip()
if update_name not in participants:
    print(f"Error: {update_name} does not exist, cannot update.")
else:
    new_score_input = input("Enter new score: ").strip()
    try:
        updated_score = int(new_score_input)
    except ValueError:
        print("Error: the score must be a number.")
    else:
        if updated_score < 0 or updated_score > 100:
            print("Error: the score must be between 0 and 100.")
        else:
            pos = participants.index(update_name)
            scores[pos] = updated_score
            print(f"Successfully updated {update_name}'s score to {updated_score}")


# Write the logic to withdraw (remove) a participant from the list.
# Ensure that the score for that specific participant is also removed from the scores list
print("\n--- Withdraw participant ---")
withdraw_name = input("Enter participant name to withdraw: ").strip()
if withdraw_name not in participants:
    print(f"Error: {withdraw_name} not found, cannot withdraw.")
else:
    remove_pos = participants.index(withdraw_name)
    participants.pop(remove_pos)
    scores.pop(remove_pos)
    print(f"{withdraw_name} has been withdrawn from participant list.")



# Create and display a scoreboard where all the participants and their scores are displayed in descending order.
# Display their rank alongside the participant name and score

print("\n--- Scoreboard (descending with rank) ---")
paired_list = list(zip(participants, scores))
sorted_by_score = sorted(paired_list, key=lambda x: x[1], reverse=True)
for rank, (p_name, p_score) in enumerate(sorted_by_score, start=1):
    print(f"Rank {rank} | Name: {p_name} | Score: {p_score}")



# Calculate statistics: 
# Calculate what the highest score is, what lowest score is, what the average score is.
# Calculate how many participants have the highest score and the lowest score
# Calculate how many participants have distinctions, how many are qualified, and how many are not qualified

highest_score = max(scores)
lowest_score = min(scores)
avg_score = sum(scores) / len(scores)
count_highest = scores.count(highest_score)
count_lowest = scores.count(lowest_score)

count_distinction = 0
count_qualified = 0
count_not_qualified = 0
for s in scores:
    if s > distinction_score:
        count_distinction += 1
    elif s > qualification_score:
        count_qualified += 1
    else:
        count_not_qualified += 1


# Generate a final report that displays the participant name, their rank, their score, and their qualification (DISTINCTION, QUALIFIED, NOT QUALIFIED)
# Also the display all the statistics you calculated above

print("\n======== FINAL REPORT ========")
print(f"{'Rank':<5}{'Name':<22}{'Score':<8}{'Qualification'}")
print("-"*52)
for rank, (p_name, p_score) in enumerate(sorted_by_score, start=1):
    if p_score > distinction_score:
        q_status = "DISTINCTION"
    elif p_score > qualification_score:
        q_status = "QUALIFIED"
    else:
        q_status = "NOT QUALIFIED"
    print(f"{rank:<5}{p_name:<22}{p_score:<8}{q_status}")

print("\n----- Statistics -----")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Average score: {avg_score:.2f}")
print(f"Number with highest score: {count_highest}")
print(f"Number with lowest score: {count_lowest}")
print(f"Number with distinction: {count_distinction}")
print(f"Number qualified: {count_qualified}")
print(f"Number not qualified: {count_not_qualified}")
print("============================")