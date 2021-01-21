The list inside a dictionnary in the request.post come from googleform odd behaviour to duplicate fields rather than to concatenate them with URL enconding for multiple choice questions.
ex: entry.12345678=box+1&entry.12345678=box+2 rather than entry.12345678=box+1&box+2

Since dictionnaries key are unique, it only take the last one sended which overwrite the previous ones.

# inputs

googledocs default one
- text
- linear
- choiceGrid
- checkboxGrid
- shortAnswer
- paragraph
- multipleChoice
- checkboxes
- dropdown

customs:
- number: return a number between a provided interval
- yesOrNo: return yes or no
- email


# Todo

- [ ] File upload
- [ ] Decimals
- [ ] covtests

/!\ attention triple ''' pour retour ligne

# pas de retour à la lignje pour les paragraphes
#
#
# pas de autre
