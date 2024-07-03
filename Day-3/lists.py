

fave_website = [
    "https://www.youtube.com/",
    "https://www.codewars.com/",
    "https://orteil.dashnet.org/cookieclicker/"
]

fave_games = [
    "Final Fantasy",
    "SaGa Series",
    "Tekken",
    "Broken Sword"
]

fave_website.append("https://github.com/")
fave_website.append("https://open.spotify.com/")

print(fave_website)
fave_website.pop()
print(fave_website)

# .remove()
# The remove() method removes the first occurrence of the element with the specified value.
# This changes the list.
fave_website.remove("https://www.codewars.com/")
print(fave_website)

# .reverse()
# The reverse() method reverses the sorting order of the elements
# this does changes the list
fave_website.reverse()
print(f"reverse: {fave_website}")

# .sort()
# The sort() method sorts the list ascending by default. (Alphabetically)
# this changes the list
# fave_website.sort()
print(fave_website)


# .count()
# The count() method returns the number of elements with the specified value.
# .count doesnt change the list but returns an integer
fave_website.append("https://orteil.dashnet.org/cookieclicker/")
print(fave_website)
print(fave_website.count("https://orteil.dashnet.org/cookieclicker/"))

