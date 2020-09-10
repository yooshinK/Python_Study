class Family:
    def me(self):
        return 'I am parent'

class K_Family(Family):
    def me(self):
        super().me()
        return super().me() + ' and ' + 'I am Child'

test = K_Family()
print(test.me())
