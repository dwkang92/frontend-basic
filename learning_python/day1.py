# 1. Function - print

print("Hello World!")
print("welcome", 21, "year-old", "boy")

# 2. Seperator
# welcome|21|year-old|boy
# welcome////21////year-old////boy
print("welcome", 21, "year-old", "boy", sep="|")
print("welcome", 21, "year-old", "boy", sep="////")

# Same Result!
print("Journey", "\n", "Kyle", "\n", "Canada!")
print("Journey", "Kyle", "Canada!", sep="\n")