# Disable every delay and only fill one survey, testing purpose
debug = True

# Form url (the one with docs.google.com/forms/.../formResponse), not the shorten one
url = 'https://docs.google.com/forms/d/e/1FAIpQLSckRtlfO2gYxz86viUovA1umT7BLWYiRTI5lSM4mf0b0rtvTw/formResponse'
#url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSf3mVlq3JWm_wQW77lGFlN_lbYai4mUZTs5ZIgHtXTNJQ71ZQ/formResponse'

# Number of fake survey to submit
loopMax = 200

''' Range of seconds to answer the survey
will choose randomly between the 2 values
Otherwise it will look like the survey was done in 0 sec, so not so legit '''
answerMin = 80
answerMax = 150

'''Range of minutes between each survey filling
will choose randomly between the 2 values
Otherwise it will look like all the survey answers where done at the same time, not so legit also '''
surveyMin = 1
surveyMax = 2
