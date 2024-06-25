
# # LAB_PIP


# ## using what you've learned , create a new project to print Text Art in the terminal :
# - Create a virtual environment & activate it
# - Use ART package to print Text Art.
# - Print the phrase "BELIEVE AND ACHEIVE" designed with font `block`.
# - print the phrase "HELLO" designed with font `sub-zero`.


# ## Bonus
# - Come up with different phrases with different art and decoration
# - Use colorama to color the text in the terminal.


from art import *



phrase1 = text2art("BELIEVE AND ACHEIVE", font= 'block', chr_ignore= True)
print(phrase1)

phrase2 = text2art("HELLO", font= 'sub-zero')#, chr_ignore= True)
print(phrase2)