# Sam Walters
# Lab 1, source code
# This program displays one my favorite quotes from the movie AIRPLANE! by the Zucker Brothers and Jim Abraham
# When run, it will print the quote surrounded by asterisks 

# the quote to be printed
quote = "'I am serious. And don\'t call me Shirley.' - Dr. Rumack, as played by Leslie Nielsen"

# empty string to dump some number of asterisks into
asterisks = ''
# count chars, put that many into @asterisks, +2 for border corners
for n in range(len(quote)+6):
    asterisks += '*'

# print top of the border
print(asterisks)
# print edges and quote
print('** ' + quote + ' **')
# print bottom
print(asterisks)
