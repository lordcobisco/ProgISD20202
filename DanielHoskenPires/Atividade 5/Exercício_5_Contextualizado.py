#Exercício contextualizado 5 - Dados Covid
#Letra a) 

listaCovid = [['Norte', 'AC', 'Cruzeiro do Sul', 12, 120020, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-05-14 00:00:00', 20, 88376.0, 144, 19, 1, 0, ' ', ' ', 0.0], ['Norte', 'AC', 'Mâncio Lima', 12, 120033, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-06-02 00:00:00', 23, 18977.0, 26, 1, 1, 1, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Girau do Ponciano', 27, 270290, 27007, '7ª REGIAO DE SAUDE', '2020-07-20 00:00:00', 30, 40917.0, 761, 0, 6, 1, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Boca da Mata', 27, 270100, 27005, '5ª REGIAO DE SAUDE', '2020-05-17 00:00:00', 21, 27281.0, 9, -1, 0, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Envira', 13, 130150, 13007, 'REGIONAL JURUA', '2020-05-13 00:00:00', 20, 20033.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Atalaia do Norte', 13, 130020, 13009, 'ALTO SOLIMOES', '2020-04-21 00:00:00', 17, 19921.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'AP', 'Mazagão', 16, 160040, 16003, 'AREA SUDOESTE', '2020-04-01 00:00:00', 14, 21632.0, 0, 0, 0, 0, ' ', ' ', 1.0], ['Norte', 'AP', 'Pedra Branca do Amapari', 16, 160015, 16001, 'AREA CENTRAL', '2020-04-06 00:00:00', 15, 16502.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'Utinga', 29, 293280, 29011, 'ITABERABA', '2020-06-26 00:00:00', 26, 19178.0, 3, 0, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'Planaltino', 29, 292490, 29015, 'JEQUIE', '2020-07-24 00:00:00', 30, 9322.0, 2, 1, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Penaforte', 23, 231060, 23019, '19ª REGIAO BREJO SANTO', '2020-04-25 00:00:00', 17, 9077.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Acaraú', 23, 230020, 23012, '12ª REGIAO ACARAU', '2020-06-24 00:00:00', 26, 62641.0, 1469, 6, 35, 5, ' ', ' ', 0.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-07-09 00:00:00', 28, 3015268.0, 65677, 1363, 823, 22, ' ', ' ', 1.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-04-07 00:00:00', 15, 3015268.0, 492, 19, 12, 2, ' ', ' ', 1.0], ['Sudeste', 'ES', 'São Domingos do Norte', 32, 320465, 32001, 'CENTRAL', '2020-08-16 00:00:00', 34, 8638.0, 232, 0, 8, 0, ' ', ' ', 0.0], ['Sudeste', 'ES', 'Pedro Canário', 32, 320405, 32003, 'NORTE', '2020-06-27 00:00:00', 26, 26184.0, 147, 0, 4, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Piracanjuba', 52, 521710, 52002, 'CENTRO SUL', '2020-06-03 00:00:00', 23, 24524.0, 15, 0, 1, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Campos Belos', 52, 520490, 52006, 'NORDESTE I', '2020-08-21 00:00:00', 34, 19887.0, 135, 0, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Pastos Bons', 21, 210800, 21015, 'SAO JOAO DOS PATOS', '2020-07-07 00:00:00', 28, 19472.0, 41, 0, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Peritoró', 21, 210845, 21007, 'CODO', '2020-08-21 00:00:00', 34, 23196.0, 329, 0, 3, 0, ' ', ' ', 0.0], ['Sudeste', 'MG', 'Aiuruoca', 31, 310120, 31008, 'SAO LOURENCO', '2020-06-15 00:00:00', 25, 6003.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'MG', 'Santa Cruz de Minas', 31, 315733, 31015, 'SAO JOAO DEL REI', '2020-04-15 00:00:00', 16, 8604.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Brasilândia', 50, 500230, 50004, 'TRES LAGOAS', '2020-04-12 00:00:00', 16, 11872.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Sete Quedas', 50, 500770, 50003, 'DOURADOS', '2020-05-29 00:00:00', 22, 10791.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Colniza', 51, 510325, 51008, 'NOROESTE MATOGROSSENSE', '2020-08-06 00:00:00', 32, 38582.0, 44, 2, 1, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Ribeirão Cascalheira', 51, 510718, 51006, 'MEDIO ARAGUAIA', '2020-07-27 00:00:00', 31, 10206.0, 101, 0, 7, 1, ' ', ' ', 0.0], ['Norte', 'PA', 'Capitão Poço', 15, 150230, 15008, 'METROPOLITANA III', '2020-04-07 00:00:00', 15, 54303.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Igarapé-Miri', 15, 150330, 15011, 'TOCANTINS', '2020-05-17 00:00:00', 21, 62698.0, 134, 20, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Areia', 25, 250110, 25003, '3ª REGIAO', '2020-08-24 00:00:00', 35, 22819.0, 411, 0, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Cachoeira dos Índios', 25, 250330, 25009, '9ª REGIAO', '2020-05-23 00:00:00', 21, 10244.0, 3, 1, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Ferreiros', 26, 260550, 26005, 'GOIANA', '2020-06-12 00:00:00', 24, 12123.0, 74, 0, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Escada', 26, 260520, 26008, 'PALMARES', '2020-06-25 00:00:00', 26, 68875.0, 207, 1, 22, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Pedro Laurentino', 22, 220793, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-05-28 00:00:00', 22, 2536.0, 1, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'São Pedro do Piauí', 22, 221050, 22004, 'ENTRE RIOS', '2020-04-24 00:00:00', 17, 14291.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Manoel Ribas', 41, 411450, 41022, '22ª RS IVAIPORA', '2020-07-12 00:00:00', 29, 13502.0, 14, 2, 1, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'São Tomé', 41, 412610, 41013, '13ª RS CIANORTE', '2020-06-30 00:00:00', 27, 5722.0, 61, 6, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Cardoso Moreira', 33, 330115, 33007, 'NOROESTE', '2020-06-19 00:00:00', 25, 12823.0, 57, 9, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Tanguá', 33, 330575, 33006, 'METROPOLITANA II', '2020-08-05 00:00:00', 32, 34309.0, 618, 8, 37, 1, ' ', ' ', 1.0], ['Nordeste', 'RN', 'Areia Branca', 24, 240110, 24002, '2ª REGIAO DE SAUDE - MOSSORO', '2020-08-18 00:00:00', 34, 27774.0, 727, 5, 48, 0, ' ', ' ', 0.0], ['Nordeste', 'RN', 'Espírito Santo', 24, 240350, 24001, '1ª REGIAO DE SAUDE - SAO JOSE DE MIPIBU', '2020-05-15 00:00:00', 20, 10505.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Primavera de Rondônia', 11, 110147, 11002, 'CAFE', '2020-04-26 00:00:00', 18, 2856.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Guajará-Mirim', 11, 110010, 11004, 'MADEIRA-MAMORE', '2020-08-06 00:00:00', 32, 46174.0, 2385, 35, 72, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Mucajaí', 14, 140030, 14001, 'CENTRO NORTE', '2020-04-25 00:00:00', 17, 17853.0, 1, 0, 0, 0, ' ', ' ', 1.0], ['Norte', 'RR', 'Mucajaí', 14, 140030, 14001, 'CENTRO NORTE', '2020-07-13 00:00:00', 29, 17853.0, 401, 3, 6, 0, ' ', ' ', 1.0], ['Sul', 'RS', 'Vila Maria', 43, 432340, 43017, 'REGIAO 17', '2020-07-30 00:00:00', 31, 4358.0, 51, 1, 3, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Caçapava do Sul', 43, 430280, 43027, 'REGIAO 27', '2020-08-23 00:00:00', 35, 33624.0, 403, 2, 9, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'São João Batista', 42, 421630, 42007, 'GRANDE FLORIANOPOLIS', '2020-07-03 00:00:00', 27, 37424.0, 135, 18, 2, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Papanduva', 42, 421220, 42012, 'PLANALTO NORTE', '2020-06-22 00:00:00', 26, 19320.0, 20, 0, 4, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Amparo de São Francisco', 28, 280010, 28007, 'PROPRIA', '2020-07-06 00:00:00', 28, 2374.0, 16, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Gracho Cardoso', 28, 280260, 28005, 'NOSSA SENHORA DA GLORIA', '2020-06-19 00:00:00', 25, 5818.0, 31, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Patrocínio Paulista', 35, 353630, 35081, 'TRES COLINAS', '2020-05-30 00:00:00', 22, 14670.0, 6, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Buritama', 35, 350810, 35023, 'CONSORCIOS DO DRS II', '2020-04-14 00:00:00', 16, 17144.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'TO', 'Sítio Novo do Tocantins', 17, 172080, 17002, 'BICO DO PAPAGAIO', '2020-08-14 00:00:00', 33, 9029.0, 177, 9, 4, 0, ' ', ' ', 0.0], ['Norte', 'TO', 'Sucupira', 17, 172085, 17005, 'ILHA DO BANANAL', '2020-04-04 00:00:00', 14, 1966.0, 0, 0, 0, 0, ' ', ' ', 0.0]]
tuplaCovid = (('Norte', 'AC', 'Cruzeiro do Sul', 12, 120020, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-05-14 00:00:00', 20, 88376.0, 144, 19, 1, 0, ' ', ' ', 0.0), ('Norte', 'AC', 'Mâncio Lima', 12, 120033, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-06-02 00:00:00', 23, 18977.0, 26, 1, 1, 1, ' ', ' ', 0.0), ('Nordeste', 'AL', 'Girau do Ponciano', 27, 270290, 27007, '7ª REGIAO DE SAUDE', '2020-07-20 00:00:00', 30, 40917.0, 761, 0, 6, 1, ' ', ' ', 0.0), ('Nordeste', 'AL', 'Boca da Mata', 27, 270100, 27005, '5ª REGIAO DE SAUDE', '2020-05-17 00:00:00', 21, 27281.0, 9, -1, 0, 0, ' ', ' ', 0.0), ('Norte', 'AM', 'Envira', 13, 130150, 13007, 'REGIONAL JURUA', '2020-05-13 00:00:00', 20, 20033.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'AM', 'Atalaia do Norte', 13, 130020, 13009, 'ALTO SOLIMOES', '2020-04-21 00:00:00', 17, 19921.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'AP', 'Mazagão', 16, 160040, 16003, 'AREA SUDOESTE', '2020-04-01 00:00:00', 14, 21632.0, 0, 0, 0, 0, ' ', ' ', 1.0), ('Norte', 'AP', 'Pedra Branca do Amapari', 16, 160015, 16001, 'AREA CENTRAL', '2020-04-06 00:00:00', 15, 16502.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'BA', 'Utinga', 29, 293280, 29011, 'ITABERABA', '2020-06-26 00:00:00', 26, 19178.0, 3, 0, 1, 0, ' ', ' ', 0.0), ('Nordeste', 'BA', 'Planaltino', 29, 292490, 29015, 'JEQUIE', '2020-07-24 00:00:00', 30, 9322.0, 2, 1, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'CE', 'Penaforte', 23, 231060, 23019, '19ª REGIAO BREJO SANTO', '2020-04-25 00:00:00', 17, 9077.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'CE', 'Acaraú', 23, 230020, 23012, '12ª REGIAO ACARAU', '2020-06-24 00:00:00', 26, 62641.0, 1469, 6, 35, 5, ' ', ' ', 0.0), ('Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-07-09 00:00:00', 28, 3015268.0, 65677, 1363, 823, 22, ' ', ' ', 1.0), ('Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-04-07 00:00:00', 15, 3015268.0, 492, 19, 12, 2, ' ', ' ', 1.0), ('Sudeste', 'ES', 'São Domingos do Norte', 32, 320465, 32001, 'CENTRAL', '2020-08-16 00:00:00', 34, 8638.0, 232, 0, 8, 0, ' ', ' ', 0.0), ('Sudeste', 'ES', 'Pedro Canário', 32, 320405, 32003, 'NORTE', '2020-06-27 00:00:00', 26, 26184.0, 147, 0, 4, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'GO', 'Piracanjuba', 52, 521710, 52002, 'CENTRO SUL', '2020-06-03 00:00:00', 23, 24524.0, 15, 0, 1, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'GO', 'Campos Belos', 52, 520490, 52006, 'NORDESTE I', '2020-08-21 00:00:00', 34, 19887.0, 135, 0, 3, 0, ' ', ' ', 0.0), ('Nordeste', 'MA', 'Pastos Bons', 21, 210800, 21015, 'SAO JOAO DOS PATOS', '2020-07-07 00:00:00', 28, 19472.0, 41, 0, 1, 0, ' ', ' ', 0.0), ('Nordeste', 'MA', 'Peritoró', 21, 210845, 21007, 'CODO', '2020-08-21 00:00:00', 34, 23196.0, 329, 0, 3, 0, ' ', ' ', 0.0), ('Sudeste', 'MG', 'Aiuruoca', 31, 310120, 31008, 'SAO LOURENCO', '2020-06-15 00:00:00', 25, 6003.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'MG', 'Santa Cruz de Minas', 31, 315733, 31015, 'SAO JOAO DEL REI', '2020-04-15 00:00:00', 16, 8604.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MS', 'Brasilândia', 50, 500230, 50004, 'TRES LAGOAS', '2020-04-12 00:00:00', 16, 11872.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MS', 'Sete Quedas', 50, 500770, 50003, 'DOURADOS', '2020-05-29 00:00:00', 22, 10791.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MT', 'Colniza', 51, 510325, 51008, 'NOROESTE MATOGROSSENSE', '2020-08-06 00:00:00', 32, 38582.0, 44, 2, 1, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MT', 'Ribeirão Cascalheira', 51, 510718, 51006, 'MEDIO ARAGUAIA', '2020-07-27 00:00:00', 31, 10206.0, 101, 0, 7, 1, ' ', ' ', 0.0), ('Norte', 'PA', 'Capitão Poço', 15, 150230, 15008, 'METROPOLITANA III', '2020-04-07 00:00:00', 15, 54303.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'PA', 'Igarapé-Miri', 15, 150330, 15011, 'TOCANTINS', '2020-05-17 00:00:00', 21, 62698.0, 134, 20, 5, 0, ' ', ' ', 0.0), ('Nordeste', 'PB', 'Areia', 25, 250110, 25003, '3ª REGIAO', '2020-08-24 00:00:00', 35, 22819.0, 411, 0, 3, 0, ' ', ' ', 0.0), ('Nordeste', 'PB', 'Cachoeira dos Índios', 25, 250330, 25009, '9ª REGIAO', '2020-05-23 00:00:00', 21, 10244.0, 3, 1, 1, 0, ' ', ' ', 0.0), ('Nordeste', 'PE', 'Ferreiros', 26, 260550, 26005, 'GOIANA', '2020-06-12 00:00:00', 24, 12123.0, 74, 0, 5, 0, ' ', ' ', 0.0), ('Nordeste', 'PE', 'Escada', 26, 260520, 26008, 'PALMARES', '2020-06-25 00:00:00', 26, 68875.0, 207, 1, 22, 0, ' ', ' ', 0.0), ('Nordeste', 'PI', 'Pedro Laurentino', 22, 220793, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-05-28 00:00:00', 22, 2536.0, 1, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'PI', 'São Pedro do Piauí', 22, 221050, 22004, 'ENTRE RIOS', '2020-04-24 00:00:00', 17, 14291.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Sul', 'PR', 'Manoel Ribas', 41, 411450, 41022, '22ª RS IVAIPORA', '2020-07-12 00:00:00', 29, 13502.0, 14, 2, 1, 0, ' ', ' ', 0.0), ('Sul', 'PR', 'São Tomé', 41, 412610, 41013, '13ª RS CIANORTE', '2020-06-30 00:00:00', 27, 5722.0, 61, 6, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'RJ', 'Cardoso Moreira', 33, 330115, 33007, 'NOROESTE', '2020-06-19 00:00:00', 25, 12823.0, 57, 9, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'RJ', 'Tanguá', 33, 330575, 33006, 'METROPOLITANA II', '2020-08-05 00:00:00', 32, 34309.0, 618, 8, 37, 1, ' ', ' ', 1.0), ('Nordeste', 'RN', 'Areia Branca', 24, 240110, 24002, '2ª REGIAO DE SAUDE - MOSSORO', '2020-08-18 00:00:00', 34, 27774.0, 727, 5, 48, 0, ' ', ' ', 0.0), ('Nordeste', 'RN', 'Espírito Santo', 24, 240350, 24001, '1ª REGIAO DE SAUDE - SAO JOSE DE MIPIBU', '2020-05-15 00:00:00', 20, 10505.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'RO', 'Primavera de Rondônia', 11, 110147, 11002, 'CAFE', '2020-04-26 00:00:00', 18, 2856.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'RO', 'Guajará-Mirim', 11, 110010, 11004, 'MADEIRA-MAMORE', '2020-08-06 00:00:00', 32, 46174.0, 2385, 35, 72, 0, ' ', ' ', 0.0), ('Norte', 'RR', 'Mucajaí', 14, 140030, 14001, 'CENTRO NORTE', '2020-04-25 00:00:00', 17, 17853.0, 1, 0, 0, 0, ' ', ' ', 1.0), ('Norte', 'RR', 'Mucajaí', 14, 140030, 14001, 'CENTRO NORTE', '2020-07-13 00:00:00', 29, 17853.0, 401, 3, 6, 0, ' ', ' ', 1.0), ('Sul', 'RS', 'Vila Maria', 43, 432340, 43017, 'REGIAO 17', '2020-07-30 00:00:00', 31, 4358.0, 51, 1, 3, 0, ' ', ' ', 0.0), ('Sul', 'RS', 'Caçapava do Sul', 43, 430280, 43027, 'REGIAO 27', '2020-08-23 00:00:00', 35, 33624.0, 403, 2, 9, 0, ' ', ' ', 0.0), ('Sul', 'SC', 'São João Batista', 42, 421630, 42007, 'GRANDE FLORIANOPOLIS', '2020-07-03 00:00:00', 27, 37424.0, 135, 18, 2, 0, ' ', ' ', 0.0), ('Sul', 'SC', 'Papanduva', 42, 421220, 42012, 'PLANALTO NORTE', '2020-06-22 00:00:00', 26, 19320.0, 20, 0, 4, 0, ' ', ' ', 0.0), ('Nordeste', 'SE', 'Amparo de São Francisco', 28, 280010, 28007, 'PROPRIA', '2020-07-06 00:00:00', 28, 2374.0, 16, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'SE', 'Gracho Cardoso', 28, 280260, 28005, 'NOSSA SENHORA DA GLORIA', '2020-06-19 00:00:00', 25, 5818.0, 31, 0, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'SP', 'Patrocínio Paulista', 35, 353630, 35081, 'TRES COLINAS', '2020-05-30 00:00:00', 22, 14670.0, 6, 0, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'SP', 'Buritama', 35, 350810, 35023, 'CONSORCIOS DO DRS II', '2020-04-14 00:00:00', 16, 17144.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'TO', 'Sítio Novo do Tocantins', 17, 172080, 17002, 'BICO DO PAPAGAIO', '2020-08-14 00:00:00', 33, 9029.0, 177, 9, 4, 0, ' ', ' ', 0.0), ('Norte', 'TO', 'Sucupira', 17, 172085, 17005, 'ILHA DO BANANAL', '2020-04-04 00:00:00', 14, 1966.0, 0, 0, 0, 0, ' ', ' ', 0.0))

#Letra b) 
#lista com o número de casos acumulados para o estado do Rio de Janeiro
listaCovid.sort() 
print ("O número de casos acumulados da lista referente ao estado do Rio de Janeiro é de: ", (listaCovid[44][10] + listaCovid[45][10])) 

#tupla com o número de casos acumulados para o estado do Rio de Janeiro
print ("O número de casos acumulados da tupla referente ao estado do Rio de Janeiro é de: ", (tuplaCovid[36][10] + tuplaCovid[37][10]))

#Letra c)
#lista 

listaCovid = [['Norte', 'AC', 'Cruzeiro do Sul', 12, 120020, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-05-14 00:00:00', 20, 88376.0, 144, 19, 1, 0, ' ', ' ', 0.0], ['Norte', 'AC', 'Mâncio Lima', 12, 120033, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-06-02 00:00:00', 23, 18977.0, 26, 1, 1, 1, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Girau do Ponciano', 27, 270290, 27007, '7ª REGIAO DE SAUDE', '2020-07-20 00:00:00', 30, 40917.0, 761, 0, 6, 1, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Boca da Mata', 27, 270100, 27005, '5ª REGIAO DE SAUDE', '2020-05-17 00:00:00', 21, 27281.0, 9, -1, 0, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Envira', 13, 130150, 13007, 'REGIONAL JURUA', '2020-05-13 00:00:00', 20, 20033.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Atalaia do Norte', 13, 130020, 13009, 'ALTO SOLIMOES', '2020-04-21 00:00:00', 17, 19921.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'AP', 'Mazagão', 16, 160040, 16003, 'AREA SUDOESTE', '2020-04-01 00:00:00', 14, 21632.0, 0, 0, 0, 0, ' ', ' ', 1.0], ['Norte', 'AP', 'Pedra Branca do Amapari', 16, 160015, 16001, 'AREA CENTRAL', '2020-04-06 00:00:00', 15, 16502.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'Utinga', 29, 293280, 29011, 'ITABERABA', '2020-06-26 00:00:00', 26, 19178.0, 3, 0, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'Planaltino', 29, 292490, 29015, 'JEQUIE', '2020-07-24 00:00:00', 30, 9322.0, 2, 1, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Penaforte', 23, 231060, 23019, '19ª REGIAO BREJO SANTO', '2020-04-25 00:00:00', 17, 9077.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Acaraú', 23, 230020, 23012, '12ª REGIAO ACARAU', '2020-06-24 00:00:00', 26, 62641.0, 1469, 6, 35, 5, ' ', ' ', 0.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-07-09 00:00:00', 28, 3015268.0, 65677, 1363, 823, 22, ' ', ' ', 1.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-04-07 00:00:00', 15, 3015268.0, 492, 19, 12, 2, ' ', ' ', 1.0], ['Sudeste', 'ES', 'São Domingos do Norte', 32, 320465, 32001, 'CENTRAL', '2020-08-16 00:00:00', 34, 8638.0, 232, 0, 8, 0, ' ', ' ', 0.0], ['Sudeste', 'ES', 'Pedro Canário', 32, 320405, 32003, 'NORTE', '2020-06-27 00:00:00', 26, 26184.0, 147, 0, 4, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Piracanjuba', 52, 521710, 52002, 'CENTRO SUL', '2020-06-03 00:00:00', 23, 24524.0, 15, 0, 1, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Campos Belos', 52, 520490, 52006, 'NORDESTE I', '2020-08-21 00:00:00', 34, 19887.0, 135, 0, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Pastos Bons', 21, 210800, 21015, 'SAO JOAO DOS PATOS', '2020-07-07 00:00:00', 28, 19472.0, 41, 0, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Peritoró', 21, 210845, 21007, 'CODO', '2020-08-21 00:00:00', 34, 23196.0, 329, 0, 3, 0, ' ', ' ', 0.0], ['Sudeste', 'MG', 'Aiuruoca', 31, 310120, 31008, 'SAO LOURENCO', '2020-06-15 00:00:00', 25, 6003.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'MG', 'Santa Cruz de Minas', 31, 315733, 31015, 'SAO JOAO DEL REI', '2020-04-15 00:00:00', 16, 8604.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Brasilândia', 50, 500230, 50004, 'TRES LAGOAS', '2020-04-12 00:00:00', 16, 11872.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Sete Quedas', 50, 500770, 50003, 'DOURADOS', '2020-05-29 00:00:00', 22, 10791.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Colniza', 51, 510325, 51008, 'NOROESTE MATOGROSSENSE', '2020-08-06 00:00:00', 32, 38582.0, 44, 2, 1, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Ribeirão Cascalheira', 51, 510718, 51006, 'MEDIO ARAGUAIA', '2020-07-27 00:00:00', 31, 10206.0, 101, 0, 7, 1, ' ', ' ', 0.0], ['Norte', 'PA', 'Capitão Poço', 15, 150230, 15008, 'METROPOLITANA III', '2020-04-07 00:00:00', 15, 54303.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Igarapé-Miri', 15, 150330, 15011, 'TOCANTINS', '2020-05-17 00:00:00', 21, 62698.0, 134, 20, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Areia', 25, 250110, 25003, '3ª REGIAO', '2020-08-24 00:00:00', 35, 22819.0, 411, 0, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Cachoeira dos Índios', 25, 250330, 25009, '9ª REGIAO', '2020-05-23 00:00:00', 21, 10244.0, 3, 1, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Ferreiros', 26, 260550, 26005, 'GOIANA', '2020-06-12 00:00:00', 24, 12123.0, 74, 0, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Escada', 26, 260520, 26008, 'PALMARES', '2020-06-25 00:00:00', 26, 68875.0, 207, 1, 22, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Pedro Laurentino', 22, 220793, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2020-05-28 00:00:00', 22, 2536.0, 1, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'São Pedro do Piauí', 22, 221050, 22004, 'ENTRE RIOS', '2020-04-24 00:00:00', 17, 14291.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Manoel Ribas', 41, 411450, 41022, '22ª RS IVAIPORA', '2020-07-12 00:00:00', 29, 13502.0, 14, 2, 1, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'São Tomé', 41, 412610, 41013, '13ª RS CIANORTE', '2020-06-30 00:00:00', 27, 5722.0, 61, 6, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Cardoso Moreira', 33, 330115, 33007, 'NOROESTE', '2020-06-19 00:00:00', 25, 12823.0, 57, 9, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Tanguá', 33, 330575, 33006, 'METROPOLITANA II', '2020-08-05 00:00:00', 32, 34309.0, 618, 8, 37, 1, ' ', ' ', 1.0], ['Nordeste', 'RN', 'Areia Branca', 24, 240110, 24002, '2ª REGIAO DE SAUDE - MOSSORO', '2020-08-18 00:00:00', 34, 27774.0, 727, 5, 48, 0, ' ', ' ', 0.0], ['Nordeste', 'RN', 'Espírito Santo', 24, 240350, 24001, '1ª REGIAO DE SAUDE - SAO JOSE DE MIPIBU', '2020-05-15 00:00:00', 20, 10505.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Primavera de Rondônia', 11, 110147, 11002, 'CAFE', '2020-04-26 00:00:00', 18, 2856.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Guajará-Mirim', 11, 110010, 11004, 'MADEIRA-MAMORE', '2020-08-06 00:00:00', 32, 46174.0, 2385, 35, 72, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Mucajaí', 14, 140030, 14001, 'CENTRO NORTE', '2020-04-25 00:00:00', 17, 17853.0, 1, 0, 0, 0, ' ', ' ', 1.0], ['Norte', 'RR', 'Mucajaí', 14, 140030, 14001, 'CENTRO NORTE', '2020-07-13 00:00:00', 29, 17853.0, 401, 3, 6, 0, ' ', ' ', 1.0], ['Sul', 'RS', 'Vila Maria', 43, 432340, 43017, 'REGIAO 17', '2020-07-30 00:00:00', 31, 4358.0, 51, 1, 3, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Caçapava do Sul', 43, 430280, 43027, 'REGIAO 27', '2020-08-23 00:00:00', 35, 33624.0, 403, 2, 9, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'São João Batista', 42, 421630, 42007, 'GRANDE FLORIANOPOLIS', '2020-07-03 00:00:00', 27, 37424.0, 135, 18, 2, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Papanduva', 42, 421220, 42012, 'PLANALTO NORTE', '2020-06-22 00:00:00', 26, 19320.0, 20, 0, 4, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Amparo de São Francisco', 28, 280010, 28007, 'PROPRIA', '2020-07-06 00:00:00', 28, 2374.0, 16, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Gracho Cardoso', 28, 280260, 28005, 'NOSSA SENHORA DA GLORIA', '2020-06-19 00:00:00', 25, 5818.0, 31, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Patrocínio Paulista', 35, 353630, 35081, 'TRES COLINAS', '2020-05-30 00:00:00', 22, 14670.0, 6, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Buritama', 35, 350810, 35023, 'CONSORCIOS DO DRS II', '2020-04-14 00:00:00', 16, 17144.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'TO', 'Sítio Novo do Tocantins', 17, 172080, 17002, 'BICO DO PAPAGAIO', '2020-08-14 00:00:00', 33, 9029.0, 177, 9, 4, 0, ' ', ' ', 0.0], ['Norte', 'TO', 'Sucupira', 17, 172085, 17005, 'ILHA DO BANANAL', '2020-04-04 00:00:00', 14, 1966.0, 0, 0, 0, 0, ' ', ' ', 0.0]]

obitosacumuladosACl = (listaCovid[0][12] + listaCovid[1][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do ACRE é de:", obitosacumuladosACl)

obitosacumuladosALl = (listaCovid[2][12] + listaCovid[3][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado de ALAGOAS é de:", obitosacumuladosALl)

obitosacumuladosAMl = (listaCovid[4][12] + listaCovid[5][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado de AMAZONAS é de:", obitosacumuladosAMl)

obitosacumuladosAPl = (listaCovid[6][12] + listaCovid[7][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do AMAPÁ é de:", obitosacumuladosAPl)

obitosacumuladosBAl = (listaCovid[8][12] + listaCovid[9][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado da BAHIA é de:", obitosacumuladosBAl)

obitosacumuladosCEl = (listaCovid[10][12] + listaCovid[11][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do CEARÁ é de:", obitosacumuladosCEl)

obitosacumuladosDFl = (listaCovid[12][12] + listaCovid[13][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do DISTRITO FEDERAL é de:", obitosacumuladosDFl)

obitosacumuladosESl = (listaCovid[14][12] + listaCovid[15][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do ESPIRITO SANTO é de:", obitosacumuladosESl)

obitosacumuladosGOl = (listaCovid[16][12] + listaCovid[17][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado de GOIÁS é de:", obitosacumuladosGOl)

obitosacumuladosMAl = (listaCovid[18][12] + listaCovid[19][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do MARANHÃO é de:", obitosacumuladosMAl)

obitosacumuladosMGl = (listaCovid[20][12] + listaCovid[21][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado de MINAS GERAIS é de:", obitosacumuladosMGl)

obitosacumuladosMSl = (listaCovid[22][12] + listaCovid[23][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do MATO GROSSO DO SUL é de:", obitosacumuladosMSl)

obitosacumuladosMTl = (listaCovid[24][12] + listaCovid[25][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do MATO GROSSO é de:", obitosacumuladosMTl)

obitosacumuladosPAl = (listaCovid[26][12] + listaCovid[27][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do PARÁ é de:", obitosacumuladosPAl)

obitosacumuladosPBl = (listaCovid[28][12] + listaCovid[29][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado da PARAÍBA é de:", obitosacumuladosPBl)

obitosacumuladosPEl = (listaCovid[30][12] + listaCovid[31][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do PERNAMBUCO é de:", obitosacumuladosPEl)

obitosacumuladosPIl = (listaCovid[32][12] + listaCovid[33][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do PIAUÍ é de:", obitosacumuladosPIl)

obitosacumuladosPRl = (listaCovid[34][12] + listaCovid[35][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do PARANÁ é de:", obitosacumuladosPRl)

obitosacumuladosRJl = (listaCovid[36][12] + listaCovid[37][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do RIO DE JANEIRO é de:", obitosacumuladosRJl)

obitosacumuladosRNl = (listaCovid[38][12] + listaCovid[39][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do RIO GRANDE DO NORTE é de:", obitosacumuladosRNl)

obitosacumuladosROl = (listaCovid[40][12] + listaCovid[41][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado de RONDÔNIA é de:", obitosacumuladosROl)

obitosacumuladosRRl = (listaCovid[42][12] + listaCovid[43][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado de RORAIMA é de:", obitosacumuladosRRl)

obitosacumuladosRSl = (listaCovid[44][12] + listaCovid[45][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do RIO GRANDE DO SUL é de:", obitosacumuladosRSl)

obitosacumuladosSCl = (listaCovid[46][12] + listaCovid[47][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado de SANTA CATARINA é de:", obitosacumuladosSCl)

obitosacumuladosSEl = (listaCovid[48][12] + listaCovid[49][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado de SERGIPE é de:", obitosacumuladosSEl)

obitosacumuladosSPl = (listaCovid[50][12] + listaCovid[51][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado de SÃO PAULO é de:", obitosacumuladosSPl)

obitosacumuladosTOl = (listaCovid[52][12] + listaCovid[53][12])
print ("De acordo com a lista, o número de óbitos acumuldados do estado do TOCANTINS é de:", obitosacumuladosTOl)


#tupla
obitosacumuladosACt = (tuplaCovid[0][12] + tuplaCovid[1][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do ACRE é de:", obitosacumuladosACt)

obitosacumuladosALt = (tuplaCovid[2][12] + tuplaCovid[3][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado de ALAGOAS é de:", obitosacumuladosALt)

obitosacumuladosAMt = (tuplaCovid[4][12] + tuplaCovid[5][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado de AMAZONAS é de:", obitosacumuladosAMt)

obitosacumuladosAPt = (tuplaCovid[6][12] + tuplaCovid[7][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do AMAPÁ é de:", obitosacumuladosAPt)

obitosacumuladosBAt = (tuplaCovid[8][12] + tuplaCovid[9][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado da BAHIA é de:", obitosacumuladosBAt)

obitosacumuladosCEt = (tuplaCovid[10][12] + tuplaCovid[11][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do CEARÁ é de:", obitosacumuladosCEt)

obitosacumuladosDFt = (tuplaCovid[12][12] + tuplaCovid[13][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do DISTRITO FEDERAL é de:", obitosacumuladosDFt)

obitosacumuladosESt = (tuplaCovid[14][12] + tuplaCovid[15][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do ESPIRITO SANTO é de:", obitosacumuladosESt)

obitosacumuladosGOt = (tuplaCovid[16][12] + tuplaCovid[17][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado de GOIÁS é de:", obitosacumuladosGOt)

obitosacumuladosMAt = (tuplaCovid[18][12] + tuplaCovid[19][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do MARANHÃO é de:", obitosacumuladosMAt)

obitosacumuladosMGt = (tuplaCovid[20][12] + tuplaCovid[21][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado de MINAS GERAIS é de:", obitosacumuladosMGt)

obitosacumuladosMSt = (tuplaCovid[22][12] + tuplaCovid[23][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do MATO GROSSO DO SUL é de:", obitosacumuladosMSt)

obitosacumuladosMTt = (tuplaCovid[24][12] + tuplaCovid[25][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do MATO GROSSO é de:", obitosacumuladosMTt)

obitosacumuladosPAt = (tuplaCovid[26][12] + tuplaCovid[27][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do PARÁ é de:", obitosacumuladosPAt)

obitosacumuladosPBt = (tuplaCovid[28][12] + tuplaCovid[29][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado da PARAÍBA é de:", obitosacumuladosPBt)

obitosacumuladosPEt = (tuplaCovid[30][12] + tuplaCovid[31][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do PERNAMBUCO é de:", obitosacumuladosPEt)

obitosacumuladosPIt = (tuplaCovid[32][12] + tuplaCovid[33][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do PIAUÍ é de:", obitosacumuladosPIt)

obitosacumuladosPRt = (tuplaCovid[34][12] + tuplaCovid[35][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do PARANÁ é de:", obitosacumuladosPRt)

obitosacumuladosRJt = (tuplaCovid[36][12] + tuplaCovid[37][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do RIO DE JANEIRO é de:", obitosacumuladosRJt)

obitosacumuladosRNt = (tuplaCovid[38][12] + tuplaCovid[39][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do RIO GRANDE DO NORTE é de:", obitosacumuladosRNt)

obitosacumuladosROt = (tuplaCovid[40][12] + tuplaCovid[41][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado de RONDÔNIA é de:", obitosacumuladosROt)

obitosacumuladosRRt = (tuplaCovid[42][12] + tuplaCovid[43][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado de RORAIMA é de:", obitosacumuladosRRt)

obitosacumuladosRSt = (tuplaCovid[44][12] + tuplaCovid[45][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do RIO GRANDE DO SUL é de:", obitosacumuladosRSt)

obitosacumuladosSCt = (tuplaCovid[46][12] + tuplaCovid[47][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado de SANTA CATARINA é de:", obitosacumuladosSCt)

obitosacumuladosSEt = (tuplaCovid[48][12] + tuplaCovid[49][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado de SERGIPE é de:", obitosacumuladosSEt)

obitosacumuladosSPt = (tuplaCovid[50][12] + tuplaCovid[51][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado de SÃO PAULO é de:", obitosacumuladosSPt)

obitosacumuladosTOt = (tuplaCovid[52][12] + tuplaCovid[53][12])
print ("De acordo com a tupla, o número de óbitos acumuldados do estado do TOCANTINS é de:", obitosacumuladosTOt)

#Letra d)
#Lista
obitosanovosPBl = (listaCovid[28][13] + listaCovid[29][13])
print ("De acordo com a lista, o número de óbitos novos do estado da PARAÍBA é de:",obitosanovosPBl,", e esse valor está incorreto!")

listaCovid.pop(28)
listaCovid.pop(29)

listaCovid.insert (28, ['Nordeste', 'PB', 'Areia', 25, 250110, 25003, '3ª REGIAO', '2020-08-24 00:00:00', 35, 22819.0, 411, 0, 3, 4, ' ', ' ', 0.0])
listaCovid.insert (29, ['Nordeste', 'PB', 'Cachoeira dos Índios', 25, 250330, 25009, '9ª REGIAO', '2020-05-23 00:00:00', 21, 10244.0, 3, 1, 1, 11, ' ', ' ', 0.0])

obitosanovosPBlat = (listaCovid[28][13] + listaCovid[29][13])
print ("O valor atualizado da lista, referente ao número de óbitos novos do estado da PARAÍBA é de:",obitosanovosPBlat,"!")

#tupla
#Obs: Não é possível alterar dados de uma tupla.


obitosanovosPBt = (tuplaCovid[28][13] + tuplaCovid[29][13])
print ("De acordo com a lista, o número de óbitos novos do estado da PARAÍBA é de:",obitosanovosPBt,", e esse valor está incorreto!")

tuplaCovid.pop(28)
tuplaCovid.pop(29)

tuplaCovid.insert (28, ['Nordeste', 'PB', 'Areia', 25, 250110, 25003, '3ª REGIAO', '2020-08-24 00:00:00', 35, 22819.0, 411, 0, 3, 4, ' ', ' ', 0.0])
tuplaCovid.insert (29, ['Nordeste', 'PB', 'Cachoeira dos Índios', 25, 250330, 25009, '9ª REGIAO', '2020-05-23 00:00:00', 21, 10244.0, 3, 1, 1, 11, ' ', ' ', 0.0])

obitosanovosPBtat = (tuplaCovid[28][13] + tuplaCovid[29][13])
print ("O valor atualizado da lista, referente ao número de óbitos novos do estado da PARAÍBA é de:",obitosanovosPBlat,"!")

#Letra e) Questão respondida através de um print e anexado na pasta da atividade 5

#Letra f) 

NovaListaCovid = [['Norte', 'AP', 'Serra do Navio', 16, 160005, 16001, 'AREA CENTRAL', '29-08-2020', 35, 5397, 622, 0, 4, 0, ' ', ' ', 0], 
['Norte', 'AP', 'Amapá', 16, 160010, 16002, 'AREA NORTE', '29/08/2020', 35, 9109, 484, 0, 4, 0, ' ', ' ', 0],
['Norte', 'AP', 'Pedra Branca do Amapari', 16, 160015, 16001, 'AREA CENTRAL', '29/08/2020', 35, 16502, 2526, 4, 5, 0, ' ', ' ', 0],
['Norte', 'AP', 'Calçoene', 16, 160020, 16002, 'AREA NORTE', '29/08/2020', 35, 11117, 1126, 0, 5, 0, ' ', ' ', 0],
['Norte', 'AP', 'Cutias', 16, 160021, 16001, 'AREA CENTRAL', '29/08/2020', 35, 5983, 522, 0, 2, 0, ' ', ' ', 0],
['Norte', 'AP', 'Ferreira Gomes', 16, 160023, 16001, 'AREA CENTRAL', '29/08/2020', 35, 7780, 539, 0, 3, 0, ' ', ' ', 0],
['Norte', 'AP', 'Itaubal', 16, 160025, 16001, 'AREA CENTRAL', '29/08/2020', 35, 5503, 286, 0, 0, 0, ' ', ' ', 0],
['Norte', 'AP', 'Laranjal do Jari', 16, 160027, 16003, 'AREA SUDOESTE', '29/08/2020', 35, 50410, 4283, 0, 44, 0, ' ', ' ', 0],
['Norte', 'AP', 'Macapá', 16, 160030, 16001, 'AREA CENTRAL', '29/08/2020', 35, 503327, 17134, 34, 446, 1, ' ', ' ', 1],
['Norte', 'AP', 'Mazagão', 16, 160040, 16003, 'AREA SUDOESTE', '29/08/2020', 35, 21632, 1354, 0, 8, 0, ' ', ' ', 1],
['Norte', 'AP', 'Oiapoque', 16, 160050, 16002, 'AREA NORTE', '29/08/2020', 35, 27270, 2510, 2, 20, 0, ' ', ' ', 0],
['Norte', 'AP', 'Porto Grande', 16, 160053, 16001, 'AREA CENTRAL', '29/08/2020', 35, 21971, 1098, 2, 13, 0, ' ', ' ', 0],
['Norte', 'AP', 'Pracuúba', 16, 160055, 16002, 'AREA NORTE', '29/08/2020', 35, 5120, 350, 0, 6, 1, ' ', ' ', 0],
['Norte', 'AP', 'Santana', 16, 160060, 16003, 'AREA SUDOESTE', '29/08/2020', 35, 121364, 6877, 99, 82, 0, ' ', ' ', 1],
['Norte', 'AP', 'Tartarugalzinho', 16, 160070, 16002, 'AREA NORTE', '29/08/2020', 35, 17315, 992, 5, 4, 0, ' ', ' ', 0],
['Norte', 'AP', 'Vitória do Jari', 16, 160080, 16003, 'AREA SUDOESTE', '29/08/2020', 35, 15931, 2068, 0, 13, 0, ' ', ' ', 0]]

print (NovaListaCovid)

listaCovid.append (NovaListaCovid)

print (listaCovid)

#Letra g)
listaCovid[0].pop(5) 
listaCovid[0].pop(5) 
listaCovid[1].pop(5) 
listaCovid[1].pop(5)
listaCovid[2].pop(5) 
listaCovid[2].pop(5) 
listaCovid[3].pop(5) 
listaCovid[3].pop(5) 
listaCovid[4].pop(5) 
listaCovid[4].pop(5) 
listaCovid[5].pop(5) 
listaCovid[5].pop(5) 
listaCovid[6].pop(5) 
listaCovid[6].pop(5) 
listaCovid[7].pop(5) 
listaCovid[7].pop(5) 
listaCovid[8].pop(5) 
listaCovid[8].pop(5) 
listaCovid[9].pop(5) 
listaCovid[9].pop(5) 
listaCovid[10].pop(5) 
listaCovid[10].pop(5) 
listaCovid[11].pop(5) 
listaCovid[11].pop(5) 
listaCovid[12].pop(5) 
listaCovid[12].pop(5) 
listaCovid[13].pop(5) 
listaCovid[13].pop(5) 
listaCovid[14].pop(5) 
listaCovid[14].pop(5) 
listaCovid[15].pop(5) 
listaCovid[15].pop(5) 
listaCovid[16].pop(5) 
listaCovid[16].pop(5) 
listaCovid[17].pop(5) 
listaCovid[17].pop(5) 
listaCovid[18].pop(5) 
listaCovid[18].pop(5) 
listaCovid[19].pop(5) 
listaCovid[19].pop(5) 
listaCovid[20].pop(5) 
listaCovid[20].pop(5) 
listaCovid[21].pop(5) 
listaCovid[21].pop(5) 
listaCovid[22].pop(5) 
listaCovid[22].pop(5) 
listaCovid[23].pop(5) 
listaCovid[23].pop(5) 
listaCovid[24].pop(5) 
listaCovid[24].pop(5) 
listaCovid[25].pop(5) 
listaCovid[25].pop(5) 
listaCovid[26].pop(5) 
listaCovid[26].pop(5) 
listaCovid[27].pop(5) 
listaCovid[27].pop(5) 
listaCovid[28].pop(5) 
listaCovid[28].pop(5) 
listaCovid[29].pop(5) 
listaCovid[29].pop(5) 
listaCovid[30].pop(5) 
listaCovid[30].pop(5) 
listaCovid[31].pop(5) 
listaCovid[31].pop(5) 
listaCovid[32].pop(5) 
listaCovid[32].pop(5) 
listaCovid[33].pop(5) 
listaCovid[33].pop(5) 
listaCovid[34].pop(5) 
listaCovid[34].pop(5) 
listaCovid[35].pop(5) 
listaCovid[35].pop(5) 
listaCovid[36].pop(5) 
listaCovid[36].pop(5) 
listaCovid[37].pop(5) 
listaCovid[37].pop(5) 
listaCovid[38].pop(5) 
listaCovid[38].pop(5) 
listaCovid[39].pop(5) 
listaCovid[39].pop(5) 
listaCovid[40].pop(5) 
listaCovid[40].pop(5) 
listaCovid[41].pop(5) 
listaCovid[41].pop(5) 
listaCovid[42].pop(5) 
listaCovid[42].pop(5) 
listaCovid[43].pop(5) 
listaCovid[43].pop(5) 
listaCovid[44].pop(5) 
listaCovid[44].pop(5) 
listaCovid[45].pop(5) 
listaCovid[45].pop(5) 
listaCovid[46].pop(5) 
listaCovid[46].pop(5) 
listaCovid[47].pop(5) 
listaCovid[47].pop(5) 
listaCovid[48].pop(5) 
listaCovid[48].pop(5) 
listaCovid[49].pop(5) 
listaCovid[49].pop(5) 
listaCovid[50].pop(5) 
listaCovid[50].pop(5) 
listaCovid[51].pop(5) 
listaCovid[51].pop(5) 
listaCovid[52].pop(5) 
listaCovid[52].pop(5) 
listaCovid[53].pop(5) 
listaCovid[53].pop(5) 

print (listaCovid)


#Letra h)



SomaDadosPopulacao = (NovaListaCovid[0][9]) + (NovaListaCovid[1][9]) + (NovaListaCovid[2][9]) + (NovaListaCovid[3][9]) + (NovaListaCovid[4][9]) + (NovaListaCovid[5][9]) + (NovaListaCovid[6][9]) + (NovaListaCovid[7][9]) + (NovaListaCovid[8][9]) + (NovaListaCovid[9][9]) + (NovaListaCovid[10][9]) + (NovaListaCovid[11][9]) + (NovaListaCovid[12][9]) + (NovaListaCovid[13][9]) + (NovaListaCovid[14][9]) + (NovaListaCovid[15][9]) 
print (SomaDadosPopulacao)
ListaComparacao = [SomaDadosPopulacao]
print (ListaComparacao)
print (1691462 in ListaComparacao)

SomaDadosCasosAcumulados = (NovaListaCovid[0][10]) + (NovaListaCovid[1][10]) + (NovaListaCovid[2][10]) + (NovaListaCovid[3][10]) + (NovaListaCovid[4][10]) + (NovaListaCovid[5][10]) + (NovaListaCovid[6][10]) + (NovaListaCovid[7][10]) + (NovaListaCovid[8][10]) + (NovaListaCovid[9][10]) + (NovaListaCovid[10][10]) + (NovaListaCovid[11][10]) + (NovaListaCovid[12][10]) + (NovaListaCovid[13][10]) + (NovaListaCovid[14][10]) + (NovaListaCovid[15][10]) 
print (SomaDadosCasosAcumulados)
ListaComparacao.append (SomaDadosCasosAcumulados)
print (ListaComparacao)
print (79914 in ListaComparacao)

SomaDadosCasosNovos = (NovaListaCovid[0][11]) + (NovaListaCovid[1][11]) + (NovaListaCovid[2][11]) + (NovaListaCovid[3][11]) + (NovaListaCovid[4][11]) + (NovaListaCovid[5][11]) + (NovaListaCovid[6][11]) + (NovaListaCovid[7][11]) + (NovaListaCovid[8][11]) + (NovaListaCovid[9][11]) + (NovaListaCovid[10][11]) + (NovaListaCovid[11][11]) + (NovaListaCovid[12][11]) + (NovaListaCovid[13][11]) + (NovaListaCovid[14][11]) + (NovaListaCovid[15][11]) 
print (SomaDadosCasosNovos)
ListaComparacao.append (SomaDadosCasosNovos)
print (ListaComparacao)
print (508 in ListaComparacao)

SomaDadosObidosAcumulados = (NovaListaCovid[0][12]) + (NovaListaCovid[1][12]) + (NovaListaCovid[2][12]) + (NovaListaCovid[3][12]) + (NovaListaCovid[4][12]) + (NovaListaCovid[5][12]) + (NovaListaCovid[6][12]) + (NovaListaCovid[7][12]) + (NovaListaCovid[8][12]) + (NovaListaCovid[9][12]) + (NovaListaCovid[10][12]) + (NovaListaCovid[11][12]) + (NovaListaCovid[12][12]) + (NovaListaCovid[13][12]) + (NovaListaCovid[14][12]) + (NovaListaCovid[15][12]) 
print (SomaDadosObidosAcumulados)
ListaComparacao.append (SomaDadosObidosAcumulados)
print (ListaComparacao)
print (508 in ListaComparacao)

SomaDadosObidosNovos = (NovaListaCovid[0][13]) + (NovaListaCovid[1][13]) + (NovaListaCovid[2][13]) + (NovaListaCovid[3][13]) + (NovaListaCovid[4][13]) + (NovaListaCovid[5][13]) + (NovaListaCovid[6][13]) + (NovaListaCovid[7][13]) + (NovaListaCovid[8][13]) + (NovaListaCovid[9][13]) + (NovaListaCovid[10][13]) + (NovaListaCovid[11][13]) + (NovaListaCovid[12][13]) + (NovaListaCovid[13][13]) + (NovaListaCovid[14][13]) + (NovaListaCovid[15][13]) 
print (SomaDadosObidosNovos)
ListaComparacao.append (SomaDadosObidosNovos)
print (ListaComparacao)
print (4 in ListaComparacao)

#Letra i)

print ("o tamanho total da lista é de:", len(NovaListaCovid))

#Letra j)

ListaDadosObidosNovos = [NovaListaCovid[0][13], NovaListaCovid[1][13], NovaListaCovid[2][13], NovaListaCovid[3][13], NovaListaCovid[4][13], NovaListaCovid[5][13], NovaListaCovid[6][13], NovaListaCovid[7][13], NovaListaCovid[8][13], NovaListaCovid[9][13], NovaListaCovid[10][13], NovaListaCovid[11][13], NovaListaCovid[12][13], NovaListaCovid[13][13], NovaListaCovid[14][13], NovaListaCovid[15][13]]

print ("O menor número de óbitdos novos foi de:", min(ListaDadosObidosNovos))
print ("O maior número de óbitdos novos foi de:",max(ListaDadosObidosNovos))

#Letra k)
AgendaCovidAmapaCompleta = {'Serra do Navio': [16, 160005, 16001, 'AREA CENTRAL', '29-08-2020', 35, 5397, 622, 0, 4, 0, ' ', ' ', 0], 
'Amapá': [16, 160010, 16002, 'AREA NORTE', '29/08/2020', 35, 9109, 484, 0, 4, 0, ' ', ' ', 0],
'Pedra Branca do Amapari': [16, 160015, 16001, 'AREA CENTRAL', '29/08/2020', 35, 16502, 2526, 4, 5, 0, ' ', ' ', 0],
'Calçoene': [16, 160020, 16002, 'AREA NORTE', '29/08/2020', 35, 11117, 1126, 0, 5, 0, ' ', ' ', 0],
'Cutias': [16, 160021, 16001, 'AREA CENTRAL', '29/08/2020', 35, 5983, 522, 0, 2, 0, ' ', ' ', 0],
'Ferreira Gomes': [16, 160023, 16001, 'AREA CENTRAL', '29/08/2020', 35, 7780, 539, 0, 3, 0, ' ', ' ', 0],
'Itaubal': [16, 160025, 16001, 'AREA CENTRAL', '29/08/2020', 35, 5503, 286, 0, 0, 0, ' ', ' ', 0],
'Laranjal do Jari': [16, 160027, 16003, 'AREA SUDOESTE', '29/08/2020', 35, 50410, 4283, 0, 44, 0, ' ', ' ', 0],
'Macapá': [16, 160030, 16001, 'AREA CENTRAL', '29/08/2020', 35, 503327, 17134, 34, 446, 1, ' ', ' ', 1],
'Mazagão': [16, 160040, 16003, 'AREA SUDOESTE', '29/08/2020', 35, 21632, 1354, 0, 8, 0, ' ', ' ', 1],
'Oiapoque': [16, 160050, 16002, 'AREA NORTE', '29/08/2020', 35, 27270, 2510, 2, 20, 0, ' ', ' ', 0],
'Porto Grande': [16, 160053, 16001, 'AREA CENTRAL', '29/08/2020', 35, 21971, 1098, 2, 13, 0, ' ', ' ', 0],
'Pracuúba': [16, 160055, 16002, 'AREA NORTE', '29/08/2020', 35, 5120, 350, 0, 6, 1, ' ', ' ', 0],
'Santana': [16, 160060, 16003, 'AREA SUDOESTE', '29/08/2020', 35, 121364, 6877, 99, 82, 0, ' ', ' ', 1],
'Tartarugalzinho': [16, 160070, 16002, 'AREA NORTE', '29/08/2020', 35, 17315, 992, 5, 4, 0, ' ', ' ', 0],
'Vitória do Jari': [16, 160080, 16003, 'AREA SUDOESTE', '29/08/2020', 35, 15931, 2068, 0, 13, 0, ' ', ' ', 0]}

AgendaCovidAmapaCasosNovos= {'Serra do Navio': [0], 'Amapá': [0],'Pedra Branca do Amapari': [4],'Calçoene': [0],'Cutias': [0],
'Ferreira Gomes': [0],'Itaubal': [0],'Laranjal do Jari': [0],'Macapá': [34],'Mazagão': [0],'Oiapoque': [2],
'Porto Grande': [2],'Pracuúba': [0],'Santana': [99],'Tartarugalzinho': [5],'Vitória do Jari': [0]}

print ('O número de casos novos para a cidade de Santana é de:', AgendaCovidAmapaCasosNovos['Santana'])

#Letra i)
AgendaTeresina = {'Região': ['Nordeste'], 'Estado': ['PI'], 'Ciadade': ['Teresina'], 'CodUF': [22], 'CodMunicípio': [221100], 'CodRegião': [22004], 'NomeRegião': ['ENTRE RIOS'] , 'Data': ['29/08/2020'], 'SemanaEPI': [35], 'População': [864845], 'CasosAcumulados': [25044], 'CasosNovos': [320],'ÓbitosAcumulados': [900], 'ÓbitosNovos':[6], 'Interior': [1]}

print ('O número de casos novos para a cidade de Teresina PI é de:', AgendaTeresina['CasosNovos'])