#while, a condition, a colon:

count = 1

while count <= 5:
    print("Iteration", count)
    count += 1

#break

numbers = [1, 2, 3, 4, 5, 6]
target = 4

for number in numbers:
    print(number)
    if number == target:
        print('Target found!' ,number)
        break;

#continue
scores = [68, 42, 57, 78, 35, 62, 50, 92]
total = 0
count = 0

for score in scores:
    if score < 50:
        continue
    total += score
    count += 1

average = total / count if count > 0 else 0

print("Average score for scores above 50: ", average)
