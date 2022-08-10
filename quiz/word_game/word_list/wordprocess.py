file = input('Enter File Name: ')

# add text to process here  
text = """abolish	escalate	influence
accomplish	establish	investigate
accurate	evaluate	navigate
announce	evidence	opposed
anxious	exhaust	ordinary
approach	expansion	passage
approval	expectation	persuade
approximate	explain	primary
argument	express	recently
avoid	extend	reference
briskly	familiar	review
cease	frequent	revolt
claim	gigantic	scarce
conclude	gist	significant
conflict	glare	source
consistent	harsh	summarize
context	heroic	superior
convince	hesitate	tension
culture	hilarious	tolerate
decade	historic	tremble
dissatisfied	horizontal	unexpected
dominate	hostile	unfamiliar
drowsy	huddle	vertical
edible	identify	effortless
illegible	equivalent	immigrate
 """

text = text.replace('\t','\n')

with open(file, 'w',encoding='utf-8') as f:
     f.write(text)
