import school_scores
list_of_scores = school_scores.get_all()

#print(list_of_scores)
print(list_of_scores[0])

#gets out state name and year
for row in list_of_scores:
    print(row["State"]["Name"], row["Year"])

#gets out total test takers
for row in list_of_scores:
    print(row["Total"]["Test-takers"])
