# importing the module
import wikipedia

# finding result for the search
# sentences = 2 refers to numbers of line
result = wikipedia.summary("Rajeev Gandhi",sentences = 2)

# printing the result
print({"content":result})