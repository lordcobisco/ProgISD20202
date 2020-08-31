resImagemF = 80
tipoCelularF = 0
faixaIluminacaoF = 300
brilhoF = 50
contrasteF = 50
angEspF = 45   # angulo espelho #
laserF = 0
planoFocalF = 1
lenteObjF = 100
antiCorposF = 1
calibraH1 = 'L'
calibraH2 = 'N'
calibraV1 = 'U'
calibraV2 = 'A'


print('Esse programa tem como objetivo receber dados para microscopia confocal de varredura à laser.')
print('Por favor, selecione os parâmetros que deseja alterar. ')

resImagem = int(input('Digite a resolução da imagem necessária. (0 ~ 100). '))
varBool1 = resImagem != resImagemF
print("Houve alteração na variável? " + str(varBool1))

tipoCelular = int(input('Digite o tipo celular necessário. (0 ~ 3).'))
varBool2 = tipoCelularF != tipoCelular
print("Houve alteração na variável? " + str(varBool2))

faixaIluminacao = int(input('Digite a faixa de iluminação necessária. (0 ~ 100) '))
varBool3 = faixaIluminacaoF != faixaIluminacao
print("Houve alteração na variável? " + str(varBool3))

brilho = int(input('Digite o brilho desejado. (0 ~ 100). Valor padrão = 50 '))
varBool4 = brilhoF != brilho
print("Houve alteração na variável? " + str(varBool4))

contraste = int(input('Digite o contraste desejado. (0 ~ 100). Valor padrão = 50 '))
varBool5 = contrasteF != contraste
print("Houve alteração na variável? " + str(varBool5))

angEsp = int(input('Digite o ângulo do espelho dicróico desejado. (0º ~ 180º). Valor padrão = 45º '))
varBool6 = angEspF != angEsp
print("Houve alteração na variável? " + str(varBool6))

laser = int(input('Digite o tipo de laser desejado. (0 ~ 3) '))
varBool7 = laserF != laser
print("Houve alteração na variável? " + str(varBool7))

planoFocal = int(input('Digite o plano focal desejado. (0 ~ 100). Valor padrão = 1 '))
varBool8 = planoFocalF != planoFocal
print("Houve alteração na variável? " + str(varBool8))

lenteObj = int(input('Digite a espessura da lente objetiva. (0 ~ 1000). Valor padrão = 100 '))
varBool9 = lenteObjF != lenteObj
print("Houve alteração na variável? " + str(varBool9))

antiCorpos = int(input('Digite os anticorpos secundários. (0 ~ 5) '))
varBool10 = antiCorposF != antiCorpos
print("Houve alteração na variável? " + str(varBool10))

print("Os parâmetros setados pelo usuário foram: ")
print('Resolução da imagem:', resImagem)
print('Tipo de célula:', tipoCelular)
print('Faixa de iluminação:', faixaIluminacao)
print('Brilho:', brilho)
print('Contraste:', contraste)
print('Ângulo do Espelho:', angEsp)
print('Tipo de laser:', laser)
print('Plano Focal:', planoFocal)
print('Lente Objetiva:', lenteObj)
print('Anticorpos:', antiCorpos)

print('Pressione "L" 10 vezes para calibração horizontal')

contador1 = str(input('Pressione L. '))
H = contador1 == calibraH1
print(str(H))
contador2 = str(input('Pressione L. '))
H2 = contador2 == calibraH1
print(str(H2))
contador3 = str(input('Pressione L. '))
H3 = contador3 == calibraH1
print(str(H3))
contador4 = str(input('Pressione L. '))
H4 = contador4 == calibraH1
print(str(H4))
contador5 = str(input('Pressione L. '))
H5 = contador5 == calibraH1
print(str(H5))
contador6 = str(input('Pressione L. '))
H6 = contador6 == calibraH1
print(str(H6))
contador7 = str(input('Pressione L. '))
H7 = contador7 == calibraH1
print(str(H7))
contador8 = str(input('Pressione L. '))
H8 = contador8 == calibraH1
print(str(H8))
contador9 = str(input('Pressione L. '))
H9 = contador9 == calibraH1
print(str(H9))
contador10 = str(input('Pressione L. '))
H10 = contador10 == calibraH1
print(str(H10))

print('Agora pressione "N" 10 vezes para calibração horizontal')

contador11 = str(input('Pressione N. '))
H11 = contador11 == calibraH2
print(str(H11))
contador12 = str(input('Pressione N. '))
H12 = contador12 == calibraH2
print(str(H12))
contador13 = str(input('Pressione N. '))
H13 = contador13 == calibraH2
print(str(H13))
contador14 = str(input('Pressione N. '))
H14 = contador14 == calibraH2
print(str(H14))
contador15 = str(input('Pressione N. '))
H15 = contador15 == calibraH2
print(str(H15))
contador16 = str(input('Pressione N. '))
H16 = contador16 == calibraH2
print(str(H16))
contador17 = str(input('Pressione N. '))
H17 = contador17 == calibraH2
print(str(H17))
contador18 = str(input('Pressione N. '))
H18 = contador18 == calibraH2
print(str(H18))
contador19 = str(input('Pressione N. '))
H19 = contador19 == calibraH2
print(str(H19))
contador20 = str(input('Pressione N. '))
H20 = contador20 == calibraH2
print(str(H20))

print('Calibração horizontal efetuada com sucesso!')

print('Pressione "U" 10 vezes para calibração vertical')

contador1 = str(input('Pressione U. '))
H = contador1 == calibraV1
print(str(H))
contador2 = str(input('Pressione U. '))
H2 = contador2 == calibraV1
print(str(H2))
contador3 = str(input('Pressione U. '))
H3 = contador3 == calibraV1
print(str(H3))
contador4 = str(input('Pressione U. '))
H4 = contador4 == calibraV1
print(str(H4))
contador5 = str(input('Pressione U. '))
H5 = contador5 == calibraV1
print(str(H5))
contador6 = str(input('Pressione U. '))
H6 = contador6 == calibraV1
print(str(H6))
contador7 = str(input('Pressione U. '))
H7 = contador7 == calibraV1
print(str(H7))
contador8 = str(input('Pressione U. '))
H8 = contador8 == calibraV1
print(str(H8))
contador9 = str(input('Pressione U. '))
H9 = contador9 == calibraV1
print(str(H9))
contador10 = str(input('Pressione U. '))
H10 = contador10 == calibraV1
print(str(H10))

print('Agora pressione "A" 10 vezes para calibração vertical')

contador11 = str(input('Pressione A. '))
H11 = contador11 == calibraV2
print(str(H11))
contador12 = str(input('Pressione A. '))
H12 = contador12 == calibraV2
print(str(H12))
contador13 = str(input('Pressione A. '))
H13 = contador13 == calibraV2
print(str(H13))
contador14 = str(input('Pressione A. '))
H14 = contador14 == calibraV2
print(str(H14))
contador15 = str(input('Pressione A. '))
H15 = contador15 == calibraV2
print(str(H15))
contador16 = str(input('Pressione A. '))
H16 = contador16 == calibraV2
print(str(H16))
contador17 = str(input('Pressione A. '))
H17 = contador17 == calibraV2
print(str(H17))
contador18 = str(input('Pressione A. '))
H18 = contador18 == calibraV2
print(str(H18))
contador19 = str(input('Pressione A. '))
H19 = contador19 == calibraV2
print(str(H19))
contador20 = str(input('Pressione A. '))
H20 = contador20 == calibraV2
print(str(H20))

print('Calibração efetuada com sucesso!')