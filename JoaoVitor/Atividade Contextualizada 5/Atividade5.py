tupla_head = ['regiao', 'estado', 'municipio', 'coduf', 'codmun', 'codRegiaoSaude', 'nomeRegiaoSaude', 'data', 'semanaEpi', 'populacaoTCU2019', 'casosAcumulado', 'casosNovos', 'obitosAcumulado', 'obitosNovos', 'Recuperadosnovos', 'emAcompanhamentoNovos', 'interior/metropolitana']

print ("Dados da Covid-19 no Brasil, para a data de 26/08/2020")

#Questao 1a
lista_cov = [['Norte', 'RO', 0, 11, 0, 0, 0, 26/8/2020, 35, 1777225, 53119, 605, 1100, 13, 0, 0, 0],
['Norte', 'AC', 0, 12, 0, 0, 0, 26/8/2020, 35, 881935, 24119, 183, 607, 0, 0, 0, 0],
['Norte', 'AM', 0, 13, 0, 0, 0, 26/8/2020, 35, 4144597, 117412, 833, 3600, 12, 0, 0, 0],
['Norte', 'RR', 0, 14, 0, 0, 0, 26/8/2020, 35, 605761, 42359, 315, 582, 0, 0, 0, 0],
['Norte', 'PA', 0, 15, 0, 0, 0, 26/8/2020, 35, 8602865, 193564, 1955, 6097, 19, 0, 0, 0],
['Norte', 'AP', 0, 16, 0, 0, 0, 26/8/2020, 35, 845731, 41981, 428, 647, 5, 0, 0, 0],
['Norte', 'TO', 0, 17, 0, 0, 0, 26/8/2020, 35, 1572866, 46364, 964, 621, 11, 0, 0, 0],
['Nordeste', 'MA', 0, 21, 0, 0, 0, 26/8/2020, 35, 7075181, 147676, 1755, 3390, 13, 0, 0, 0],
['Nordeste', 'PI', 0, 22, 0, 0, 0, 26/8/2020, 35, 3273227, 74096, 1140, 1754, 13, 0, 0, 0],
['Nordeste', 'CE', 0, 23, 0, 0, 0, 26/8/2020, 35, 9132078, 208782, 1396, 8351, 12, 0, 0, 0],
['Nordeste', 'RN', 0, 24, 0, 0, 0, 26/8/2020, 35, 3506853, 60442, 281, 2215, 23, 0, 0, 0],
['Nordeste', 'PB', 0, 25, 0, 0, 0, 26/8/2020, 35, 4018127, 103213, 1005, 2371, 21, 0, 0, 0],
['Nordeste', 'PE', 0, 26, 0, 0, 0, 26/8/2020, 35, 9557071, 121078, 1120, 7460, 35, 0, 0, 0],
['Nordeste', 'AL', 0, 27, 0, 0, 0, 26/8/2020, 35, 3337357, 77317, 423, 1844, 8, 0, 0, 0],
['Nordeste', 'SE', 0, 28, 0, 0, 0, 26/8/2020, 35, 2298696, 71222, 296, 1822, 14, 0, 0, 0],
['Nordeste', 'BA', 0, 29, 0, 0, 0, 26/8/2020, 35, 14873064, 245021, 4082, 5116, 65, 0, 0, 0],
['Sudeste', 'MG', 0, 31, 0, 0, 0, 26/8/2020, 35, 21168791, 201973, 3237, 4948, 101, 0, 0, 0],
['Sudeste', 'ES', 0, 32, 0, 0, 0, 26/8/2020, 35, 4018650, 107909, 718, 3086, 18, 0, 0, 0],
['Sudeste', 'RJ', 0, 33, 0, 0, 0, 26/8/2020, 35, 17264943, 216675, 2672, 15700, 140, 0, 0, 0],
['Sudeste', 'SP', 0, 35, 0, 0, 0, 26/8/2020, 35, 45919049, 776135, 10465, 29194, 282, 0, 0, 0],
['Sul', 'PR', 0, 41, 0, 0, 0, 26/8/2020, 35, 11433957, 122241, 1704, 3102, 40, 0, 0, 0],
['Sul', 'SC', 0, 42, 0, 0, 0, 26/8/2020, 35, 7164788, 137560, 1870, 2142, 26, 0, 0, 0],
['Sul', 'RS', 0, 43, 0, 0, 0, 26/8/2020, 35, 11377239, 115984, 3221, 3235, 74, 0, 0, 0],
['Centro-Oeste', 'MS', 0, 50, 0, 0, 0, 26/8/2020, 35, 2778986, 45359, 1035, 783, 16, 0, 0, 0],
['Centro-Oeste', 'MT', 0, 51, 0, 0, 0, 26/8/2020, 35, 3484466, 85709, 1432, 2611, 20, 0, 0, 0],
['Centro-Oeste', 'GO', 0, 52, 0, 0, 0, 26/8/2020, 35, 7018354, 124593, 2463, 2888, 49, 0, 0, 0],
['Centro-Oeste', 'DF', 0, 53, 0, 0, 0, 26/8/2020, 35, 3015268, 155253, 1563, 2399, 55, 0, 0, 0],
['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', [26, 8, 2020], 35, 3015268, 155253, 1563, 2399, 55, 0, 0, 1],
['Sudeste', 'SP', 'São Paulo', 35, 355030, 35016, 'SAO PAULO', [26, 8, 2020], 35, 12252023, 252063, 1892, 11215, 74, 0, 0, 1],
['Nordeste', 'PB', 'Alhandra', 25, 250060, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 19588, 627, 2, 17, 0, 0, 0, 1],
['Nordeste', 'PB', 'Bayeux', 25, 250180, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 96880, 1731, 3, 95, 1, 0, 0, 1],
['Nordeste', 'PB', 'Caaporã', 25, 250300, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 21828, 947, 8, 13, 0, 0, 0, 1],
['Nordeste', 'PB', 'Cabedelo', 25, 250320, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 67736, 2713, 25, 59, 0, 0, 0, 1],
['Nordeste', 'PB', 'Conde', 25, 250460, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 24670, 761, 3, 13, 1, 0, 0, 1],
['Nordeste', 'PB', 'Cruz do Espírito Santo', 25, 250490, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 17319, 286, 0, 20, 0, 0, 0, 1],
['Nordeste', 'PB', 'João Pessoa', 25, 250750, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 809015, 26351, 242, 809, 4, 0, 0, 1],
['Nordeste', 'PB', 'Lucena', 25, 250860, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 13080, 439, 7, 6, 0, 0, 0, 1],
['Nordeste', 'PB', 'Mari', 25, 250910, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 21837, 1147, 4, 16, 0, 0, 0, 0],
['Nordeste', 'PB', 'Pitimbu', 25, 251190, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 19065, 615, 0, 8, 0, 0, 0, 1],
['Nordeste', 'PB', 'Riachão do Poço', 25, 251276, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 4509, 94, 1, 2, 0, 0, 0, 0],
['Nordeste', 'PB', 'Santa Rita', 25, 251370, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 136586, 2978, 18, 142, 0, 0, 0, 1],
['Nordeste', 'PB', 'Sapé', 25, 251530, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 52625, 1098, 5, 43, 0, 0, 0, 0],
['Nordeste', 'PB', 'Sobrado', 25, 251597, 25001, '1ª REGIAO MATA ATLANTICA', [26, 8, 2020], 35, 7783, 189, 0, 4, 0, 0, 0, 0],
['Nordeste', 'BA', 'Campo Alegre de Lourdes', 29, 290590, 29016, 'JUAZEIRO', [26, 8, 2020], 35, 28798, 100, 1, 2, 0, 0, 0, 0],
['Nordeste', 'BA', 'Canudos', 29, 290682, 29016, 'JUAZEIRO', [26, 8, 2020], 35, 16668, 102, 0, 3, 0, 0, 0, 0],
['Nordeste', 'BA', 'Casa Nova', 29, 290720, 29016, 'JUAZEIRO', [26, 8, 2020], 35, 71969, 380, 19, 8, 0, 0, 0, 0],
['Nordeste', 'BA', 'Curaçá', 29, 290990, 29016, 'JUAZEIRO', [26, 8, 2020], 35, 34700, 248, 8, 2, 0, 0, 0, 0],
['Nordeste', 'BA', 'Juazeiro', 29, 291840, 29016, 'JUAZEIRO', [26, 8, 2020], 35, 216707, 4256, 57, 77, 1, 0, 0, 0],
['Nordeste', 'BA', 'Pilão Arcado', 29, 292440, 29016, 'JUAZEIRO', [26, 8, 2020], 35, 35048, 87, 3, 0, 0, 0, 0, 0],
['Nordeste', 'BA', 'Remanso', 29, 292600, 29016, 'JUAZEIRO', [26, 8, 2020], 35, 41008, 124, 3, 4, 0, 0, 0, 0],
['Nordeste', 'BA', 'Sento Sé', 29, 293020, 29016, 'JUAZEIRO', [26, 8, 2020], 35, 40684, 275, 2, 4, 0, 0, 0, 0],
['Nordeste', 'BA', 'Sobradinho', 29, 293077, 29016, 'JUAZEIRO', [26, 8, 2020], 35, 23191, 402, 7, 11, 0, 0, 0, 0],
['Nordeste', 'BA', 'Uauá', 29, 293200, 29016, 'JUAZEIRO', [26, 8, 2020], 35, 24240, 396, 3, 5, 0, 0, 0, 0],
['Norte', 'RO', 'Cacoal', 11, 110004, 11002, 'CAFE', [26, 8, 2020], 35, 85359, 1610, 53, 22, 1, 0, 0, 0],
['Norte', 'RO', 'Espigão DOeste', 11, 110009, 11002, 'CAFE', [26, 8, 2020], 35, 32374, 443, 5, 8, 0, 0, 0, 0],
['Norte', 'RO', 'Pimenta Bueno', 11, 110018, 11002, 'CAFE', [26, 8, 2020], 35, 36660, 526, 8, 10, 0, 0, 0, 0],
['Norte', 'RO', 'Ministro Andreazza', 11, 110120, 11002, 'CAFE', [26, 8, 2020], 35, 9660, 19, 1, 1, 0, 0, 0, 0],
['Norte', 'RO', 'Primavera de Rondônia', 11, 110147, 11002, 'CAFE', [26, 8, 2020], 35, 2856, 16, 0, 0, 0, 0, 0, 0],
['Norte', 'RO', 'São Felipe DOeste', 11, 110148, 11002, 'CAFE', [26, 8, 2020], 35, 5172, 76, 0, 1, 0, 0, 0, 0],
['Nordeste', 'MA', 'Matões', 21, 210660, 21017, 'TIMON', [26, 8, 2020], 35, 33782, 361, 21, 7, 3, 0, 0, 0],
['Nordeste', 'MA', 'Parnarama', 21, 210780, 21017, 'TIMON', [26, 8, 2020], 35, 34907, 448, 11, 0, 0, 0, 0, 0],
['Nordeste', 'MA', 'São Francisco do Maranhão', 21, 211090, 21017, 'TIMON', [26, 8, 2020], 35, 12210, 67, 0, 0, 0, 0, 0, 0],
['Nordeste', 'MA', 'Timon', 21, 211220, 21017, 'TIMON', [26, 8, 2020], 35, 169107, 3517, 154, 100, 0, 0, 0, 0],
['Sudeste', 'MG', 'Contagem', 31, 311860, 31018, 'CONTAGEM', [26, 8, 2020], 35, 663855, 6725, 0, 264, 4, 0, 0, 1],
['Sudeste', 'MG', 'Ibirité', 31, 312980, 31018, 'CONTAGEM', [26, 8, 2020], 35, 180204, 1383, 0, 50, 0, 0, 0, 1],
['Sudeste', 'MG', 'Sarzedo', 31, 316553, 31018, 'CONTAGEM', [26, 8, 2020], 35, 32752, 310, 10, 9, 1, 0, 0, 1],
['Nordeste', 'BA', 'Almadina', 29, 290090, 29012, 'ITABUNA', [26, 8, 2020], 35, 5464, 307, 0, 4, 0, 0, 0, 0],
['Nordeste', 'BA', 'Aurelino Leal', 29, 290240, 29012, 'ITABUNA', [26, 8, 2020], 35, 11531, 357, 1, 4, 0, 0, 0, 0],
['Nordeste', 'BA', 'Barro Preto', 29, 290330, 29012, 'ITABUNA', [26, 8, 2020], 35, 5591, 211, 0, 3, 0, 0, 0, 0],
['Nordeste', 'BA', 'Buerarema', 29, 290470, 29012, 'ITABUNA', [26, 8, 2020], 35, 18349, 408, 7, 12, 0, 0, 0, 0],
['Nordeste', 'BA', 'Camacan', 29, 290560, 29012, 'ITABUNA', [26, 8, 2020], 35, 31988, 1190, 26, 23, 0, 0, 0, 0],
['Nordeste', 'BA', 'Coaraci', 29, 290800, 29012, 'ITABUNA', [26, 8, 2020], 35, 16993, 357, 3, 5, 0, 0, 0, 0],
['Nordeste', 'BA', 'Floresta Azul', 29, 291100, 29012, 'ITABUNA', [26, 8, 2020], 35, 10629, 250, 5, 6, 0, 0, 0, 0],
['Nordeste', 'BA', 'Gongogi', 29, 291150, 29012, 'ITABUNA', [26, 8, 2020], 35, 7128, 78, 0, 3, 0, 0, 0, 0],
['Nordeste', 'BA', 'Ibicaraí', 29, 291210, 29012, 'ITABUNA', [26, 8, 2020], 35, 21689, 510, 5, 12, 0, 0, 0, 0],
['Nordeste', 'BA', 'Ibirapitanga', 29, 291270, 29012, 'ITABUNA', [26, 8, 2020], 35, 23375, 574, 15, 5, 0, 0, 0, 0],
['Nordeste', 'BA', 'Itabuna', 29, 291480, 29012, 'ITABUNA', [26, 8, 2020], 35, 213223, 9937, 183, 179, 0, 0, 0, 0],
['Nordeste', 'BA', 'Itaju do Colônia', 29, 291540, 29012, 'ITABUNA', [26, 8, 2020], 35, 6682, 82, 3, 0, 0, 0, 0, 0],
['Nordeste', 'BA', 'Itajuípe', 29, 291550, 29012, 'ITABUNA', [26, 8, 2020], 35, 20491, 843, 10, 16, 0, 0, 0, 0],
['Nordeste', 'BA', 'Itapé', 29, 291620, 29012, 'ITABUNA', [26, 8, 2020], 35, 8761, 395, 2, 5, 0, 0, 0, 0],
['Nordeste', 'BA', 'Itapitanga', 29, 291660, 29012, 'ITABUNA', [26, 8, 2020], 35, 10313, 107, 1, 1, 0, 0, 0, 0],
['Nordeste', 'BA', 'Jussari', 29, 291855, 29012, 'ITABUNA', [26, 8, 2020], 35, 5833, 159, 0, 4, 0, 0, 0, 0],
['Nordeste', 'BA', 'Maraú', 29, 292070, 29012, 'ITABUNA', [26, 8, 2020], 35, 20570, 316, 5, 5, 0, 0, 0, 0],
['Nordeste', 'BA', 'Pau Brasil', 29, 292390, 29012, 'ITABUNA', [26, 8, 2020], 35, 9831, 190, 3, 5, 0, 0, 0, 0],
['Nordeste', 'BA', 'Santa Cruz da Vitória', 29, 292780, 29012, 'ITABUNA', [26, 8, 2020], 35, 6315, 97, 0, 1, 0, 0, 0, 0],
['Nordeste', 'BA', 'São José da Vitória', 29, 292935, 29012, 'ITABUNA', [26, 8, 2020], 35, 5657, 199, 6, 2, 0, 0, 0, 0],
['Nordeste', 'BA', 'Ubaitaba', 29, 293220, 29012, 'ITABUNA', [26, 8, 2020], 35, 19056, 298, 6, 10, 0, 0, 0, 0],
['Nordeste', 'BA', 'Ubatã', 29, 293230, 29012, 'ITABUNA', [26, 8, 2020], 35, 27035, 945, 18, 11, 0, 0, 0, 0],
['Centro-Oeste', 'MS', 'Corumbá', 50, 500320, 50002, 'CORUMBA', [26, 8, 2020], 35, 111435, 2314, 53, 87, 3, 0, 0, 0],
['Centro-Oeste', 'MS', 'Ladário', 50, 500520, 50002, 'CORUMBA', [26, 8, 2020], 35, 23331, 472, 19, 10, 0, 0, 0, 0],
['Sudeste', 'MG', 'Itaguara', 31, 313220, 31031, 'ITAUNA', [26, 8, 2020], 35, 13358, 262, 0, 1, 0, 0, 0, 1],
['Sudeste', 'MG', 'Itatiaiuçu', 31, 313370, 31031, 'ITAUNA', [26, 8, 2020], 35, 11146, 249, 0, 4, 0, 0, 0, 1],
['Sudeste', 'MG', 'Itaúna', 31, 313380, 31031, 'ITAUNA', [26, 8, 2020], 35, 93214, 390, 19, 5, 0, 0, 0, 0],
['Sudeste', 'MG', 'Piracema', 31, 315060, 31031, 'ITAUNA', [26, 8, 2020], 35, 6409, 35, 0, 1, 0, 0, 0, 0]]

tupla_cov = (('Norte', 'RO', 0, 11, 0, 0, 0, 26/8/2020, 35, 1777225, 53119, 605, 1100, 13, 0, 0, 0),
('Norte', 'AC', 0, 12, 0, 0, 0, 26/8/2020, 35, 881935, 24119, 183, 607, 0, 0, 0, 0),
('Norte', 'AM', 0, 13, 0, 0, 0, 26/8/2020, 35, 4144597, 117412, 833, 3600, 12, 0, 0, 0),
('Norte', 'RR', 0, 14, 0, 0, 0, 26/8/2020, 35, 605761, 42359, 315, 582, 0, 0, 0, 0),
('Norte', 'PA', 0, 15, 0, 0, 0, 26/8/2020, 35, 8602865, 193564, 1955, 6097, 19, 0, 0, 0),
('Norte', 'AP', 0, 16, 0, 0, 0, 26/8/2020, 35, 845731, 41981, 428, 647, 5, 0, 0, 0),
('Norte', 'TO', 0, 17, 0, 0, 0, 26/8/2020, 35, 1572866, 46364, 964, 621, 11, 0, 0, 0),
('Nordeste', 'MA', 0, 21, 0, 0, 0, 26/8/2020, 35, 7075181, 147676, 1755, 3390, 13, 0, 0, 0),
('Nordeste', 'PI', 0, 22, 0, 0, 0, 26/8/2020, 35, 3273227, 74096, 1140, 1754, 13, 0, 0, 0),
('Nordeste', 'CE', 0, 23, 0, 0, 0, 26/8/2020, 35, 9132078, 208782, 1396, 8351, 12, 0, 0, 0),
('Nordeste', 'RN', 0, 24, 0, 0, 0, 26/8/2020, 35, 3506853, 60442, 281, 2215, 23, 0, 0, 0),
('Nordeste', 'PB', 0, 25, 0, 0, 0, 26/8/2020, 35, 4018127, 103213, 1005, 2371, 21, 0, 0, 0),
('Nordeste', 'PE', 0, 26, 0, 0, 0, 26/8/2020, 35, 9557071, 121078, 1120, 7460, 35, 0, 0, 0),
('Nordeste', 'AL', 0, 27, 0, 0, 0, 26/8/2020, 35, 3337357, 77317, 423, 1844, 8, 0, 0, 0),
('Nordeste', 'SE', 0, 28, 0, 0, 0, 26/8/2020, 35, 2298696, 71222, 296, 1822, 14, 0, 0, 0),
('Nordeste', 'BA', 0, 29, 0, 0, 0, 26/8/2020, 35, 14873064, 245021, 4082, 5116, 65, 0, 0, 0),
('Sudeste', 'MG', 0, 31, 0, 0, 0, 26/8/2020, 35, 21168791, 201973, 3237, 4948, 101, 0, 0, 0),
('Sudeste', 'ES', 0, 32, 0, 0, 0, 26/8/2020, 35, 4018650, 107909, 718, 3086, 18, 0, 0, 0),
('Sudeste', 'RJ', 0, 33, 0, 0, 0, 26/8/2020, 35, 17264943, 216675, 2672, 15700, 140, 0, 0, 0),
('Sudeste', 'SP', 0, 35, 0, 0, 0, 26/8/2020, 35, 45919049, 776135, 10465, 29194, 282, 0, 0, 0),
('Sul', 'PR', 0, 41, 0, 0, 0, 26/8/2020, 35, 11433957, 122241, 1704, 3102, 40, 0, 0, 0),
('Sul', 'SC', 0, 42, 0, 0, 0, 26/8/2020, 35, 7164788, 137560, 1870, 2142, 26, 0, 0, 0),
('Sul', 'RS', 0, 43, 0, 0, 0, 26/8/2020, 35, 11377239, 115984, 3221, 3235, 74, 0, 0, 0),
('Centro-Oeste', 'MS', 0, 50, 0, 0, 0, 26/8/2020, 35, 2778986, 45359, 1035, 783, 16, 0, 0, 0),
('Centro-Oeste', 'MT', 0, 51, 0, 0, 0, 26/8/2020, 35, 3484466, 85709, 1432, 2611, 20, 0, 0, 0),
('Centro-Oeste', 'GO', 0, 52, 0, 0, 0, 26/8/2020, 35, 7018354, 124593, 2463, 2888, 49, 0, 0, 0),
('Centro-Oeste', 'DF', 0, 53, 0, 0, 0, 26/8/2020, 35, 3015268, 155253, 1563, 2399, 55, 0, 0, 0),
('Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', (26, 8, 2020), 35, 3015268, 155253, 1563, 2399, 55, 0, 0, 1),
('Sudeste', 'SP', 'São Paulo', 35, 355030, 35016, 'SAO PAULO', (26, 8, 2020), 35, 12252023, 252063, 1892, 11215, 74, 0, 0, 1),
('Nordeste', 'PB', 'Alhandra', 25, 250060, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 19588, 627, 2, 17, 0, 0, 0, 1),
('Nordeste', 'PB', 'Bayeux', 25, 250180, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 96880, 1731, 3, 95, 1, 0, 0, 1),
('Nordeste', 'PB', 'Caaporã', 25, 250300, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 21828, 947, 8, 13, 0, 0, 0, 1),
('Nordeste', 'PB', 'Cabedelo', 25, 250320, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 67736, 2713, 25, 59, 0, 0, 0, 1),
('Nordeste', 'PB', 'Conde', 25, 250460, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 24670, 761, 3, 13, 1, 0, 0, 1),
('Nordeste', 'PB', 'Cruz do Espírito Santo', 25, 250490, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 17319, 286, 0, 20, 0, 0, 0, 1),
('Nordeste', 'PB', 'João Pessoa', 25, 250750, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 809015, 26351, 242, 809, 4, 0, 0, 1),
('Nordeste', 'PB', 'Lucena', 25, 250860, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 13080, 439, 7, 6, 0, 0, 0, 1),
('Nordeste', 'PB', 'Mari', 25, 250910, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 21837, 1147, 4, 16, 0, 0, 0, 0),
('Nordeste', 'PB', 'Pitimbu', 25, 251190, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 19065, 615, 0, 8, 0, 0, 0, 1),
('Nordeste', 'PB', 'Riachão do Poço', 25, 251276, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 4509, 94, 1, 2, 0, 0, 0, 0),
('Nordeste', 'PB', 'Santa Rita', 25, 251370, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 136586, 2978, 18, 142, 0, 0, 0, 1),
('Nordeste', 'PB', 'Sapé', 25, 251530, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 52625, 1098, 5, 43, 0, 0, 0, 0),
('Nordeste', 'PB', 'Sobrado', 25, 251597, 25001, '1ª REGIAO MATA ATLANTICA', (26, 8, 2020), 35, 7783, 189, 0, 4, 0, 0, 0, 0),
('Nordeste', 'BA', 'Campo Alegre de Lourdes', 29, 290590, 29016, 'JUAZEIRO', (26, 8, 2020), 35, 28798, 100, 1, 2, 0, 0, 0, 0),
('Nordeste', 'BA', 'Canudos', 29, 290682, 29016, 'JUAZEIRO', (26, 8, 2020), 35, 16668, 102, 0, 3, 0, 0, 0, 0),
('Nordeste', 'BA', 'Casa Nova', 29, 290720, 29016, 'JUAZEIRO', (26, 8, 2020), 35, 71969, 380, 19, 8, 0, 0, 0, 0),
('Nordeste', 'BA', 'Curaçá', 29, 290990, 29016, 'JUAZEIRO', (26, 8, 2020), 35, 34700, 248, 8, 2, 0, 0, 0, 0),
('Nordeste', 'BA', 'Juazeiro', 29, 291840, 29016, 'JUAZEIRO', (26, 8, 2020), 35, 216707, 4256, 57, 77, 1, 0, 0, 0),
('Nordeste', 'BA', 'Pilão Arcado', 29, 292440, 29016, 'JUAZEIRO', (26, 8, 2020), 35, 35048, 87, 3, 0, 0, 0, 0, 0),
('Nordeste', 'BA', 'Remanso', 29, 292600, 29016, 'JUAZEIRO', (26, 8, 2020), 35, 41008, 124, 3, 4, 0, 0, 0, 0),
('Nordeste', 'BA', 'Sento Sé', 29, 293020, 29016, 'JUAZEIRO', (26, 8, 2020), 35, 40684, 275, 2, 4, 0, 0, 0, 0),
('Nordeste', 'BA', 'Sobradinho', 29, 293077, 29016, 'JUAZEIRO', (26, 8, 2020), 35, 23191, 402, 7, 11, 0, 0, 0, 0),
('Nordeste', 'BA', 'Uauá', 29, 293200, 29016, 'JUAZEIRO', (26, 8, 2020), 35, 24240, 396, 3, 5, 0, 0, 0, 0),
('Norte', 'RO', 'Cacoal', 11, 110004, 11002, 'CAFE', (26, 8, 2020), 35, 85359, 1610, 53, 22, 1, 0, 0, 0),
('Norte', 'RO', 'Espigão DOeste', 11, 110009, 11002, 'CAFE', (26, 8, 2020), 35, 32374, 443, 5, 8, 0, 0, 0, 0),
('Norte', 'RO', 'Pimenta Bueno', 11, 110018, 11002, 'CAFE', (26, 8, 2020), 35, 36660, 526, 8, 10, 0, 0, 0, 0),
('Norte', 'RO', 'Ministro Andreazza', 11, 110120, 11002, 'CAFE', (26, 8, 2020), 35, 9660, 19, 1, 1, 0, 0, 0, 0),
('Norte', 'RO', 'Primavera de Rondônia', 11, 110147, 11002, 'CAFE', (26, 8, 2020), 35, 2856, 16, 0, 0, 0, 0, 0, 0),
('Norte', 'RO', 'São Felipe DOeste', 11, 110148, 11002, 'CAFE', (26, 8, 2020), 35, 5172, 76, 0, 1, 0, 0, 0, 0),
('Nordeste', 'MA', 'Matões', 21, 210660, 21017, 'TIMON', (26, 8, 2020), 35, 33782, 361, 21, 7, 3, 0, 0, 0),
('Nordeste', 'MA', 'Parnarama', 21, 210780, 21017, 'TIMON', (26, 8, 2020), 35, 34907, 448, 11, 0, 0, 0, 0, 0),
('Nordeste', 'MA', 'São Francisco do Maranhão', 21, 211090, 21017, 'TIMON', (26, 8, 2020), 35, 12210, 67, 0, 0, 0, 0, 0, 0),
('Nordeste', 'MA', 'Timon', 21, 211220, 21017, 'TIMON', (26, 8, 2020), 35, 169107, 3517, 154, 100, 0, 0, 0, 0),
('Sudeste', 'MG', 'Contagem', 31, 311860, 31018, 'CONTAGEM', (26, 8, 2020), 35, 663855, 6725, 0, 264, 4, 0, 0, 1),
('Sudeste', 'MG', 'Ibirité', 31, 312980, 31018, 'CONTAGEM', (26, 8, 2020), 35, 180204, 1383, 0, 50, 0, 0, 0, 1),
('Sudeste', 'MG', 'Sarzedo', 31, 316553, 31018, 'CONTAGEM', (26, 8, 2020), 35, 32752, 310, 10, 9, 1, 0, 0, 1),
('Nordeste', 'BA', 'Almadina', 29, 290090, 29012, 'ITABUNA', (26, 8, 2020), 35, 5464, 307, 0, 4, 0, 0, 0, 0),
('Nordeste', 'BA', 'Aurelino Leal', 29, 290240, 29012, 'ITABUNA', (26, 8, 2020), 35, 11531, 357, 1, 4, 0, 0, 0, 0),
('Nordeste', 'BA', 'Barro Preto', 29, 290330, 29012, 'ITABUNA', (26, 8, 2020), 35, 5591, 211, 0, 3, 0, 0, 0, 0),
('Nordeste', 'BA', 'Buerarema', 29, 290470, 29012, 'ITABUNA', (26, 8, 2020), 35, 18349, 408, 7, 12, 0, 0, 0, 0),
('Nordeste', 'BA', 'Camacan', 29, 290560, 29012, 'ITABUNA', (26, 8, 2020), 35, 31988, 1190, 26, 23, 0, 0, 0, 0),
('Nordeste', 'BA', 'Coaraci', 29, 290800, 29012, 'ITABUNA', (26, 8, 2020), 35, 16993, 357, 3, 5, 0, 0, 0, 0),
('Nordeste', 'BA', 'Floresta Azul', 29, 291100, 29012, 'ITABUNA', (26, 8, 2020), 35, 10629, 250, 5, 6, 0, 0, 0, 0),
('Nordeste', 'BA', 'Gongogi', 29, 291150, 29012, 'ITABUNA', (26, 8, 2020), 35, 7128, 78, 0, 3, 0, 0, 0, 0),
('Nordeste', 'BA', 'Ibicaraí', 29, 291210, 29012, 'ITABUNA', (26, 8, 2020), 35, 21689, 510, 5, 12, 0, 0, 0, 0),
('Nordeste', 'BA', 'Ibirapitanga', 29, 291270, 29012, 'ITABUNA', (26, 8, 2020), 35, 23375, 574, 15, 5, 0, 0, 0, 0),
('Nordeste', 'BA', 'Itabuna', 29, 291480, 29012, 'ITABUNA', (26, 8, 2020), 35, 213223, 9937, 183, 179, 0, 0, 0, 0),
('Nordeste', 'BA', 'Itaju do Colônia', 29, 291540, 29012, 'ITABUNA', (26, 8, 2020), 35, 6682, 82, 3, 0, 0, 0, 0, 0),
('Nordeste', 'BA', 'Itajuípe', 29, 291550, 29012, 'ITABUNA', (26, 8, 2020), 35, 20491, 843, 10, 16, 0, 0, 0, 0),
('Nordeste', 'BA', 'Itapé', 29, 291620, 29012, 'ITABUNA', (26, 8, 2020), 35, 8761, 395, 2, 5, 0, 0, 0, 0),
('Nordeste', 'BA', 'Itapitanga', 29, 291660, 29012, 'ITABUNA', (26, 8, 2020), 35, 10313, 107, 1, 1, 0, 0, 0, 0),
('Nordeste', 'BA', 'Jussari', 29, 291855, 29012, 'ITABUNA', (26, 8, 2020), 35, 5833, 159, 0, 4, 0, 0, 0, 0),
('Nordeste', 'BA', 'Maraú', 29, 292070, 29012, 'ITABUNA', (26, 8, 2020), 35, 20570, 316, 5, 5, 0, 0, 0, 0),
('Nordeste', 'BA', 'Pau Brasil', 29, 292390, 29012, 'ITABUNA', (26, 8, 2020), 35, 9831, 190, 3, 5, 0, 0, 0, 0),
('Nordeste', 'BA', 'Santa Cruz da Vitória', 29, 292780, 29012, 'ITABUNA', (26, 8, 2020), 35, 6315, 97, 0, 1, 0, 0, 0, 0),
('Nordeste', 'BA', 'São José da Vitória', 29, 292935, 29012, 'ITABUNA', (26, 8, 2020), 35, 5657, 199, 6, 2, 0, 0, 0, 0),
('Nordeste', 'BA', 'Ubaitaba', 29, 293220, 29012, 'ITABUNA', (26, 8, 2020), 35, 19056, 298, 6, 10, 0, 0, 0, 0),
('Nordeste', 'BA', 'Ubatã', 29, 293230, 29012, 'ITABUNA', (26, 8, 2020), 35, 27035, 945, 18, 11, 0, 0, 0, 0),
('Centro-Oeste', 'MS', 'Corumbá', 50, 500320, 50002, 'CORUMBA', (26, 8, 2020), 35, 111435, 2314, 53, 87, 3, 0, 0, 0),
('Centro-Oeste', 'MS', 'Ladário', 50, 500520, 50002, 'CORUMBA', (26, 8, 2020), 35, 23331, 472, 19, 10, 0, 0, 0, 0),
('Sudeste', 'MG', 'Itaguara', 31, 313220, 31031, 'ITAUNA', (26, 8, 2020), 35, 13358, 262, 0, 1, 0, 0, 0, 1),
('Sudeste', 'MG', 'Itatiaiuçu', 31, 313370, 31031, 'ITAUNA', (26, 8, 2020), 35, 11146, 249, 0, 4, 0, 0, 0, 1),
('Sudeste', 'MG', 'Itaúna', 31, 313380, 31031, 'ITAUNA', (26, 8, 2020), 35, 93214, 390, 19, 5, 0, 0, 0, 0),
('Sudeste', 'MG', 'Piracema', 31, 315060, 31031, 'ITAUNA', (26, 8, 2020), 35, 6409, 35, 0, 1, 0, 0, 0, 0))

#Questao 1b
print ("\nNumero de casos acumulados no estado do Rio de Janeiro:\nLista: " + str(lista_cov[18][10]) + "\t Tupla: " + str(lista_cov[18][10]))

#Questao 1c
print ("\nNumero de obitos acumulados por estado:")
i = 0
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1
print (str(lista_cov[i][1]) + ": " + str(lista_cov[i][12]))
i = i+1

#Questão 1d
print('\nCorrecao de dados da Paraiba: +10 casos reportados')
print('Valor antigo:\nLista:' + str(lista_cov[11][1:17:11]) + '\t Tupla: ' + str(tupla_cov[11][1:17:11]))
lista_cov[11][12] = lista_cov[11][12] + 10  #incremento de 10 na posicao de obitos da paraiba

print('Valor atual:\nLista:' + str(lista_cov[11][1:17:11]) + '\t Tupla: ' + str(tupla_cov[11][1:17:11]))

#Questao 1e
print('\nResposta da questao 1e:\nNao e\' possivel editar o valor de tuplas diretamente. Dessa forma, depende-se da conversao da tupla em uma lista, editar a lista, e assim converte-la de volta a tupla. Entretanto, dentro da tupla existem outras tuplas requerendo uma conversao mais complexa, e inviavel de realizar sem estruturas de repeticao e funcoes.')

#Questao 1f
lista_amapa = [['Norte', 'AP', 'Serra do Navio', 16, 160005, 16001, 'AREA CENTRAL', [26, 8, 2020], 35, 5397, 603, 16, 4, 0, 0, 0, 0],
['Norte', 'AP', 'Pedra Branca do Amapari', 16, 160015, 16001, 'AREA CENTRAL', [26, 8, 2020], 35, 16502, 2508, 20, 5, 0, 0, 0, 0],
['Norte', 'AP', 'Cutias', 16, 160021, 16001, 'AREA CENTRAL', [26, 8, 2020], 35, 5983, 522, 0, 2, 0, 0, 0, 0],
['Norte', 'AP', 'Ferreira Gomes', 16, 160023, 16001, 'AREA CENTRAL', [26, 8, 2020], 35, 7780, 537, 2, 3, 0, 0, 0, 0],
['Norte', 'AP', 'Itaubal', 16, 160025, 16001, 'AREA CENTRAL', [26, 8, 2020], 35, 5503, 286, 0, 0, 0, 0, 0, 0],
['Norte', 'AP', 'Macapá', 16, 160030, 16001, 'AREA CENTRAL', [26, 8, 2020], 35, 503327, 16924, 128, 438, 3, 0, 0, 1],
['Norte', 'AP', 'Porto Grande', 16, 160053, 16001, 'AREA CENTRAL', [26, 8, 2020], 35, 21971, 1090, 3, 13, 0, 0, 0, 0],
['Norte', 'AP', 'Amapá', 16, 160010, 16002, 'AREA NORTE', [26, 8, 2020], 35, 9109, 483, 6, 4, 0, 0, 0, 0],
['Norte', 'AP', 'Calçoene', 16, 160020, 16002, 'AREA NORTE', [26, 8, 2020], 35, 11117, 1121, 0, 5, 0, 0, 0, 0],
['Norte', 'AP', 'Oiapoque', 16, 160050, 16002, 'AREA NORTE', [26, 8, 2020], 35, 27270, 2490, 7, 19, 0, 0, 0, 0],
['Norte', 'AP', 'Pracuúba', 16, 160055, 16002, 'AREA NORTE', [26, 8, 2020], 35, 5120, 350, 0, 3, 1, 0, 0, 0],
['Norte', 'AP', 'Tartarugalzinho', 16, 160070, 16002, 'AREA NORTE', [26, 8, 2020], 35, 17315, 986, 5, 4, 0, 0, 0, 0],
['Norte', 'AP', 'Laranjal do Jari', 16, 160027, 16003, 'AREA SUDOESTE', [26, 8, 2020], 35, 50410, 4215, 35, 44, 1, 0, 0, 0],
['Norte', 'AP', 'Mazagão', 16, 160040, 16003, 'AREA SUDOESTE', [26, 8, 2020], 35, 21632, 1346, 0, 8, 0, 0, 0, 1],
['Norte', 'AP', 'Santana', 16, 160060, 16003, 'AREA SUDOESTE', [26, 8, 2020], 35, 121364, 6536, 163, 82, 0, 0, 0, 1],
['Norte', 'AP', 'Vitória do Jari', 16, 160080, 16003, 'AREA SUDOESTE', [26, 8, 2020], 35, 15931, 1984, 43, 13, 0, 0, 0, 0]]


i = 0
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i]); i = i+1
lista_cov.append(lista_amapa[i])

#Questao 1g
print ('\nRemover os dados sobre as regioes de sau\'de de todas as entradas da lista. Esses dados estao nos i\'ndices 6 e 7')
#apaga os indices 6 e 7 com .pop(5), pois depois de excluir o indice 6, o indice 7 toma seu lugar, se tornando o novo indice 6

i = 0
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5); i = i+1
lista_cov[i].pop(5); lista_cov[i].pop(5)


#Questao 1h
print('\nCarregar os dados dos municipios do Amapa do dia 18/08/2020 e comparar aos da lista mais atual. Caso os valores sejam iguais, exibir na tela.')
lista_18 = [['Norte', 'AP', 'Serra do Navio', 16, 160005, 16001, 'AREA CENTRAL', [18, 8, 2020], 34, 5397, 574, 2, 4, 0, 0, 0, 0],
['Norte', 'AP', 'Pedra Branca do Amapari', 16, 160015, 16001, 'AREA CENTRAL', [18, 8, 2020], 34, 16502, 2436, 3, 5, 0, 0, 0, 0],
['Norte', 'AP', 'Cutias', 16, 160021, 16001, 'AREA CENTRAL', [18, 8, 2020], 34, 5983, 522, 0, 2, 0, 0, 0, 0],
['Norte', 'AP', 'Ferreira Gomes', 16, 160023, 16001, 'AREA CENTRAL', [18, 8, 2020], 34, 7780, 532, 1, 3, 0, 0, 0, 0],
['Norte', 'AP', 'Itaubal', 16, 160025, 16001, 'AREA CENTRAL', [18, 8, 2020], 34, 5503, 286, 0, 0, 0, 0, 0, 0],
['Norte', 'AP', 'Macapá', 16, 160030, 16001, 'AREA CENTRAL', [18, 8, 2020], 34, 503327, 16297, 68, 417, 1, 0, 0, 1],
['Norte', 'AP', 'Porto Grande', 16, 160053, 16001, 'AREA CENTRAL', [18, 8, 2020], 34, 21971, 1030, 2, 10, 0, 0, 0, 0],
['Norte', 'AP', 'Amapá', 16, 160010, 16002, 'AREA NORTE', [18, 8, 2020], 34, 9109, 449, 4, 4, 0, 0, 0, 0],
['Norte', 'AP', 'Calçoene', 16, 160020, 16002, 'AREA NORTE', [18, 8, 2020], 34, 11117, 1118, 1, 5, 0, 0, 0, 0],
['Norte', 'AP', 'Oiapoque', 16, 160050, 16002, 'AREA NORTE', [18, 8, 2020], 34, 27270, 2333, 0, 19, 0, 0, 0, 0],
['Norte', 'AP', 'Pracuúba', 16, 160055, 16002, 'AREA NORTE', [18, 8, 2020], 34, 5120, 350, 0, 2, 0, 0, 0, 0],
['Norte', 'AP', 'Tartarugalzinho', 16, 160070, 16002, 'AREA NORTE', [18, 8, 2020], 34, 17315, 921, 24, 4, 0, 0, 0, 0],
['Norte', 'AP', 'Laranjal do Jari', 16, 160027, 16003, 'AREA SUDOESTE', [18, 8, 2020], 34, 50410, 4020, 60, 43, 0, 0, 0, 0],
['Norte', 'AP', 'Mazagão', 16, 160040, 16003, 'AREA SUDOESTE', [18, 8, 2020], 34, 21632, 1318, 9, 7, 0, 0, 0, 1],
['Norte', 'AP', 'Santana', 16, 160060, 16003, 'AREA SUDOESTE', [18, 8, 2020], 34, 121364, 5988, 59, 81, 1, 0, 0, 1],
['Norte', 'AP', 'Vitória do Jari', 16, 160080, 16003, 'AREA SUDOESTE', [18, 8, 2020], 34, 15931, 1783, 21, 13, 0, 0, 0, 0]]

soma_acumulado18 = 0
soma_casosnovos18 = 0
soma_obitos18 = 0
soma_obitosnovos18 = 0
i = 0

soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]; i = i+1
soma_acumulado18 = soma_acumulado18+lista_18[i][10]; soma_casosnovos18 = soma_casosnovos18 + lista_18[i][11]; soma_obitos18 = soma_obitos18 + lista_18[i][12]; soma_obitosnovos18 = soma_obitosnovos18 + lista_18[i][13]

if (soma_acumulado18 == lista_cov[5][8]):
    print('\nCasos acumulados em 18/08/2020: ' + str(soma_acumulado18) + '\tCasos acumulados em 25/08/2020: ' + str(lista_cov[5][8]))
if (soma_casosnovos18 == lista_cov[5][9]):
    print('\nCasos novos em 18/08/2020: ' + str(soma_casosnovos18) + '\tCasos novos em 25/08/2020: ' + str(lista_cov[5][9]))
if (soma_obitos18 == lista_cov[5][10]):
    print('\nTotal de obitos em 18/08/2020: ' + str(soma_obitos18) + '\tTotal de obitos em 25/08/2020: ' + str(lista_cov[5][10]))
if (soma_obitos18 == lista_cov[5][11]):
    print('\nObitos novos em 18/08/2020: ' + str(soma_obitosnovos18) + '\tObitos novos em 25/08/2020: ' + str(lista_cov[5][11]))

#Questao 1i
print ('\nO tamanho total da lista e\': ' + str(len(lista_cov)))

#Questao 1j

print ('\nCriacao de nova lista com numero de obitos novos para verificacao de maior e menor valor local.')
i = 0
lista_obitos = []
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11]); i = i+1
lista_obitos.append(lista_cov[i][11])

print('Maior numero da lista: ' + str(max(lista_obitos)) + '\t Menor numero da lista: ' + str(min(lista_obitos)))

#Questao 1k

dicionario_amapa = {}

i = 0
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]; i = i + 1
dicionario_amapa[lista_amapa[i][2]] = [lista_amapa[i][2], lista_amapa[i][9]]

print('\nLista de municipios do Amapa: ' + str(dicionario_amapa.keys()))
municipio = input ('Digite o nome do municipio do Amapa que voce deseja consultar o numero de casos novos: ')
print(dicionario_amapa.get(str(municipio)))

#Questao 1l
print('\nOs dados mais recentes de Terezina/PI serao inseridos na lista, e, em seguida, exibido seu número de casos novos: ')
lista_cov.append(['Nordeste', 'PI', 'Teresina', 22, 221100, [25, 8, 2020], 35, 864845, 23650, 226, 873, 5, 1])

print('Casos novos em Terezina/PI: ' + str(lista_cov[len(lista_cov)-1][9]))