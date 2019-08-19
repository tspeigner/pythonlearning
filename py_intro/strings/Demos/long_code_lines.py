#EXAMPLE 1
phrase = ('On a scale of {0:d} to {1:d}, ' +
            'I give {2:s} a {3:d}.'.format(1, 5,
                                   'Monty Python', 6))
print(phrase)

#EXAMPLE 2
location = "ponds"
items = "swords"
beings = "masses"
adjective = "farcical"

quote = ("Listen, strange women lyin' in {} " +
             "distributin' {} is no basis for a system of " +
             "government. Supreme executive power derives from " +
             "a mandate from the {}, not from some {} " +
             "aquatic ceremony.").format(location, items,
                                         beings, adjective)

print(quote)