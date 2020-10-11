s = "That I ever did see. Dusty as the handle on the door"

sub = "Dusty1"
index = s.find(sub)
print('inx of ' + sub + ": " + str(index))

sub = "Dusty"
index = s.find(sub)
print('inx of ' + sub + ": " + str(index))

if (sub in s):
    print('Dusty found')
