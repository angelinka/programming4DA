#Program creates a tuple that stores the months of the year, from that tuple create
#another tuple with just the summer months (May, June, July), print out the
#summer months one at a time.
#Author: Angelina B

months = ("January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "july",
          "August",
          "September",
          "October",
          "November",
          "December"
          )
# Slicing months to get 3 summer months in another tuple
summerMonths = months[4:7]
for month in summerMonths:
    print (month)