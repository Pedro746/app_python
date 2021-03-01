

trc = '----------------------------------------------------'
ref = 'REFRATÁRIO'
apt_s = 'APTO A SERVIR'
apt_n = 'INAPTO A SERVIR'

print(trc)
print('VERIFICADOR DE RECRUTAS PARA EXÉCITO\n')
print(f'FORMUÁRIO\n{trc}')

while True:
    nome = input('DIGITE O NOME: ').upper()
    idade = input('DIGITE A IDADE: ').upper()
    sexo = input('SEXO [M]asculino [F]eminino: ').upper()
    exame = input('RESULTADO EXAME APTO [S]im [N]ao: ').upper()

    print(f'{trc}\nRESULTADO')

    if nome == '' or idade == '' or sexo == '' or exame == '':
        print('\nCAMPOS EM BRANCO NÃO SÃO ACEITOS\n')
    elif nome == ' ' or idade == ' ' or sexo == ' ' or exame == ' ':
        print('\nCAMPOS EM BRANCO NÃO SÃO ACEITOS\n')
    elif nome.isnumeric() or sexo.isnumeric() or exame.isnumeric():
        print('\nERROR DADOS INVÁLIDOS')
    elif not idade.isnumeric():
        print('\nERROR, EM IDADE DIGITE APENAS NÚMEROS INTEIROS')
    else:
        idade = int(idade)

        if idade < 18 and sexo == 'M' and exame == 'S':
            print(apt_n)
        elif idade == 18 and sexo == 'M' and exame == 'S':
            print(apt_s)
        elif idade > 18 and sexo == 'M' and exame == 'S':
            print(ref, apt_s)
        elif sexo != 'M':
            print(apt_n)

    parar = input('PARAR? [S]im [N]ao').upper()
    if parar == 'S':
        break


print(trc)


