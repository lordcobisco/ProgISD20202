#Atividade Contextualizada 05

#Letra A: criar uma lista e uma tupla com as informações disponíveis no documento csv (colocar pelo menos 1 linha por estado e 10 regiões de saúde diferentes)
lista = [['Norte', 'AC', 'Jordão', 12, 120032, 12002, 'BAIXO ACRE E PURUS', '2020-05-21 00:00:00', 21, 8317.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'AC', 'Rio Branco', 12, 120040, 12002, 'BAIXO ACRE E PURUS', '2020-07-10 00:00:00', 28, 407319.0, 7894, 129, 285, 3, ' ', ' ', 1.0], ['Nordeste', 'AL', 'Capela', 27, 270170, 27004, '4ª REGIAO DE SAUDE', '2020-04-30 00:00:00', 18, 17053.0, 1, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Maravilha', 27, 270460, 27009, '9ª REGIAO DE SAUDE', '2020-06-17 00:00:00', 25, 9163.0, 15, 1, 0, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Nhamundá', 13, 130300, 13005, 'BAIXO AMAZONAS', '2020-07-20 00:00:00', 30, 21173.0, 413, 9, 5, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'São Sebastião do Uatumã', 13, 130395, 13004, 'MEDIO AMAZONAS', '2020-05-02 00:00:00', 18, 14020.0, 3, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'AP', 'Mazagão', 16, 160040, 16003, 'AREA SUDOESTE', '2020-03-27 00:00:00', 13, 21632.0, 0, 0, 0, 0, ' ', ' ', 1.0], ['Norte', 'AP', 'Oiapoque', 16, 160050, 16002, 'AREA NORTE', '2020-08-22 00:00:00', 34, 27270.0, 2433, 2, 19, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'Aurelino Leal', 29, 290240, 29012, 'ITABUNA', '2020-07-31 00:00:00', 31, 11531.0, 298, 0, 2, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'Utinga', 29, 293280, 29011, 'ITABERABA', '2020-07-05 00:00:00', 28, 19178.0, 6, 0, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Palhano', 23, 231000, 23009, '9ª REGIAO RUSSAS', '2020-07-06 00:00:00', 28, 9386.0, 56, -1, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Meruoca', 23, 230820, 23011, '11ª REGIAO SOBRAL', '2020-04-26 00:00:00', 18, 15057.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-05-10 00:00:00', 20, 3015268.0, 2682, 106, 42, 3, ' ', ' ', 1.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-07-23 00:00:00', 30, 3015268.0, 90023, 2222, 1218, 42, ' ', ' ', 1.0], ['Sudeste', 'ES', 'Guaçuí', 32, 320230, 32004, 'SUL', '2020-08-23 00:00:00', 35, 30867.0, 287, 3, 16, 0, ' ', ' ', 0.0], ['Sudeste', 'ES', 'Ponto Belo', 32, 320425, 32003, 'NORTE', '2020-07-12 00:00:00', 29, 7863.0, 25, 0, 1, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Nazário', 52, 521440, 52001, 'CENTRAL', '2020-05-18 00:00:00', 21, 9142.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Silvânia', 52, 522060, 52002, 'CENTRO SUL', '2020-04-30 00:00:00', 18, 20695.0, 1, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Campestre do Maranhão', 21, 210255, 21008, 'IMPERATRIZ', '2020-08-17 00:00:00', 34, 14374.0, 315, 0, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Grajaú', 21, 210480, 21004, 'BARRA DO CORDA', '2020-05-25 00:00:00', 22, 69527.0, 112, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'MG', 'Serra dos Aimorés', 31, 316670, 31066, 'NANUQUE', '2020-04-17 00:00:00', 16, 8699.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'MG', 'Inhapim', 31, 313090, 31034, 'CARATINGA', '2020-08-04 00:00:00', 32, 24140.0, 57, 0, 4, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Juti', 50, 500515, 50003, 'DOURADOS', '2020-05-24 00:00:00', 22, 6712.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Santa Rita do Pardo', 50, 500755, 50004, 'TRES LAGOAS', '2020-04-20 00:00:00', 17, 7851.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Itanhangá', 51, 510454, 51014, 'TELES PIRES', '2020-06-06 00:00:00', 23, 6737.0, 1, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Novo Mundo', 51, 510626, 51015, 'VALE DO PEIXOTO', '2020-05-31 00:00:00', 23, 9178.0, 12, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Redenção', 15, 150613, 15001, 'ARAGUAIA', '2020-06-24 00:00:00', 26, 84787.0, 829, 90, 12, 3, ' ', ' ', 0.0], ['Norte', 'PA', 'São Francisco do Pará', 15, 150740, 15008, 'METROPOLITANA III', '2020-06-29 00:00:00', 27, 15882.0, 67, 1, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Sapé', 25, 251530, 25001, '1ª REGIAO MATA ATLANTICA', '2020-08-09 00:00:00', 33, 52625.0, 951, 0, 34, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Alagoinha', 25, 250050, 25002, '2ª REGIAO', '2020-08-01 00:00:00', 31, 14489.0, 764, 1, 7, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Manari', 26, 260915, 26002, 'ARCOVERDE', '2020-08-07 00:00:00', 32, 21434.0, 6, 2, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Orobó', 26, 260970, 26006, 'LIMOEIRO', '2020-08-10 00:00:00', 33, 23884.0, 209, 1, 7, 1, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Monsenhor Hipólito', 22, 220650, 22009, 'VALE DO RIO GUARIBAS', '2020-06-19 00:00:00', 25, 7749.0, 25, 1, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Padre Marcos', 22, 220720, 22009, 'VALE DO RIO GUARIBAS', '2020-05-30 00:00:00', 22, 6868.0, 1, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Cruzeiro do Sul', 41, 410670, 41014, '14ª RS PARANAVAI', '2020-07-04 00:00:00', 27, 4469.0, 7, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Rio Azul', 41, 412200, 41004, '4ª RS IRATI', '2020-06-08 00:00:00', 24, 15236.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Areal', 33, 330022, 33003, 'CENTRO-SUL', '2020-08-12 00:00:00', 33, 12572.0, 138, 0, 3, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Itaguaí', 33, 330200, 33005, 'METROPOLITANA I', '2020-05-28 00:00:00', 22, 133019.0, 275, 40, 40, 2, ' ', ' ', 1.0], ['Nordeste', 'RN', 'Lagoa de Pedras', 24, 240630, 24001, '1ª REGIAO DE SAUDE - SAO JOSE DE MIPIBU', '2020-06-11 00:00:00', 24, 7544.0, 5, 0, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'RN', 'Itaú', 24, 240490, 24006, '6ª REGIAO DE SAUDE - PAU DOS FERROS', '2020-04-10 00:00:00', 15, 5878.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Vale do Paraíso', 11, 110180, 11003, 'CENTRAL', '2020-04-27 00:00:00', 18, 6825.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Ji-Paraná', 11, 110012, 11003, 'CENTRAL', '2020-07-19 00:00:00', 30, 128969.0, 755, 0, 12, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Rorainópolis', 14, 140047, 14002, 'SUL', '2020-04-06 00:00:00', 15, 30163.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Pacaraima', 14, 140045, 14001, 'CENTRO NORTE', '2020-06-05 00:00:00', 23, 17401.0, 162, 25, 3, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Nova Boa Vista', 43, 431295, 43020, 'REGIAO 20', '2020-06-11 00:00:00', 24, 1775.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Condor', 43, 430570, 43013, 'REGIAO 13', '2020-05-04 00:00:00', 19, 6753.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Cunha Porã', 42, 420470, 42002, 'OESTE', '2020-06-29 00:00:00', 27, 11086.0, 31, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Lajeado Grande', 42, 420945, 42003, 'XANXERE', '2020-05-23 00:00:00', 21, 1427.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Porto da Folha', 28, 280560, 28005, 'NOSSA SENHORA DA GLORIA', '2020-04-30 00:00:00', 18, 28596.0, 3, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Salgado', 28, 280620, 28004, 'LAGARTO', '2020-05-25 00:00:00', 22, 19998.0, 19, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Palmital', 35, 353530, 35092, 'ASSIS', '2020-06-02 00:00:00', 23, 22221.0, 5, 1, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Borborema', 35, 350740, 35032, 'CENTRO OESTE DO DRS III', '2020-08-07 00:00:00', 32, 16046.0, 61, 2, 1, 0, ' ', ' ', 0.0], ['Norte', 'TO', 'Aparecida do Rio Negro', 17, 170110, 17006, 'CAPIM DOURADO', '2020-04-22 00:00:00', 17, 4795.0, 0, 0, 0, 0, ' ', ' ', 1.0], ['Norte', 'TO', 'Santa Maria do Tocantins', 17, 171888, 17004, 'CERRADO TOCANTINS ARAGUAIA', '2020-04-13 00:00:00', 16, 3434.0, 0, 0, 0, 0, ' ', ' ', 0.0]]
tupla = (('Norte', 'AC', 'Jordão', 12, 120032, 12002, 'BAIXO ACRE E PURUS', '2020-05-21 00:00:00', 21, 8317.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'AC', 'Rio Branco', 12, 120040, 12002, 'BAIXO ACRE E PURUS', '2020-07-10 00:00:00', 28, 407319.0, 7894, 129, 285, 3, ' ', ' ', 1.0), ('Nordeste', 'AL', 'Capela', 27, 270170, 27004, '4ª REGIAO DE SAUDE', '2020-04-30 00:00:00', 18, 17053.0, 1, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'AL', 'Maravilha', 27, 270460, 27009, '9ª REGIAO DE SAUDE', '2020-06-17 00:00:00', 25, 9163.0, 15, 1, 0, 0, ' ', ' ', 0.0), ('Norte', 'AM', 'Nhamundá', 13, 130300, 13005, 'BAIXO AMAZONAS', '2020-07-20 00:00:00', 30, 21173.0, 413, 9, 5, 0, ' ', ' ', 0.0), ('Norte', 'AM', 'São Sebastião do Uatumã', 13, 130395, 13004, 'MEDIO AMAZONAS', '2020-05-02 00:00:00', 18, 14020.0, 3, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'AP', 'Mazagão', 16, 160040, 16003, 'AREA SUDOESTE', '2020-03-27 00:00:00', 13, 21632.0, 0, 0, 0, 0, ' ', ' ', 1.0), ('Norte', 'AP', 'Oiapoque', 16, 160050, 16002, 'AREA NORTE', '2020-08-22 00:00:00', 34, 27270.0, 2433, 2, 19, 0, ' ', ' ', 0.0), ('Nordeste', 'BA', 'Aurelino Leal', 29, 290240, 29012, 'ITABUNA', '2020-07-31 00:00:00', 31, 11531.0, 298, 0, 2, 0, ' ', ' ', 0.0), ('Nordeste', 'BA', 'Utinga', 29, 293280, 29011, 'ITABERABA', '2020-07-05 00:00:00', 28, 19178.0, 6, 0, 1, 0, ' ', ' ', 0.0), ('Nordeste', 'CE', 'Palhano', 23, 231000, 23009, '9ª REGIAO RUSSAS', '2020-07-06 00:00:00', 28, 9386.0, 56, -1, 3, 0, ' ', ' ', 0.0), ('Nordeste', 'CE', 'Meruoca', 23, 230820, 23011, '11ª REGIAO SOBRAL', '2020-04-26 00:00:00', 18, 15057.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-05-10 00:00:00', 20, 3015268.0, 2682, 106, 42, 3, ' ', ' ', 1.0), ('Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-07-23 00:00:00', 30, 3015268.0, 90023, 2222, 1218, 42, ' ', ' ', 1.0), ('Sudeste', 'ES', 'Guaçuí', 32, 320230, 32004, 'SUL', '2020-08-23 00:00:00', 35, 30867.0, 287, 3, 16, 0, ' ', ' ', 0.0), ('Sudeste', 'ES', 'Ponto Belo', 32, 320425, 32003, 'NORTE', '2020-07-12 00:00:00', 29, 7863.0, 25, 0, 1, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'GO', 'Nazário', 52, 521440, 52001, 'CENTRAL', '2020-05-18 00:00:00', 21, 9142.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'GO', 'Silvânia', 52, 522060, 52002, 'CENTRO SUL', '2020-04-30 00:00:00', 18, 20695.0, 1, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'MA', 'Campestre do Maranhão', 21, 210255, 21008, 'IMPERATRIZ', '2020-08-17 00:00:00', 34, 14374.0, 315, 0, 3, 0, ' ', ' ', 0.0), ('Nordeste', 'MA', 'Grajaú', 21, 210480, 21004, 'BARRA DO CORDA', '2020-05-25 00:00:00', 22, 69527.0, 112, 0, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'MG', 'Serra dos Aimorés', 31, 316670, 31066, 'NANUQUE', '2020-04-17 00:00:00', 16, 8699.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'MG', 'Inhapim', 31, 313090, 31034, 'CARATINGA', '2020-08-04 00:00:00', 32, 24140.0, 57, 0, 4, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MS', 'Juti', 50, 500515, 50003, 'DOURADOS', '2020-05-24 00:00:00', 22, 6712.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MS', 'Santa Rita do Pardo', 50, 500755, 50004, 'TRES LAGOAS', '2020-04-20 00:00:00', 17, 7851.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MT', 'Itanhangá', 51, 510454, 51014, 'TELES PIRES', '2020-06-06 00:00:00', 23, 6737.0, 1, 0, 0, 0, ' ', ' ', 0.0), ('Centro-Oeste', 'MT', 'Novo Mundo', 51, 510626, 51015, 'VALE DO PEIXOTO', '2020-05-31 00:00:00', 23, 9178.0, 12, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'PA', 'Redenção', 15, 150613, 15001, 'ARAGUAIA', '2020-06-24 00:00:00', 26, 84787.0, 829, 90, 12, 3, ' ', ' ', 0.0), ('Norte', 'PA', 'São Francisco do Pará', 15, 150740, 15008, 'METROPOLITANA III', '2020-06-29 00:00:00', 27, 15882.0, 67, 1, 3, 0, ' ', ' ', 0.0), ('Nordeste', 'PB', 'Sapé', 25, 251530, 25001, '1ª REGIAO MATA ATLANTICA', '2020-08-09 00:00:00', 33, 52625.0, 951, 0, 34, 0, ' ', ' ', 0.0), ('Nordeste', 'PB', 'Alagoinha', 25, 250050, 25002, '2ª REGIAO', '2020-08-01 00:00:00', 31, 14489.0, 764, 1, 7, 0, ' ', ' ', 0.0), ('Nordeste', 'PE', 'Manari', 26, 260915, 26002, 'ARCOVERDE', '2020-08-07 00:00:00', 32, 21434.0, 6, 2, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'PE', 'Orobó', 26, 260970, 26006, 'LIMOEIRO', '2020-08-10 00:00:00', 33, 23884.0, 209, 1, 7, 1, ' ', ' ', 0.0), ('Nordeste', 'PI', 'Monsenhor Hipólito', 22, 220650, 22009, 'VALE DO RIO GUARIBAS', '2020-06-19 00:00:00', 25, 7749.0, 25, 1, 1, 0, ' ', ' ', 0.0), ('Nordeste', 'PI', 'Padre Marcos', 22, 220720, 22009, 'VALE DO RIO GUARIBAS', '2020-05-30 00:00:00', 22, 6868.0, 1, 0, 0, 0, ' ', ' ', 0.0), ('Sul', 'PR', 'Cruzeiro do Sul', 41, 410670, 41014, '14ª RS PARANAVAI', '2020-07-04 00:00:00', 27, 4469.0, 7, 0, 0, 0, ' ', ' ', 0.0), ('Sul', 'PR', 'Rio Azul', 41, 412200, 41004, '4ª RS IRATI', '2020-06-08 00:00:00', 24, 15236.0, 1, 1, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'RJ', 'Areal', 33, 330022, 33003, 'CENTRO-SUL', '2020-08-12 00:00:00', 33, 12572.0, 138, 0, 3, 0, ' ', ' ', 0.0), ('Sudeste', 'RJ', 'Itaguaí', 33, 330200, 33005, 'METROPOLITANA I', '2020-05-28 00:00:00', 22, 133019.0, 275, 40, 40, 2, ' ', ' ', 1.0), ('Nordeste', 'RN', 'Lagoa de Pedras', 24, 240630, 24001, '1ª REGIAO DE SAUDE - SAO JOSE DE MIPIBU', '2020-06-11 00:00:00', 24, 7544.0, 5, 0, 1, 0, ' ', ' ', 0.0), ('Nordeste', 'RN', 'Itaú', 24, 240490, 24006, '6ª REGIAO DE SAUDE - PAU DOS FERROS', '2020-04-10 00:00:00', 15, 5878.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'RO', 'Vale do Paraíso', 11, 110180, 11003, 'CENTRAL', '2020-04-27 00:00:00', 18, 6825.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'RO', 'Ji-Paraná', 11, 110012, 11003, 'CENTRAL', '2020-07-19 00:00:00', 30, 128969.0, 755, 0, 12, 0, ' ', ' ', 0.0), ('Norte', 'RR', 'Rorainópolis', 14, 140047, 14002, 'SUL', '2020-04-06 00:00:00', 15, 30163.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Norte', 'RR', 'Pacaraima', 14, 140045, 14001, 'CENTRO NORTE', '2020-06-05 00:00:00', 23, 17401.0, 162, 25, 3, 0, ' ', ' ', 0.0), ('Sul', 'RS', 'Nova Boa Vista', 43, 431295, 43020, 'REGIAO 20', '2020-06-11 00:00:00', 24, 1775.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Sul', 'RS', 'Condor', 43, 430570, 43013, 'REGIAO 13', '2020-05-04 00:00:00', 19, 6753.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Sul', 'SC', 'Cunha Porã', 42, 420470, 42002, 'OESTE', '2020-06-29 00:00:00', 27, 11086.0, 31, 0, 0, 0, ' ', ' ', 0.0), ('Sul', 'SC', 'Lajeado Grande', 42, 420945, 42003, 'XANXERE', '2020-05-23 00:00:00', 21, 1427.0, 0, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'SE', 'Porto da Folha', 28, 280560, 28005, 'NOSSA SENHORA DA GLORIA', '2020-04-30 00:00:00', 18, 28596.0, 3, 0, 0, 0, ' ', ' ', 0.0), ('Nordeste', 'SE', 'Salgado', 28, 280620, 28004, 'LAGARTO', '2020-05-25 00:00:00', 22, 19998.0, 19, 0, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'SP', 'Palmital', 35, 353530, 35092, 'ASSIS', '2020-06-02 00:00:00', 23, 22221.0, 5, 1, 0, 0, ' ', ' ', 0.0), ('Sudeste', 'SP', 'Borborema', 35, 350740, 35032, 'CENTRO OESTE DO DRS III', '2020-08-07 00:00:00', 32, 16046.0, 61, 2, 1, 0, ' ', ' ', 0.0), ('Norte', 'TO', 'Aparecida do Rio Negro', 17, 170110, 17006, 'CAPIM DOURADO', '2020-04-22 00:00:00', 17, 4795.0, 0, 0, 0, 0, ' ', ' ', 1.0), ('Norte', 'TO', 'Santa Maria do Tocantins', 17, 171888, 17004, 'CERRADO TOCANTINS ARAGUAIA', '2020-04-13 00:00:00', 16, 3434.0, 0, 0, 0, 0, ' ', ' ', 0.0))

'''print(lista)
print(tupla)'''

#Letra B: printar o número de casos acumulados para o estado do Rio de Janeiro tanto para a tupla quanto para a lista
#Lista
print(lista[36][10])
print(lista[37][10])
print('Na lista, o número de casos acumulados no RJ corresponde a:', lista[36][10] + lista[37][10], '\n')
#Tupla
print(tupla[36][10])
print(tupla[37][10])
print('Na tupla, o número de casos acumulados no RJ corresponde a:', tupla[36][10] + tupla[37][10], '\n')

#Letra C: apresentar na tela todos os óbitos acumulados mostrando os casos apenas para o caso dos estados 
print('Número de óbitos acumulados no AC:', lista[0][12] + lista[1][12])
print('Número de óbitos acumulados em AL:', lista[2][12] + lista[3][12])
print('Número de óbitos acumulados no AM:', lista[4][12] + lista[5][12])
print('Número de óbitos acumulados no AP:', lista[6][12] + lista[7][12])
print('Número de óbitos acumulados na BA:', lista[8][12] + lista[9][12])
print('Número de óbitos acumulados no CE:', lista[10][12] + lista[11][12])
print('Número de óbitos acumulados no DF:', lista[12][12] + lista[13][12])
print('Número de óbitos acumulados no ES:', lista[14][12] + lista[15][12])
print('Número de óbitos acumulados em GO:', lista[16][12] + lista[17][12])
print('Número de óbitos acumulados no MA:', lista[18][12] + lista[19][12])
print('Número de óbitos acumulados em MG:', lista[20][12] + lista[21][12])
print('Número de óbitos acumulados no MS:', lista[22][12] + lista[23][12])
print('Número de óbitos acumulados no MT:', lista[24][12] + lista[25][12])
print('Número de óbitos acumulados no PA:', lista[26][12] + lista[27][12])
print('Número de óbitos acumulados na PB:', lista[28][12] + lista[29][12])
print('Número de óbitos acumulados em PE:', lista[30][12] + lista[31][12])
print('Número de óbitos acumulados no PI:', lista[32][12] + lista[33][12])
print('Número de óbitos acumulados no PR:', lista[34][12] + lista[35][12])
print('Número de óbitos acumulados no RJ:', lista[36][12] + lista[37][12])
print('Número de óbitos acumulados no RN:', lista[38][12] + lista[39][12])
print('Número de óbitos acumulados em RO:', lista[40][12] + lista[41][12])
print('Número de óbitos acumulados em RR:', lista[42][12] + lista[43][12])
print('Número de óbitos acumulados no RS:', lista[44][12] + lista[45][12])
print('Número de óbitos acumulados em SC:', lista[46][12] + lista[47][12])
print('Número de óbitos acumulados em SE:', lista[48][12] + lista[49][12])
print('Número de óbitos acumulados em SP:', lista[50][12] + lista[51][12])
print('Número de óbitos acumulados em TO:', lista[52][12] + lista[53][12])

#Letra D: Assumir que os dados de óbitos novos para o estado da Paraíba estejam errados em 10 unidades para menos. Sobrescreva a informação tanto na lista quanto na tupla, corrigindo os dados. 
#Lista
lista[28][13]=10
lista[29][13]=10
print('Corrigindo-se o número de óbitos novos no estado da Paraíba, que estava errado em 10 unidades para menos, a lista ficará:', lista, '\n')

#Letra E: as duas operações foram possíveis (lista e tupla)? Justifique.
print('Só foi possível corrigir o número de óbitos novos no estado da Paraíba na lista, pois os valores em uma tupla são imutáveis. \n')

#Letra F: Criar uma nova lista com apenas dados de 1 estado e todos os municípios e adicionar essa lista nova a lista já existente (append ou insert). 
listaAP = [['Norte', 'AP', 'Amapá', 16, 160010, 16002, 'AREA NORTE', '31/08/2020', 36, 9109, 504, 41, 4, 1, ' ', ' ', 0.0], ['Norte', 'AP', 'Calçoene', 16, 160020, 16002, 'AREA NORTE', '31/08/2020', 36, 11117, 1131, 67, 5, 1, ' ', ' ', 0.0], ['Norte', 'AP', 'Cutias', 16, 160021, 16001, 'AREA CENTRAL', '31/08/2020', 36, 5983, 583, 110, 2, 1, ' ', ' ', 0.0], ['Norte', 'AP', 'Ferreira Gomes', 16, 160023, 16001, 'AREA CENTRAL', '31/08/2020', 36, 7780, 539, 61, 3, 1, ' ', ' ', 0.0], ['Norte', 'AP', 'Itaubal', 16, 160025, 16001, 'AREA CENTRAL', '31/08/2020', 36, 5503, 286, 26, 0, 0, ' ', ' ', 0.0], ['Norte', 'AP', 'Laranjal do Jari', 16, 160027, 16003, 'AREA SUDOESTE', '31/08/2020', 36, 50410, 4325, 158, 44, 3, ' ', ' ', 0.0], ['Norte', 'AP', 'Macapá', 16, 160030, 16001, 'AREA CENTRAL', '31/08/2020', 36, 503327, 17238, 2504, 448, 16, ' ', ' ', 1], ['Norte', 'AP', 'Mazagão', 16, 160040, 16003, 'AREA SUDOESTE', '31/08/2020', 36, 21632, 1371, 87, 8, 2, ' ', ' ', 1], ['Norte', 'AP', 'Oiapoque', 16, 160050, 16002, 'AREA NORTE', '31/08/2020', 36, 27270, 2520, 183, 20, 2, ' ', ' ', 0.0], ['Norte', 'AP', 'Pedra Branca do Amapari', 16, 160015, 16001, 'AREA CENTRAL', '31/08/2020', 36, 16502, 2532, 188, 5, 1, ' ', ' ', 0.0], ['Norte', 'AP', 'Porto Grande', 16, 160053, 16001, 'AREA CENTRAL', '31/08/2020', 36, 21971, 1104, 76, 13, 1, ' ', ' ', 0.0], ['Norte', 'AP', 'Pracuúba', 16, 160055, 16002, 'AREA NORTE', '31/08/2020', 36, 5120, 350, 39, 6, 1, ' ', ' ', 0.0], ['Norte', 'AP', 'Santana', 16, 160060, 16003, 'AREA SUDOESTE', '31/08/2020', 36, 121364, 7010, 640, 82, 8, ' ', ' ', 1], ['Norte', 'AP', 'Serra do Navio', 16, 160005, 16001, 'AREA CENTRAL', '31/08/2020', 36, 5397, 622, 53, 4, 1, ' ', ' ', 0.0], ['Norte', 'AP', 'Tartarugalzinho', 16, 160070, 16002, 'AREA NORTE', '31/08/2020', 36, 17315, 992, 157, 4, 1, ' ', ' ', 0.0], ['Norte', 'AP', 'Vitória do Jari', 16, 160080, 16003, 'AREA SUDOESTE', '31/08/2020', 36, 15931, 2086, 57, 13, 2, ' ', ' ', 0.0]]

#Adicionando a lista do AP a lista já existente:
lista.append(listaAP)
print(lista)

#Letra G: remover da lista os dados das regiões de saúde
lista[0].pop(6)
lista[1].pop(6)
lista[2].pop(6)
lista[3].pop(6)
lista[4].pop(6)
lista[5].pop(6)
lista[6].pop(6)
lista[7].pop(6)
lista[8].pop(6)
lista[9].pop(6)
lista[10].pop(6)
lista[11].pop(6)
lista[12].pop(6)
lista[13].pop(6)
lista[14].pop(6)
lista[15].pop(6)
lista[16].pop(6)
lista[17].pop(6)
lista[18].pop(6)
lista[19].pop(6)
lista[20].pop(6)
lista[21].pop(6)
lista[22].pop(6)
lista[23].pop(6)
lista[24].pop(6)
lista[25].pop(6)
lista[26].pop(6)
lista[27].pop(6)
lista[28].pop(6)
lista[29].pop(6)
lista[30].pop(6)
lista[31].pop(6)
lista[32].pop(6)
lista[33].pop(6)
lista[34].pop(6)
lista[35].pop(6)
lista[36].pop(6)
lista[37].pop(6)
lista[38].pop(6)
lista[39].pop(6)
lista[40].pop(6)
lista[41].pop(6)
lista[42].pop(6)
lista[43].pop(6)
lista[44].pop(6)
lista[45].pop(6)
lista[46].pop(6)
lista[47].pop(6)
lista[48].pop(6)
lista[49].pop(6)
lista[50].pop(6)
lista[51].pop(6)
lista[52].pop(6)
lista[53].pop(6)
lista[54][0].pop(6)
lista[54][1].pop(6)
lista[54][2].pop(6)
lista[54][3].pop(6)
lista[54][4].pop(6)
lista[54][5].pop(6)
lista[54][6].pop(6)
lista[54][7].pop(6)
lista[54][8].pop(6)
lista[54][9].pop(6)
lista[54][10].pop(6)
lista[54][11].pop(6)
lista[54][12].pop(6)
lista[54][13].pop(6)
lista[54][14].pop(6)
lista[54][15].pop(6)

#Letra H: verificar se a soma dos dados dos municípios, em 18/08/2020, é igual ao dado da lista, mostrando na tela apenas se for verdadeiro
populacaoAP=845731
casosAcumuladosAP=39957
casosNovosAP=254
obitosAcumuladosAP=619
obitosNovosAP=2
print('Comparando se a soma de alguns dados dos municípios do Amapá, no dia 18/08/2020, é igual aos dados da lista, no dia 31/08/2020: ')
somaPopulacao = lista[54][0][8]+lista[54][1][8]+lista[54][2][8]+lista[54][3][8]+lista[54][4][8]+lista[54][5][8]+lista[54][6][8]+lista[54][7][8]+lista[54][8][8]+lista[54][9][8]+lista[54][10][8]+lista[54][11][8]+lista[54][12][8]+lista[54][13][8]+lista[54][14][8]+lista[54][15][8]
if(somaPopulacao==populacaoAP):
    print('O somatório da população é: ', somaPopulacao)

somaCasosAcumulados = lista[54][0][9]+lista[54][1][9]+lista[54][2][9]+lista[54][3][9]+lista[54][4][9]+lista[54][5][9]+lista[54][6][9]+lista[54][7][9]+lista[54][8][9]+lista[54][9][9]+lista[54][10][9]+lista[54][11][9]+lista[54][12][9]+lista[54][13][9]+lista[54][14][9]+lista[54][15][9]
if(casosAcumuladosAP==somaCasosAcumulados):
    print('O somatório dos casos acumulados é: ', somaCasosAcumulados)

somaCasosNovos = lista[54][0][10]+lista[54][1][10]+lista[54][2][10]+lista[54][3][10]+lista[54][4][10]+lista[54][5][10]+lista[54][6][10]+lista[54][7][10]+lista[54][8][10]+lista[54][9][10]+lista[54][10][10]+lista[54][11][10]+lista[54][12][10]+lista[54][13][10]+lista[54][14][10]+lista[54][15][10]
if(casosNovosAP==somaCasosNovos):
    print('O somatório dos casos novos é: ', somaCasosNovos)

somaObitosAcumulados = lista[54][0][11]+lista[54][1][11]+lista[54][2][11]+lista[54][3][11]+lista[54][4][11]+lista[54][5][11]+lista[54][6][11]+lista[54][7][11]+lista[54][8][11]+lista[54][9][11]+lista[54][10][11]+lista[54][11][11]+lista[54][12][11]+lista[54][13][11]+lista[54][14][11]+lista[54][15][11]
if(obitosAcumuladosAP==somaObitosAcumulados):
    print('O somatório dos óbitos acumulados é: ', somaObitosAcumulados)

somaObitosNovos = lista[54][0][12]+lista[54][1][12]+lista[54][2][12]+lista[54][3][12]+lista[54][4][12]+lista[54][5][12]+lista[54][6][12]+lista[54][7][12]+lista[54][8][12]+lista[54][9][12]+lista[54][10][12]+lista[54][11][12]+lista[54][12][12]+lista[54][13][12]+lista[54][14][12]+lista[54][15][12]
if(obitosNovosAP==somaObitosNovos):
    print('O somatório dos óbitos novos é: ', somaObitosNovos)

#Letra I: retornar o tamanho total da lista
print('O tamanho da lista é: ',len(lista))

#Letra J: verificar qual o maior e menor valor numérico de óbitos novos
listaObitosNovos=[lista[0][12],lista[1][12],lista[2][12],lista[3][12],lista[4][12],lista[5][12],lista[6][12],lista[7][12],lista[8][12],lista[9][12],lista[10][12],lista[11][12],lista[12][12],lista[13][12],lista[14][12],lista[15][12],lista[16][12],lista[17][12],lista[18][12],lista[19][12],lista[20][12],lista[21][12],lista[22][12],lista[23][12],lista[24][12],lista[25][12],lista[26][12],lista[27][12],lista[28][12],lista[29][12],lista[30][12],lista[31][12],lista[32][12],lista[33][12],lista[34][12],lista[35][12],lista[36][12],lista[37][12],lista[38][12],lista[39][12],lista[40][12],lista[41][12],lista[42][12],lista[43][12],lista[44][12],lista[45][12],lista[46][12],lista[47][12],lista[48][12],lista[49][12],lista[50][12],lista[51][12],lista[52][12],lista[53][12],lista[54][0][12],lista[54][1][12],lista[54][2][12],lista[54][3][12],lista[54][4][12],lista[54][5][12],lista[54][6][12],lista[54][7][12],lista[54][8][12],lista[54][9][12],lista[54][10][12],lista[54][11][12],lista[54][12][12],lista[54][13][12],lista[54][14][12],lista[54][15][12]]
print('Menor valor numérico de óbitos novos: ', min(listaObitosNovos))
print('Maior valor numérico de óbitos novos: ', max(listaObitosNovos))

#Letra K: criar um dicionário de forma que seja possível encontrar os municípios associados a um estado específico e extrair os dados de casos novos em apenas um comando
dicionario={'Norte', 'AC', 'Jordão', 12, 120032, 12002, 'BAIXO ACRE E PURUS', '2020-05-21 00:00:00', 21, 8317.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Norte', 'AC', 'Rio Branco', 12, 120040, 12002, 'BAIXO ACRE E PURUS', '2020-07-10 00:00:00', 28, 407319.0, 7894, 129, 285, 3, ' ', ' ', 1.0, 'Nordeste', 'AL', 'Capela', 27, 270170, 27004, '4ª REGIAO DE SAUDE', '2020-04-30 00:00:00', 18, 17053.0, 1, 0, 0, 0, ' ', ' ', 0.0, 'Nordeste', 'AL', 'Maravilha', 27, 270460, 27009, '9ª REGIAO DE SAUDE', '2020-06-17 00:00:00', 25, 9163.0, 15, 1, 0, 0, ' ', ' ', 0.0, 'Norte', 'AM', 'Nhamundá', 13, 130300, 13005, 'BAIXO AMAZONAS', '2020-07-20 00:00:00', 30, 21173.0, 413, 9, 5, 0, ' ', ' ', 0.0, 'Norte', 'AM', 'São Sebastião do Uatumã', 13, 130395, 13004, 'MEDIO AMAZONAS', '2020-05-02 00:00:00', 18, 14020.0, 3, 0, 0, 0, ' ', ' ', 0.0, 'Norte', 'AP', 'Mazagão', 16, 160040, 16003, 'AREA SUDOESTE', '2020-03-27 00:00:00', 13, 21632.0, 0, 0, 0, 0, ' ', ' ', 1.0, 'Norte', 'AP', 'Oiapoque', 16, 160050, 16002, 'AREA NORTE', '2020-08-22 00:00:00', 34, 27270.0, 2433, 2, 19, 0, ' ', ' ', 0.0, 'Nordeste', 'BA', 'Aurelino Leal', 29, 290240, 29012, 'ITABUNA', '2020-07-31 00:00:00', 31, 11531.0, 298, 0, 2, 0, ' ', ' ', 0.0, 'Nordeste', 'BA', 'Utinga', 29, 293280, 29011, 'ITABERABA', '2020-07-05 00:00:00', 28, 19178.0, 6, 0, 1, 0, ' ', ' ', 0.0, 'Nordeste', 'CE', 'Palhano', 23, 231000, 23009, '9ª REGIAO RUSSAS', '2020-07-06 00:00:00', 28, 9386.0, 56, -1, 3, 0, ' ', ' ', 0.0, 'Nordeste', 'CE', 'Meruoca', 23, 230820, 23011, '11ª REGIAO SOBRAL', '2020-04-26 00:00:00', 18, 15057.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-05-10 00:00:00', 20, 3015268.0, 2682, 106, 42, 3, ' ', ' ', 1.0, 'Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-07-23 00:00:00', 30, 3015268.0, 90023, 2222, 1218, 42, ' ', ' ', 1.0, 'Sudeste', 'ES', 'Guaçuí', 32, 320230, 32004, 'SUL', '2020-08-23 00:00:00', 35, 30867.0, 287, 3, 16, 0, ' ', ' ', 0.0, 'Sudeste', 'ES', 'Ponto Belo', 32, 320425, 32003, 'NORTE', '2020-07-12 00:00:00', 29, 7863.0, 25, 0, 1, 0, ' ', ' ', 0.0, 'Centro-Oeste', 'GO', 'Nazário', 52, 521440, 52001, 'CENTRAL', '2020-05-18 00:00:00', 21, 9142.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Centro-Oeste', 'GO', 'Silvânia', 52, 522060, 52002, 'CENTRO SUL', '2020-04-30 00:00:00', 18, 20695.0, 1, 0, 0, 0, ' ', ' ', 0.0, 'Nordeste', 'MA', 'Campestre do Maranhão', 21, 210255, 21008, 'IMPERATRIZ', '2020-08-17 00:00:00', 34, 14374.0, 315, 0, 3, 0, ' ', ' ', 0.0, 'Nordeste', 'MA', 'Grajaú', 21, 210480, 21004, 'BARRA DO CORDA', '2020-05-25 00:00:00', 22, 69527.0, 112, 0, 0, 0, ' ', ' ', 0.0, 'Sudeste', 'MG', 'Serra dos Aimorés', 31, 316670, 31066, 'NANUQUE', '2020-04-17 00:00:00', 16, 8699.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Sudeste', 'MG', 'Inhapim', 31, 313090, 31034, 'CARATINGA', '2020-08-04 00:00:00', 32, 24140.0, 57, 0, 4, 0, ' ', ' ', 0.0, 'Centro-Oeste', 'MS', 'Juti', 50, 500515, 50003, 'DOURADOS', '2020-05-24 00:00:00', 22, 6712.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Centro-Oeste', 'MS', 'Santa Rita do Pardo', 50, 500755, 50004, 'TRES LAGOAS', '2020-04-20 00:00:00', 17, 7851.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Centro-Oeste', 'MT', 'Itanhangá', 51, 510454, 51014, 'TELES PIRES', '2020-06-06 00:00:00', 23, 6737.0, 1, 0, 0, 0, ' ', ' ', 0.0, 'Centro-Oeste', 'MT', 'Novo Mundo', 51, 510626, 51015, 'VALE DO PEIXOTO', '2020-05-31 00:00:00', 23, 9178.0, 12, 0, 0, 0, ' ', ' ', 0.0, 'Norte', 'PA', 'Redenção', 15, 150613, 15001, 'ARAGUAIA', '2020-06-24 00:00:00', 26, 84787.0, 829, 90, 12, 3, ' ', ' ', 0.0, 'Norte', 'PA', 'São Francisco do Pará', 15, 150740, 15008, 'METROPOLITANA III', '2020-06-29 00:00:00', 27, 15882.0, 67, 1, 3, 0, ' ', ' ', 0.0, 'Nordeste', 'PB', 'Sapé', 25, 251530, 25001, '1ª REGIAO MATA ATLANTICA', '2020-08-09 00:00:00', 33, 52625.0, 951, 0, 34, 0, ' ', ' ', 0.0, 'Nordeste', 'PB', 'Alagoinha', 25, 250050, 25002, '2ª REGIAO', '2020-08-01 00:00:00', 31, 14489.0, 764, 1, 7, 0, ' ', ' ', 0.0, 'Nordeste', 'PE', 'Manari', 26, 260915, 26002, 'ARCOVERDE', '2020-08-07 00:00:00', 32, 21434.0, 6, 2, 0, 0, ' ', ' ', 0.0, 'Nordeste', 'PE', 'Orobó', 26, 260970, 26006, 'LIMOEIRO', '2020-08-10 00:00:00', 33, 23884.0, 209, 1, 7, 1, ' ', ' ', 0.0, 'Nordeste', 'PI', 'Monsenhor Hipólito', 22, 220650, 22009, 'VALE DO RIO GUARIBAS', '2020-06-19 00:00:00', 25, 7749.0, 25, 1, 1, 0, ' ', ' ', 0.0, 'Nordeste', 'PI', 'Padre Marcos', 22, 220720, 22009, 'VALE DO RIO GUARIBAS', '2020-05-30 00:00:00', 22, 6868.0, 1, 0, 0, 0, ' ', ' ', 0.0, 'Sul', 'PR', 'Cruzeiro do Sul', 41, 410670, 41014, '14ª RS PARANAVAI', '2020-07-04 00:00:00', 27, 4469.0, 7, 0, 0, 0, ' ', ' ', 0.0, 'Sul', 'PR', 'Rio Azul', 41, 412200, 41004, '4ª RS IRATI', '2020-06-08 00:00:00', 24, 15236.0, 1, 1, 0, 0, ' ', ' ', 0.0, 'Sudeste', 'RJ', 'Areal', 33, 330022, 33003, 'CENTRO-SUL', '2020-08-12 00:00:00', 33, 12572.0, 138, 0, 3, 0, ' ', ' ', 0.0, 'Sudeste', 'RJ', 'Itaguaí', 33, 330200, 33005, 'METROPOLITANA I', '2020-05-28 00:00:00', 22, 133019.0, 275, 40, 40, 2, ' ', ' ', 1.0, 'Nordeste', 'RN', 'Lagoa de Pedras', 24, 240630, 24001, '1ª REGIAO DE SAUDE - SAO JOSE DE MIPIBU', '2020-06-11 00:00:00', 24, 7544.0, 5, 0, 1, 0, ' ', ' ', 0.0, 'Nordeste', 'RN', 'Itaú', 24, 240490, 24006, '6ª REGIAO DE SAUDE - PAU DOS FERROS', '2020-04-10 00:00:00', 15, 5878.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Norte', 'RO', 'Vale do Paraíso', 11, 110180, 11003, 'CENTRAL', '2020-04-27 00:00:00', 18, 6825.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Norte', 'RO', 'Ji-Paraná', 11, 110012, 11003, 'CENTRAL', '2020-07-19 00:00:00', 30, 128969.0, 755, 0, 12, 0, ' ', ' ', 0.0, 'Norte', 'RR', 'Rorainópolis', 14, 140047, 14002, 'SUL', '2020-04-06 00:00:00', 15, 30163.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Norte', 'RR', 'Pacaraima', 14, 140045, 14001, 'CENTRO NORTE', '2020-06-05 00:00:00', 23, 17401.0, 162, 25, 3, 0, ' ', ' ', 0.0, 'Sul', 'RS', 'Nova Boa Vista', 43, 431295, 43020, 'REGIAO 20', '2020-06-11 00:00:00', 24, 1775.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Sul', 'RS', 'Condor', 43, 430570, 43013, 'REGIAO 13', '2020-05-04 00:00:00', 19, 6753.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Sul', 'SC', 'Cunha Porã', 42, 420470, 42002, 'OESTE', '2020-06-29 00:00:00', 27, 11086.0, 31, 0, 0, 0, ' ', ' ', 0.0, 'Sul', 'SC', 'Lajeado Grande', 42, 420945, 42003, 'XANXERE', '2020-05-23 00:00:00', 21, 1427.0, 0, 0, 0, 0, ' ', ' ', 0.0, 'Nordeste', 'SE', 'Porto da Folha', 28, 280560, 28005, 'NOSSA SENHORA DA GLORIA', '2020-04-30 00:00:00', 18, 28596.0, 3, 0, 0, 0, ' ', ' ', 0.0, 'Nordeste', 'SE', 'Salgado', 28, 280620, 28004, 'LAGARTO', '2020-05-25 00:00:00', 22, 19998.0, 19, 0, 0, 0, ' ', ' ', 0.0, 'Sudeste', 'SP', 'Palmital', 35, 353530, 35092, 'ASSIS', '2020-06-02 00:00:00', 23, 22221.0, 5, 1, 0, 0, ' ', ' ', 0.0, 'Sudeste', 'SP', 'Borborema', 35, 350740, 35032, 'CENTRO OESTE DO DRS III', '2020-08-07 00:00:00', 32, 16046.0, 61, 2, 1, 0, ' ', ' ', 0.0, 'Norte', 'TO', 'Aparecida do Rio Negro', 17, 170110, 17006, 'CAPIM DOURADO', '2020-04-22 00:00:00', 17, 4795.0, 0, 0, 0, 0, ' ', ' ', 1.0, 'Norte', 'TO', 'Santa Maria do Tocantins', 17, 171888, 17004, 'CERRADO TOCANTINS ARAGUAIA', '2020-04-13 00:00:00', 16, 3434.0, 0, 0, 0, 0, ' ', ' ', 0.0}
print(dicionario)

#Letra L: extrair os dados de Teresina/PI apresentando os casos novos com um print
dicTeresina = {'Região':'Nordeste', 'Estado':'PI', 'Município':'Teresina', 'Código UF' : 22, 'Código Município':221100, 'Código Região':22004, 'Região de Saúde':'ENTRE RIOS', 'Data':'31/08/2020', 'Semana':36, 'População':864845, 'Casos Acumulados':25115, 'Casos Novos':45, 'Óbitos Acumulados':908, 'Óbitos Novos':3, 'Interior':1}
print('Casos novos em Teresina/PI no dia 31/08/2020: ',dicTeresina['Casos Novos'])