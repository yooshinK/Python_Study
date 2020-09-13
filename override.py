class Family:
    def me(self):
        return 'I am parent'

class K_Family(Family):
    def me(self):
        print(super().me()) # call parent class's me()
        return super().me() + ' and ' + 'I am Child'

test = K_Family()
print(test.me())

# Result
# I am parent
# I am parent and I am Child
