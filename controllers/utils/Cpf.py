# Code from Adriano Margarin link: https://github.com/adrianomargarin/cpf_cnpj/blob/master/cpf_cnpj/cpf_cnpj.py

class Cpf(object):

    def __init__(self, cpf):
        self.cpf = cpf

    def validate_size(self):
        cpf = self.cleaning()
        if len(cpf) > 11 or len(cpf) < 11:
            return False
        return True

    def validate(self):
        if self.validate_size():
            digit_1 = 0
            digit_2 = 0
            i = 0
            cpf = self.cleaning()
            while i < 10:
                digit_1 = ((digit_1 + (int(cpf[i]) * (11-i-1))) % 11
                    if i < 9 else digit_1)
                digit_2 = (digit_2 + (int(cpf[i]) * (11-i))) % 11
                i += 1
            return ((int(cpf[9]) == (11 - digit_1 if digit_1 > 1 else 0)) and
                    (int(cpf[10]) == (11 - digit_2 if digit_2 > 1 else 0)))
        return False

    def cleaning(self):
        return self.cpf.replace('.', '').replace('-', '')

    def format(self):
        return '%s.%s.%s-%s' % (
            self.cpf[0:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11])

