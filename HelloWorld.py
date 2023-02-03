class DenislavMladenov:
    def __init__(self):
        self.email = 'denislav.mladenov***@gmail.com'
        self.phone = (+359, 894, 99, '**', 22)
        self.city = {'Pernik', 'Sofia'}
        self.brain = ['python', 'cloud', 'databases']

    def __contains__(self, skill):
        if skill not in self.brain:
            self.brain += [skill]
        return True


t = DenislavMladenov()
print(t.email)
print(t.phone)
print(t.city)
print(t.brain)
print()