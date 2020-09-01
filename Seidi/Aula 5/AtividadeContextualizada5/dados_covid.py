# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:41:14 2020

@author: seidi
"""

# variáveis globais
ind_regiao            = 0 
ind_estado            = 1 
ind_municipio         = 2
#ind_coduf            = 3
#ind_codmun           = 4
ind_codRegiaoSaude    = 5 
ind_nomeRegiaoSaude   = 6
#ind_data             = 7 
#semanaEpi            = 8
#populacaoTCU2019     = 9
ind_casosAcumulado    = 10
ind_casosNovos        = 11
ind_obitosAcumulado   = 12
ind_obitosNovos       = 13
ind_Recuperadosnovos  = 14
#ind_emAcompanhamentoNovos = 15
#ind_interior_metropolitana = 16



# a. Realize o download dos dados de forma manual e crie uma lista e uma tupla com as
#informações disponíveis no documento csv (coloque pelo menos 1 linha por estado e 10
#regiões de saúde diferentes, algo próximo de umas 40 linhas).
print('_'*80)
print('item a - criação de dados em lista e tupla')
lista_covid = [['Norte', 			'AC', 'Porto Walter', 				12, 120039, 12003, 'JURUA E TARAUACA/ENVIRA', 				'2020-08-29 00:00:00', 35, 11982.0, 258, 10, 2, 0, ' ', ' ', 0.0], 
               ['Norte', 			'AC', 'Santa Rosa do Purus', 		12, 120043, 12002, 'BAIXO ACRE E PURUS', 					'2020-08-29 00:00:00', 35, 6540.0, 274, 0, 2, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'AL', 'Minador do Negrão', 			27, 270530, 27008, '8ª REGIAO DE SAUDE', 					'2020-08-29 00:00:00', 35, 5329.0, 12, 0, 0, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'AL', 'Penedo', 					27, 270670, 27006, '6ª REGIAO DE SAUDE', 					'2020-08-29 00:00:00', 35, 63683.0, 1196, 3, 13, 0, ' ', ' ', 0.0], 
               ['Norte', 			'AM', 'Barcelos', 					13, 130040, 13001, 'MANAUS, ENTORNO E ALTO RIO NEGRO', 		'2020-08-29 00:00:00', 35, 27502.0, 2506, 88, 24, 0, ' ', ' ', 0.0], 
               ['Norte', 			'AM', 'Barreirinha', 				13, 130050, 13005, 'BAIXO AMAZONAS', 						'2020-08-29 00:00:00', 35, 32041.0, 858, 2, 12, 0, ' ', ' ', 0.0], 
               ['Norte', 			'AP', 'Mazagão', 					16, 160040, 16003, 'AREA SUDOESTE', 						'2020-08-29 00:00:00', 35, 21632.0, 1354, 0, 8, 0, ' ', ' ', 1.0], 
               ['Norte', 			'AP', 'Mazagão', 					16, 160040, 16003, 'AREA SUDOESTE', 						'2020-08-29 00:00:00', 35, 21632.0, 1354, 0, 8, 0, ' ', ' ', 1.0], 
               ['Nordeste', 		'BA', 'Pilão Arcado', 				29, 292440, 29016, 'JUAZEIRO', 								'2020-08-29 00:00:00', 35, 35048.0, 89, 1, 0, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'BA', 'Castro Alves', 				29, 290730, 29022, 'SANTO ANTONIO DE JESUS', 				'2020-08-29 00:00:00', 35, 26264.0, 333, 7, 4, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'CE', 'Ibicuitinga', 				23, 230533, 23008, '8ª REGIAO QUIXADA', 					'2020-08-29 00:00:00', 35, 12525.0, 441, 0, 6, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'CE', 'Granja', 					23, 230470, 23016, '16ª REGIAO CAMOCIM', 					'2020-08-29 00:00:00', 35, 54748.0, 1231, 2, 41, 0, ' ', ' ', 0.0], 
               ['Centro-Oeste', 	'DF', 'Brasília', 					53, 530010, 53001, 'DISTRITO FEDERAL', 						'2020-08-29 00:00:00', 35, 3015268.0, 159526, 1346, 2250, -190, ' ', ' ', 1.0], 
               ['Sudeste', 	    	'ES', 'Castelo', 					32, 320140, 32004, 'SUL', 									'2020-08-29 00:00:00', 35, 37534.0, 1212, 2, 28, 0, ' ', ' ', 0.0], 
               ['Sudeste', 	    	'ES', 'Pedro Canário', 				32, 320405, 32003, 'NORTE', 								'2020-08-29 00:00:00', 35, 26184.0, 456, 3, 14, 0, ' ', ' ', 0.0], 
               ['Centro-Oeste', 	'GO', 'Novo Brasil', 				52, 521520, 52009, 'OESTE I', 								'2020-08-29 00:00:00', 35, 2913.0, 15, 0, 0, 0, ' ', ' ', 0.0], 
               ['Centro-Oeste', 	'GO', 'Maurilândia', 				52, 521300, 52015, 'SUDOESTE I', 							'2020-08-29 00:00:00', 35, 14080.0, 222, 10, 3, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'MA', 'Passagem Franca', 			21, 210790, 21015, 'SAO JOAO DOS PATOS', 					'2020-08-29 00:00:00', 35, 19019.0, 233, 1, 0, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'MA', 'Timon', 						21, 211220, 21017, 'TIMON', 								'2020-08-29 00:00:00', 35, 169107.0, 3613, 14, 103, 2, ' ', ' ', 0.0], 
               ['Sudeste', 	    	'MG', 'Buritizeiro', 				31, 310940, 31055, 'PIRAPORA', 								'2020-08-29 00:00:00', 35, 28056.0, 184, 9, 5, 0, ' ', ' ', 0.0], 
               ['Sudeste', 	    	'MG', 'Paulistas', 					31, 314840, 31080, 'PECANHA/SAO JOAO EVANGELISTA', 			'2020-08-29 00:00:00', 35, 4830.0, 1, 0, 0, 0, ' ', ' ', 0.0], 
               ['Centro-Oeste', 	'MS', 'Fátima do Sul', 				50, 500380, 50003, 'DOURADOS', 								'2020-08-29 00:00:00', 35, 19189.0, 354, 12, 9, 0, ' ', ' ', 0.0], 
               ['Centro-Oeste', 	'MS', 'Caarapó', 					50, 500240, 50003, 'DOURADOS', 								'2020-08-29 00:00:00', 35, 30174.0, 330, 4, 1, 0, ' ', ' ', 0.0], 
               ['Centro-Oeste', 	'MT', 'Castanheira', 				51, 510285, 51008, 'NOROESTE MATOGROSSENSE', 				'2020-08-29 00:00:00', 35, 8729.0, 72, 0, 2, 0, ' ', ' ', 0.0], 
               ['Centro-Oeste', 	'MT', 'Nova Canaã do Norte', 		51, 510621, 51010, 'NORTE MATOGROSSENSE', 					'2020-08-29 00:00:00', 35, 12787.0, 156, 0, 3, 0, ' ', ' ', 0.0], 
               ['Norte', 			'PA', 'Oeiras do Pará', 			15, 150520, 15011, 'TOCANTINS', 							'2020-08-29 00:00:00', 35, 32512.0, 485, 0, 21, 0, ' ', ' ', 0.0], 
               ['Norte', 			'PA', 'Palestina do Pará', 			15, 150549, 15003, 'CARAJAS', 								'2020-08-29 00:00:00', 35, 7589.0, 243, 5, 3, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'PB', 'Boa Vista', 					25, 250215, 25016, '16ª REGIAO', 							'2020-08-29 00:00:00', 35, 7051.0, 102, 1, 1, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'PB', 'Juazeirinho', 				25, 250770, 25016, '16ª REGIAO', 							'2020-08-29 00:00:00', 35, 18171.0, 220, 3, 1, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'PE', 'Serra Talhada', 				26, 261390, 26012, 'SERRA TALHADA', 						'2020-08-29 00:00:00', 35, 86350.0, 3159, 20, 49, 1, ' ', ' ', 0.0], 
               ['Nordeste', 		'PE', 'Bom Jardim', 				26, 260220, 26006, 'LIMOEIRO', 								'2020-08-29 00:00:00', 35, 39184.0, 612, 18, 26, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'PI', 'Curimatá',					22, 220320, 22002, 'CHAPADA DAS MANGABEIRAS', 				'2020-08-29 00:00:00', 35, 11388.0, 140, 2, 1, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'PI', 'Madeiro', 					22, 220585, 22003, 'COCAIS', 								'2020-08-29 00:00:00', 35, 8310.0, 352, 0, 2, 0, ' ', ' ', 0.0], 
               ['Sul', 		     	'PR', 'Mallet', 					41, 411390, 41004, '4ª RS IRATI', 							'2020-08-29 00:00:00', 35, 13630.0, 49, 0, 2, 0, ' ', ' ', 0.0], 
               ['Sul', 		     	'PR', 'Sulina', 					41, 412665, 41007, '7ª RS PATO BRANCO', 					'2020-08-29 00:00:00', 35, 2981.0, 34, 0, 0, 0, ' ', ' ', 0.0], 
               ['Sudeste', 	    	'RJ', 'Macaé', 						33, 330240, 33008, 'NORTE', 								'2020-08-29 00:00:00', 35, 256672.0, 6994, 71, 134, 2, ' ', ' ', 0.0], 
               ['Sudeste', 	    	'RJ', 'Sapucaia', 					33, 330540, 33003, 'CENTRO-SUL',						 	'2020-08-29 00:00:00', 35, 18228.0, 332, 3, 23, 0, ' ', ' ', 0.0], 
               ['Nordeste',	    	'RN', 'Doutor Severiano', 			24, 240320, 24006, '6ª REGIAO DE SAUDE - PAU DOS FERROS', 	'2020-08-29 00:00:00', 35, 7076.0, 32, 0, 1, 0, ' ', ' ', 0.0], 
               ['Nordeste',	    	'RN', 'Portalegre', 				24, 241020, 24006, '6ª REGIAO DE SAUDE - PAU DOS FERROS', 	'2020-08-29 00:00:00', 35, 7867.0, 33, 0, 0, 0, ' ', ' ', 0.0], 
               ['Norte', 			'RO', 'Campo Novo de Rondônia', 	11, 110070, 11001, 'VALE DO JAMARI', 						'2020-08-29 00:00:00', 35, 14139.0, 133, 0, 5, 0, ' ', ' ', 0.0], 
               ['Norte', 			'RO', 'Cujubim', 					11, 110094, 11001, 'VALE DO JAMARI', 						'2020-08-29 00:00:00', 35, 25215.0, 243, 0, 6, 0, ' ', ' ', 0.0], 
               ['Norte', 			'RR', 'Cantá', 						14, 140017, 14001, 'CENTRO NORTE', 							'2020-08-29 00:00:00', 35, 18335.0, 898, 7, 9, 0, ' ', ' ', 1.0], 
               ['Norte', 			'RR', 'Bonfim', 					14, 140015, 14001, 'CENTRO NORTE',							'2020-08-29 00:00:00', 35, 12409.0, 699, 1, 11, 0, ' ', ' ', 1.0], 
               ['Sul', 		     	'RS', 'Cristal do Sul', 			43, 430607, 43015, 'REGIAO 15', 							'2020-08-29 00:00:00', 35, 2847.0, 19, 1, 0, 0, ' ', ' ', 0.0], 
               ['Sul', 		     	'RS', 'Frederico Westphalen', 		43, 430850, 43015, 'REGIAO 15', 							'2020-08-29 00:00:00', 35, 31313.0, 583, 5, 9, 1, ' ', ' ', 0.0], 
               ['Sul', 		     	'SC', 'Guarujá do Sul', 			42, 420660, 42001, 'EXTREMO OESTE', 						'2020-08-29 00:00:00', 35, 5160.0, 7, 0, 0, 0, ' ', ' ', 0.0], 
               ['Sul', 		     	'SC', 'Antônio Carlos', 			42, 420120, 42007, 'GRANDE FLORIANOPOLIS', 					'2020-08-29 00:00:00', 35, 8513.0, 233, 2, 11, 0, ' ', ' ', 1.0], 
               ['Nordeste', 		'SE', 'Indiaroba', 					28, 280280, 28002, 'ESTANCIA', 								'2020-08-29 00:00:00', 35, 17957.0, 154, 0, 11, 0, ' ', ' ', 0.0], 
               ['Nordeste', 		'SE', 'Tobias Barreto', 			28, 280740, 28004, 'LAGARTO', 								'2020-08-29 00:00:00', 35, 52191.0, 1517, 6, 35, 0, ' ', ' ', 0.0], 
               ['Sudeste', 	    	'SP', 'Arujá', 						35, 350390, 35011, 'ALTO DO TIETE', 						'2020-08-29 00:00:00', 35, 89824.0, 1573, 6, 69, 0, ' ', ' ', 1.0], 
               ['Sudeste', 	    	'SP', 'Ribeirão do Sul', 			35, 354320, 35094, 'OURINHOS', 								'2020-08-29 00:00:00', 35, 4541.0, 25, 0, 1, 0, ' ', ' ', 0.0], 
               ['Norte', 			'TO', 'Bandeirantes do Tocantins', 	17, 170305, 17004, 'CERRADO TOCANTINS ARAGUAIA', 			'2020-08-29 00:00:00', 35, 3553.0, 32, 0, 1, 0, ' ', ' ', 0.0], 
               ['Norte', 			'TO', 'Palmeirante', 				17, 171570, 17004, 'CERRADO TOCANTINS ARAGUAIA', 			'2020-08-29 00:00:00', 35, 6026.0, 133, 1, 3, 0, ' ', ' ', 0.0],
			   ['Nordeste',			'PI', 'Teresina',					22,	221100,	22004, 'ENTRE RIOS',							'2020-08-18 00:00:00', 34, 864845.0, 22102,	299, 833, 7,'','',1],
               ['Sudeste',			'RJ', '',							33,	'',	'',	'',										        '2020-08-29 00:00:00', 35, 17264943,222957,	3759, 16016,157,'','','']]

tupla_covid = (('Norte', 			'AC', 'Porto Walter', 				12, 120039, 12003, 'JURUA E TARAUAestadCA/ENVIRA', 				'2020-08-29 00:00:00', 35, 11982.0, 258, 10, 2, 0, ' ', ' ', 0.0), 
               ('Norte', 			'AC', 'Santa Rosa do Purus', 		12, 120043, 12002, 'BAIXO ACRE E PURUS', 					'2020-08-29 00:00:00', 35, 6540.0, 274, 0, 2, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'AL', 'Minador do Negrão', 			27, 270530, 27008, '8ª REGIAO DE SAUDE', 					'2020-08-29 00:00:00', 35, 5329.0, 12, 0, 0, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'AL', 'Penedo', 					27, 270670, 27006, '6ª REGIAO DE SAUDE', 					'2020-08-29 00:00:00', 35, 63683.0, 1196, 3, 13, 0, ' ', ' ', 0.0), 
               ('Norte', 			'AM', 'Barcelos', 					13, 130040, 13001, 'MANAUS, ENTORNO E ALTO RIO NEGRO', 		'2020-08-29 00:00:00', 35, 27502.0, 2506, 88, 24, 0, ' ', ' ', 0.0), 
               ('Norte', 			'AM', 'Barreirinha', 				13, 130050, 13005, 'BAIXO AMAZONAS', 						'2020-08-29 00:00:00', 35, 32041.0, 858, 2, 12, 0, ' ', ' ', 0.0), 
               ('Norte', 			'AP', 'Mazagão', 					16, 160040, 16003, 'AREA SUDOESTE', 						'2020-08-29 00:00:00', 35, 21632.0, 1354, 0, 8, 0, ' ', ' ', 1.0), 
               ('Norte', 			'AP', 'Mazagão', 					16, 160040, 16003, 'AREA SUDOESTE', 						'2020-08-29 00:00:00', 35, 21632.0, 1354, 0, 8, 0, ' ', ' ', 1.0), 
               ('Nordeste', 		'BA', 'Pilão Arcado', 				29, 292440, 29016, 'JUAZEIRO', 								'2020-08-29 00:00:00', 35, 35048.0, 89, 1, 0, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'BA', 'Castro Alves', 				29, 290730, 29022, 'SANTO ANTONIO DE JESUS', 				'2020-08-29 00:00:00', 35, 26264.0, 333, 7, 4, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'CE', 'Ibicuitinga', 				23, 230533, 23008, '8ª REGIAO QUIXADA', 					'2020-08-29 00:00:00', 35, 12525.0, 441, 0, 6, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'CE', 'Granja', 					23, 230470, 23016, '16ª REGIAO CAMOCIM', 					'2020-08-29 00:00:00', 35, 54748.0, 1231, 2, 41, 0, ' ', ' ', 0.0), 
               ('Centro-Oeste', 	'DF', 'Brasília', 					53, 530010, 53001, 'DISTRITO FEDERAL', 						'2020-08-29 00:00:00', 35, 3015268.0, 159526, 1346, 2250, -190, ' ', ' ', 1.0), 
               ('Sudeste', 	    	'ES', 'Castelo', 					32, 320140, 32004, 'SUL', 									'2020-08-29 00:00:00', 35, 37534.0, 1212, 2, 28, 0, ' ', ' ', 0.0), 
               ('Sudeste', 	    	'ES', 'Pedro Canário', 				32, 320405, 32003, 'NORTE', 								'2020-08-29 00:00:00', 35, 26184.0, 456, 3, 14, 0, ' ', ' ', 0.0), 
               ('Centro-Oeste', 	'GO', 'Novo Brasil', 				52, 521520, 52009, 'OESTE I', 								'2020-08-29 00:00:00', 35, 2913.0, 15, 0, 0, 0, ' ', ' ', 0.0), 
               ('Centro-Oeste', 	'GO', 'Maurilândia', 				52, 521300, 52015, 'SUDOESTE I', 							'2020-08-29 00:00:00', 35, 14080.0, 222, 10, 3, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'MA', 'Passagem Franca', 			21, 210790, 21015, 'SAO JOAO DOS PATOS', 					'2020-08-29 00:00:00', 35, 19019.0, 233, 1, 0, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'MA', 'Timon', 						21, 211220, 21017, 'TIMON', 								'2020-08-29 00:00:00', 35, 169107.0, 3613, 14, 103, 2, ' ', ' ', 0.0), 
               ('Sudeste', 	    	'MG', 'Buritizeiro', 				31, 310940, 31055, 'PIRAPORA', 								'2020-08-29 00:00:00', 35, 28056.0, 184, 9, 5, 0, ' ', ' ', 0.0), 
               ('Sudeste', 	    	'MG', 'Paulistas', 					31, 314840, 31080, 'PECANHA/SAO JOAO EVANGELISTA', 			'2020-08-29 00:00:00', 35, 4830.0, 1, 0, 0, 0, ' ', ' ', 0.0), 
               ('Centro-Oeste', 	'MS', 'Fátima do Sul', 				50, 500380, 50003, 'DOURADOS', 								'2020-08-29 00:00:00', 35, 19189.0, 354, 12, 9, 0, ' ', ' ', 0.0), 
               ('Centro-Oeste', 	'MS', 'Caarapó', 					50, 500240, 50003, 'DOURADOS', 								'2020-08-29 00:00:00', 35, 30174.0, 330, 4, 1, 0, ' ', ' ', 0.0), 
               ('Centro-Oeste', 	'MT', 'Castanheira', 				51, 510285, 51008, 'NOROESTE MATOGROSSENSE', 				'2020-08-29 00:00:00', 35, 8729.0, 72, 0, 2, 0, ' ', ' ', 0.0), 
               ('Centro-Oeste', 	'MT', 'Nova Canaã do Norte', 		51, 510621, 51010, 'NORTE MATOGROSSENSE', 					'2020-08-29 00:00:00', 35, 12787.0, 156, 0, 3, 0, ' ', ' ', 0.0), 
               ('Norte', 			'PA', 'Oeiras do Pará', 			15, 150520, 15011, 'TOCANTINS', 							'2020-08-29 00:00:00', 35, 32512.0, 485, 0, 21, 0, ' ', ' ', 0.0), 
               ('Norte', 			'PA', 'Palestina do Pará', 			15, 150549, 15003, 'CARAJAS', 								'2020-08-29 00:00:00', 35, 7589.0, 243, 5, 3, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'PB', 'Boa Vista', 					25, 250215, 25016, '16ª REGIAO', 							'2020-08-29 00:00:00', 35, 7051.0, 102, 1, 1, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'PB', 'Juazeirinho', 				25, 250770, 25016, '16ª REGIAO', 							'2020-08-29 00:00:00', 35, 18171.0, 220, 3, 1, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'PE', 'Serra Talhada', 				26, 261390, 26012, 'SERRA TALHADA', 						'2020-08-29 00:00:00', 35, 86350.0, 3159, 20, 49, 1, ' ', ' ', 0.0), 
               ('Nordeste', 		'PE', 'Bom Jardim', 				26, 260220, 26006, 'LIMOEIRO', 								'2020-08-29 00:00:00', 35, 39184.0, 612, 18, 26, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'PI', 'Curimatá',					22, 220320, 22002, 'CHAPADA DAS MANGABEIRAS', 				'2020-08-29 00:00:00', 35, 11388.0, 140, 2, 1, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'PI', 'Madeiro', 					22, 220585, 22003, 'COCAIS', 								'2020-08-29 00:00:00', 35, 8310.0, 352, 0, 2, 0, ' ', ' ', 0.0), 
               ('Sul', 		     	'PR', 'Mallet', 					41, 411390, 41004, '4ª RS IRATI', 							'2020-08-29 00:00:00', 35, 13630.0, 49, 0, 2, 0, ' ', ' ', 0.0), 
               ('Sul', 		     	'PR', 'Sulina', 					41, 412665, 41007, '7ª RS PATO BRANCO', 					'2020-08-29 00:00:00', 35, 2981.0, 34, 0, 0, 0, ' ', ' ', 0.0), 
               ('Sudeste', 	    	'RJ', 'Macaé', 						33, 330240, 33008, 'NORTE', 								'2020-08-29 00:00:00', 35, 256672.0, 6994, 71, 134, 2, ' ', ' ', 0.0), 
               ('Sudeste', 	    	'RJ', 'Sapucaia', 					33, 330540, 33003, 'CENTRO-SUL',						 	'2020-08-29 00:00:00', 35, 18228.0, 332, 3, 23, 0, ' ', ' ', 0.0), 
               ('Nordeste',	    	'RN', 'Doutor Severiano', 			24, 240320, 24006, '6ª REGIAO DE SAUDE - PAU DOS FERROS', 	'2020-08-29 00:00:00', 35, 7076.0, 32, 0, 1, 0, ' ', ' ', 0.0), 
               ('Nordeste',	    	'RN', 'Portalegre', 				24, 241020, 24006, '6ª REGIAO DE SAUDE - PAU DOS FERROS', 	'2020-08-29 00:00:00', 35, 7867.0, 33, 0, 0, 0, ' ', ' ', 0.0), 
               ('Norte', 			'RO', 'Campo Novo de Rondônia', 	11, 110070, 11001, 'VALE DO JAMARI', 						'2020-08-29 00:00:00', 35, 14139.0, 133, 0, 5, 0, ' ', ' ', 0.0), 
               ('Norte', 			'RO', 'Cujubim', 					11, 110094, 11001, 'VALE DO JAMARI', 						'2020-08-29 00:00:00', 35, 25215.0, 243, 0, 6, 0, ' ', ' ', 0.0), 
               ('Norte', 			'RR', 'Cantá', 						14, 140017, 14001, 'CENTRO NORTE', 							'2020-08-29 00:00:00', 35, 18335.0, 898, 7, 9, 0, ' ', ' ', 1.0), 
               ('Norte', 			'RR', 'Bonfim', 					14, 140015, 14001, 'CENTRO NORTE',							'2020-08-29 00:00:00', 35, 12409.0, 699, 1, 11, 0, ' ', ' ', 1.0), 
               ('Sul', 		     	'RS', 'Cristal do Sul', 			43, 430607, 43015, 'REGIAO 15', 							'2020-08-29 00:00:00', 35, 2847.0, 19, 1, 0, 0, ' ', ' ', 0.0), 
               ('Sul', 		     	'RS', 'Frederico Westphalen', 		43, 430850, 43015, 'REGIAO 15', 							'2020-08-29 00:00:00', 35, 31313.0, 583, 5, 9, 1, ' ', ' ', 0.0), 
               ('Sul', 		     	'SC', 'Guarujá do Sul', 			42, 420660, 42001, 'EXTREMO OESTE', 						'2020-08-29 00:00:00', 35, 5160.0, 7, 0, 0, 0, ' ', ' ', 0.0), 
               ('Sul', 		     	'SC', 'Antônio Carlos', 			42, 420120, 42007, 'GRANDE FLORIANOPOLIS', 					'2020-08-29 00:00:00', 35, 8513.0, 233, 2, 11, 0, ' ', ' ', 1.0), 
               ('Nordeste', 		'SE', 'Indiaroba', 					28, 280280, 28002, 'ESTANCIA', 								'2020-08-29 00:00:00', 35, 17957.0, 154, 0, 11, 0, ' ', ' ', 0.0), 
               ('Nordeste', 		'SE', 'Tobias Barreto', 			28, 280740, 28004, 'LAGARTO', 								'2020-08-29 00:00:00', 35, 52191.0, 1517, 6, 35, 0, ' ', ' ', 0.0), 
               ('Sudeste', 	    	'SP', 'Arujá', 						35, 350390, 35011, 'ALTO DO TIETE', 						'2020-08-29 00:00:00', 35, 89824.0, 1573, 6, 69, 0, ' ', ' ', 1.0), 
               ('Sudeste', 	    	'SP', 'Ribeirão do Sul', 			35, 354320, 35094, 'OURINHOS', 								'2020-08-29 00:00:00', 35, 4541.0, 25, 0, 1, 0, ' ', ' ', 0.0), 
               ('Norte', 			'TO', 'Bandeirantes do Tocantins', 	17, 170305, 17004, 'CERRADO TOCANTINS ARAGUAIA', 			'2020-08-29 00:00:00', 35, 3553.0, 32, 0, 1, 0, ' ', ' ', 0.0), 
               ('Norte', 			'TO', 'Palmeirante', 				17, 171570, 17004, 'CERRADO TOCANTINS ARAGUAIA', 			'2020-08-29 00:00:00', 35, 6026.0, 133, 1, 3, 0, ' ', ' ', 0.0),
			   ('Nordeste',			'PI', 'Teresina',					22,	221100,	22004, 'ENTRE RIOS',							'2020-08-18 00:00:00', 34, 864845.0, 22102,	299, 833, 7,'','',1),
               ('Sudeste',			'RJ', '',							33,	'',	'',	'',										        '2020-08-29 00:00:00', 35, 17264943,222957,	3759, 16016,157,'','',''))


print('Gerada lista de dados covid')
print('Tamanho total da lista: ', len(lista_covid))
print('')


# b. Mande printar na tela o número de casos acumulados para o estado do rio de janeiro
#tanto para a tupla quanto para a lista.

print('_'*80)
print('item b - casos acumulados no estado do Rio de Janeiro')
print('Casos acumulados no estado do Rio de Janeiro (lista_covid):', lista_covid[-1][ind_casosAcumulado])
print('Casos acumulados no estado do Rio de Janeiro (tupla_covid):', tupla_covid[-1][ind_casosAcumulado])
print('')

# c. Apresente na tela todos os óbitos acumulados mostrando os casos apenas para o caso
#dos estados (sem mostrar regiões de saúde, etc..).

print('_'*80)
print('item c - óbitos acumulados nos estados')
print('Casos acumulados no estado', lista_covid[0][ind_estado],  ', município ',lista_covid[0][ind_municipio], ':',lista_covid[0][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[1][ind_estado],  ', município ',lista_covid[1][ind_municipio], ':',lista_covid[1][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[2][ind_estado],  ', município ',lista_covid[2][ind_municipio], ':',lista_covid[2][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[3][ind_estado],  ', município ',lista_covid[3][ind_municipio], ':',lista_covid[3][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[4][ind_estado],  ', município ',lista_covid[4][ind_municipio], ':',lista_covid[4][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[5][ind_estado],  ', município ',lista_covid[5][ind_municipio], ':',lista_covid[5][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[6][ind_estado],  ', município ',lista_covid[6][ind_municipio], ':',lista_covid[6][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[7][ind_estado],  ', município ',lista_covid[7][ind_municipio], ':',lista_covid[7][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[8][ind_estado],  ', município ',lista_covid[8][ind_municipio], ':',lista_covid[8][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[9][ind_estado],  ', município ',lista_covid[9][ind_municipio], ':',lista_covid[9][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[10][ind_estado], ', município ',lista_covid[10][ind_municipio],':',lista_covid[10][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[11][ind_estado], ', município ',lista_covid[11][ind_municipio],':',lista_covid[11][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[12][ind_estado], ', município ',lista_covid[12][ind_municipio],':',lista_covid[12][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[13][ind_estado], ', município ',lista_covid[13][ind_municipio],':',lista_covid[13][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[14][ind_estado], ', município ',lista_covid[14][ind_municipio],':',lista_covid[14][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[15][ind_estado], ', município ',lista_covid[15][ind_municipio],':',lista_covid[15][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[16][ind_estado], ', município ',lista_covid[16][ind_municipio],':',lista_covid[16][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[17][ind_estado], ', município ',lista_covid[17][ind_municipio],':',lista_covid[17][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[18][ind_estado], ', município ',lista_covid[18][ind_municipio],':',lista_covid[18][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[19][ind_estado], ', município ',lista_covid[19][ind_municipio],':',lista_covid[19][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[20][ind_estado], ', município ',lista_covid[20][ind_municipio],':',lista_covid[20][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[21][ind_estado], ', município ',lista_covid[21][ind_municipio],':',lista_covid[21][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[22][ind_estado], ', município ',lista_covid[22][ind_municipio],':',lista_covid[22][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[23][ind_estado], ', município ',lista_covid[23][ind_municipio],':',lista_covid[23][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[24][ind_estado], ', município ',lista_covid[24][ind_municipio],':',lista_covid[24][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[25][ind_estado], ', município ',lista_covid[25][ind_municipio],':',lista_covid[25][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[26][ind_estado], ', município ',lista_covid[26][ind_municipio],':',lista_covid[26][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[27][ind_estado], ', município ',lista_covid[27][ind_municipio],':',lista_covid[27][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[28][ind_estado], ', município ',lista_covid[28][ind_municipio],':',lista_covid[28][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[29][ind_estado], ', município ',lista_covid[29][ind_municipio],':',lista_covid[29][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[30][ind_estado], ', município ',lista_covid[30][ind_municipio],':',lista_covid[30][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[31][ind_estado], ', município ',lista_covid[31][ind_municipio],':',lista_covid[31][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[32][ind_estado], ', município ',lista_covid[32][ind_municipio],':',lista_covid[32][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[33][ind_estado], ', município ',lista_covid[33][ind_municipio],':',lista_covid[33][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[34][ind_estado], ', município ',lista_covid[34][ind_municipio],':',lista_covid[34][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[35][ind_estado], ', município ',lista_covid[35][ind_municipio],':',lista_covid[35][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[36][ind_estado], ', município ',lista_covid[36][ind_municipio],':',lista_covid[36][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[37][ind_estado], ', município ',lista_covid[37][ind_municipio],':',lista_covid[37][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[38][ind_estado], ', município ',lista_covid[38][ind_municipio],':',lista_covid[38][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[39][ind_estado], ', município ',lista_covid[39][ind_municipio],':',lista_covid[39][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[40][ind_estado], ', município ',lista_covid[40][ind_municipio],':',lista_covid[40][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[41][ind_estado], ', município ',lista_covid[41][ind_municipio],':',lista_covid[41][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[42][ind_estado], ', município ',lista_covid[42][ind_municipio],':',lista_covid[42][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[43][ind_estado], ', município ',lista_covid[43][ind_municipio],':',lista_covid[43][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[44][ind_estado], ', município ',lista_covid[44][ind_municipio],':',lista_covid[44][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[45][ind_estado], ', município ',lista_covid[45][ind_municipio],':',lista_covid[45][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[46][ind_estado], ', município ',lista_covid[46][ind_municipio],':',lista_covid[46][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[47][ind_estado], ', município ',lista_covid[47][ind_municipio],':',lista_covid[47][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[48][ind_estado], ', município ',lista_covid[48][ind_municipio],':',lista_covid[48][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[49][ind_estado], ', município ',lista_covid[49][ind_municipio],':',lista_covid[49][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[50][ind_estado], ', município ',lista_covid[50][ind_municipio],':',lista_covid[50][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[51][ind_estado], ', município ',lista_covid[51][ind_municipio],':',lista_covid[51][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[52][ind_estado], ', município ',lista_covid[52][ind_municipio],':',lista_covid[52][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[53][ind_estado], ', município ',lista_covid[53][ind_municipio],':',lista_covid[53][ind_obitosAcumulado])
print('Casos acumulados no estado', lista_covid[54][ind_estado], ', município ',lista_covid[54][ind_municipio],':',lista_covid[54][ind_obitosAcumulado])
print('')


#d. Assuma que os dados de óbitos novos para o estado da paraíba estejam errados em 10
#unidades para menos. Sobrescreva a informação tanto na lista quanto na tupla,
#corrigindo os dados.


print('_'*80)
print('item d - correção de dados de óbitos novos')
print('Acrescentando 10 no número de novos óbitos nos municípios da Paraíba')
ind_paraiba1 = 27 # Boa Vista - PB
ind_paraiba2 = 28 # Juazeirinho - PB
lista_covid[ind_paraiba1][ind_obitosNovos] += 10
lista_covid[ind_paraiba2][ind_obitosNovos] += 10
print('')

#tupla_covid[ind_paraiba1][ind_obitosNovos] += 10 # erro
#tupla_covid[ind_paraiba2][ind_obitosNovos] += 10 # erro

# e. As duas operações foram possíveis (lista e tupla)? Justifique.

print('_'*80)
print('item e - validade da operação em listas e tuplas')
print('Resposta: Não, a operação é válida sobre a estrutura lista, porém não\n\
é válida sobre a tupla, já que esta estrutura é imutável em relação aos dados')
print('')

# f. Crie uma nova lista com apenas dados de 1 estado e todos os municípios e adicione essa
#lista nova a lista já existente (append ou insert).

print('_'*80)
print('item f - criação de lista com dados dos municípios de um estado')
dados_covid_municipios_AC =  [['Norte', 'AC', 'Tarauacá', 12, 120060, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-08-18 00:00:00', 34, 42567.0, 1401, 85, 13, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Rio Branco', 12, 120040, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 407319.0, 9692, 30, 377, 6, ' ', ' ', 1.0], 
    				['Norte', 'AC', 'Manoel Urbano', 12, 120034, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 9459.0, 253, 2, 2, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Cruzeiro do Sul', 12, 120020, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-08-18 00:00:00', 34, 88376.0, 2961, 19, 53, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Epitaciolândia', 12, 120025, 12001, 'ALTO ACRE', '2020-08-18 00:00:00', 34, 18411.0, 456, 15, 11, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Plácido de Castro', 12, 120038, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 19761.0, 386, 0, 8, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Assis Brasil', 12, 120005, 12001, 'ALTO ACRE', '2020-08-18 00:00:00', 34, 7417.0, 440, 1, 9, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Senador Guiomard', 12, 120045, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 23024.0, 401, 2, 10, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Marechal Thaumaturgo', 12, 120035, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-08-18 00:00:00', 34, 18867.0, 287, 3, 1, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Rodrigues Alves', 12, 120042, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-08-18 00:00:00', 34, 18930.0, 137, 0, 6, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Capixaba', 12, 120017, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 11733.0, 240, 1, 7, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Jordão', 12, 120032, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 8317.0, 119, 4, 1, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Brasiléia', 12, 120010, 12001, 'ALTO ACRE', '2020-08-18 00:00:00', 34, 26278.0, 1035, 93, 15, 1, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Bujari', 12, 120013, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 10266.0, 353, 1, 6, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Xapuri', 12, 120070, 12001, 'ALTO ACRE', '2020-08-18 00:00:00', 34, 19323.0, 685, 27, 11, 1, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Mâncio Lima', 12, 120033, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-08-18 00:00:00', 34, 18977.0, 553, 0, 8, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Sena Madureira', 12, 120050, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 45848.0, 1267, 17, 10, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Porto Walter', 12, 120039, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-08-18 00:00:00', 34, 11982.0, 240, 0, 2, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Porto Acre', 12, 120080, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 18504.0, 460, 0, 14, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Acrelândia', 12, 120001, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 15256.0, 398, 20, 8, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Santa Rosa do Purus', 12, 120043, 12002, 'BAIXO ACRE E PURUS', '2020-08-18 00:00:00', 34, 6540.0, 201, 2, 2, 0, ' ', ' ', 0.0], 
    				['Norte', 'AC', 'Feijó', 12, 120030, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-08-18 00:00:00', 34, 34780.0, 968, 6, 16, 0, ' ', ' ', 0.0]]

lista_covid.append(dados_covid_municipios_AC[0])
lista_covid.append(dados_covid_municipios_AC[1])
lista_covid.append(dados_covid_municipios_AC[2])
lista_covid.append(dados_covid_municipios_AC[3])
lista_covid.append(dados_covid_municipios_AC[4])
lista_covid.append(dados_covid_municipios_AC[5])
lista_covid.append(dados_covid_municipios_AC[6])
lista_covid.append(dados_covid_municipios_AC[7])
lista_covid.append(dados_covid_municipios_AC[8])
lista_covid.append(dados_covid_municipios_AC[9])
lista_covid.append(dados_covid_municipios_AC[10])
lista_covid.append(dados_covid_municipios_AC[11])
lista_covid.append(dados_covid_municipios_AC[12])
lista_covid.append(dados_covid_municipios_AC[13])
lista_covid.append(dados_covid_municipios_AC[14])
lista_covid.append(dados_covid_municipios_AC[15])
lista_covid.append(dados_covid_municipios_AC[16])
lista_covid.append(dados_covid_municipios_AC[17])
lista_covid.append(dados_covid_municipios_AC[18])
lista_covid.append(dados_covid_municipios_AC[19])
lista_covid.append(dados_covid_municipios_AC[20])
lista_covid.append(dados_covid_municipios_AC[21])

print('Adicionando dados dos municípios do Acre à lista original (somente as linhas do dia 18/08/2020)')
print('')

# g. Remova da lista os dados das regiões de saúde.

print('_'*80)
print('item g - remoção dos dados das regiões de saúde')
print('Removendo os dados das regiões de saúde')
lista_covid[0].remove(lista_covid[0][ind_nomeRegiaoSaude])
lista_covid[1].remove(lista_covid[1][ind_nomeRegiaoSaude])
lista_covid[2].remove(lista_covid[2][ind_nomeRegiaoSaude])
lista_covid[3].remove(lista_covid[3][ind_nomeRegiaoSaude])
lista_covid[4].remove(lista_covid[4][ind_nomeRegiaoSaude])
lista_covid[5].remove(lista_covid[5][ind_nomeRegiaoSaude])
lista_covid[6].remove(lista_covid[6][ind_nomeRegiaoSaude])
lista_covid[7].remove(lista_covid[7][ind_nomeRegiaoSaude])
lista_covid[8].remove(lista_covid[8][ind_nomeRegiaoSaude])
lista_covid[9].remove(lista_covid[9][ind_nomeRegiaoSaude])
lista_covid[10].remove(lista_covid[10][ind_nomeRegiaoSaude])
lista_covid[11].remove(lista_covid[11][ind_nomeRegiaoSaude])
lista_covid[12].remove(lista_covid[12][ind_nomeRegiaoSaude])
lista_covid[13].remove(lista_covid[13][ind_nomeRegiaoSaude])
lista_covid[14].remove(lista_covid[14][ind_nomeRegiaoSaude])
lista_covid[15].remove(lista_covid[15][ind_nomeRegiaoSaude])
lista_covid[16].remove(lista_covid[16][ind_nomeRegiaoSaude])
lista_covid[17].remove(lista_covid[17][ind_nomeRegiaoSaude])
lista_covid[18].remove(lista_covid[18][ind_nomeRegiaoSaude])
lista_covid[19].remove(lista_covid[19][ind_nomeRegiaoSaude])
lista_covid[20].remove(lista_covid[20][ind_nomeRegiaoSaude])
lista_covid[21].remove(lista_covid[21][ind_nomeRegiaoSaude])
lista_covid[22].remove(lista_covid[22][ind_nomeRegiaoSaude])
lista_covid[23].remove(lista_covid[23][ind_nomeRegiaoSaude])
lista_covid[24].remove(lista_covid[24][ind_nomeRegiaoSaude])
lista_covid[25].remove(lista_covid[25][ind_nomeRegiaoSaude])
lista_covid[26].remove(lista_covid[26][ind_nomeRegiaoSaude])
lista_covid[27].remove(lista_covid[27][ind_nomeRegiaoSaude])
lista_covid[28].remove(lista_covid[28][ind_nomeRegiaoSaude])
lista_covid[29].remove(lista_covid[29][ind_nomeRegiaoSaude])
lista_covid[30].remove(lista_covid[30][ind_nomeRegiaoSaude])
lista_covid[31].remove(lista_covid[31][ind_nomeRegiaoSaude])
lista_covid[32].remove(lista_covid[32][ind_nomeRegiaoSaude])
lista_covid[33].remove(lista_covid[33][ind_nomeRegiaoSaude])
lista_covid[34].remove(lista_covid[34][ind_nomeRegiaoSaude])
lista_covid[35].remove(lista_covid[35][ind_nomeRegiaoSaude])
lista_covid[36].remove(lista_covid[36][ind_nomeRegiaoSaude])
lista_covid[37].remove(lista_covid[37][ind_nomeRegiaoSaude])
lista_covid[38].remove(lista_covid[38][ind_nomeRegiaoSaude])
lista_covid[39].remove(lista_covid[39][ind_nomeRegiaoSaude])
lista_covid[40].remove(lista_covid[40][ind_nomeRegiaoSaude])
lista_covid[41].remove(lista_covid[41][ind_nomeRegiaoSaude])
lista_covid[42].remove(lista_covid[42][ind_nomeRegiaoSaude])
lista_covid[43].remove(lista_covid[43][ind_nomeRegiaoSaude])
lista_covid[44].remove(lista_covid[44][ind_nomeRegiaoSaude])
lista_covid[45].remove(lista_covid[45][ind_nomeRegiaoSaude])
lista_covid[46].remove(lista_covid[46][ind_nomeRegiaoSaude])
lista_covid[47].remove(lista_covid[47][ind_nomeRegiaoSaude])
lista_covid[48].remove(lista_covid[48][ind_nomeRegiaoSaude])
lista_covid[49].remove(lista_covid[49][ind_nomeRegiaoSaude])
lista_covid[50].remove(lista_covid[50][ind_nomeRegiaoSaude])
lista_covid[51].remove(lista_covid[51][ind_nomeRegiaoSaude])
lista_covid[52].remove(lista_covid[52][ind_nomeRegiaoSaude])
lista_covid[53].remove(lista_covid[53][ind_nomeRegiaoSaude])
lista_covid[54].remove(lista_covid[54][ind_nomeRegiaoSaude])
lista_covid[55].remove(lista_covid[55][ind_nomeRegiaoSaude])
lista_covid[56].remove(lista_covid[56][ind_nomeRegiaoSaude])
lista_covid[57].remove(lista_covid[57][ind_nomeRegiaoSaude])
lista_covid[58].remove(lista_covid[58][ind_nomeRegiaoSaude])
lista_covid[59].remove(lista_covid[59][ind_nomeRegiaoSaude])
lista_covid[60].remove(lista_covid[60][ind_nomeRegiaoSaude])
lista_covid[61].remove(lista_covid[61][ind_nomeRegiaoSaude])
lista_covid[62].remove(lista_covid[62][ind_nomeRegiaoSaude])
lista_covid[63].remove(lista_covid[63][ind_nomeRegiaoSaude])
lista_covid[64].remove(lista_covid[64][ind_nomeRegiaoSaude])
lista_covid[65].remove(lista_covid[65][ind_nomeRegiaoSaude])
lista_covid[66].remove(lista_covid[66][ind_nomeRegiaoSaude])
lista_covid[67].remove(lista_covid[67][ind_nomeRegiaoSaude])
lista_covid[68].remove(lista_covid[68][ind_nomeRegiaoSaude])
lista_covid[69].remove(lista_covid[69][ind_nomeRegiaoSaude])
lista_covid[70].remove(lista_covid[70][ind_nomeRegiaoSaude])
lista_covid[71].remove(lista_covid[71][ind_nomeRegiaoSaude])
lista_covid[72].remove(lista_covid[72][ind_nomeRegiaoSaude])
lista_covid[73].remove(lista_covid[73][ind_nomeRegiaoSaude])
lista_covid[74].remove(lista_covid[74][ind_nomeRegiaoSaude])
lista_covid[75].remove(lista_covid[75][ind_nomeRegiaoSaude])
lista_covid[76].remove(lista_covid[76][ind_nomeRegiaoSaude])

# variáveis globais
ind_regiao            = 0 
ind_estado            = 1 
ind_municipio         = 2
#ind_coduf            = 3
#ind_codmun           = 4
ind_codRegiaoSaude    = 5 
ind_data              = 6
#semanaEpi            = 7
#populacaoTCU2019     = 8
ind_casosAcumulado    = 9
ind_casosNovos        = 10
ind_obitosAcumulado   = 11
ind_obitosNovos       = 12
ind_Recuperadosnovos  = 13
#ind_emAcompanhamentoNovos = 15
#ind_interior_metropolitana = 16
print('')

# h. Verifique se a soma dos dados dos municípios na data de 18/08/2020 é igual ao dado da
#lista, mostrando na tela apenas se for verdadeiro.

# testando com os dados do estado do Acre
print('_'*80)
print('item h -  verificação da soma de dados entre lista de municípios e lista do estado')
dados_covid_estado_AC = ['Norte','AC','',12,'','','','2020-08-18 00:00:00',34,881935,22933,328,590,8,'','','']	
dados_covid_estado_AC.remove(dados_covid_estado_AC[ind_nomeRegiaoSaude])	

# casos acumulados
total_casos_ac_municipios = dados_covid_municipios_AC[0][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[1][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[2][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[3][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[4][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[5][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[6][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[7][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[8][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[9][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[10][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[11][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[12][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[13][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[14][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[15][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[16][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[17][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[18][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[19][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[20][ind_casosAcumulado] +\
                             dados_covid_municipios_AC[21][ind_casosAcumulado]
print('Casos acumulados segundo a soma dos municipio do AC: ', total_casos_ac_municipios)
print('Casos acumulados segundo a contagem do estado do AC: ', dados_covid_estado_AC[ind_casosAcumulado])
print('As contagens são iguais? ', total_casos_ac_municipios == dados_covid_estado_AC[ind_casosAcumulado])

# casos novos
total_casos_novos_municipios = dados_covid_municipios_AC[0][ind_casosNovos] +\
                             dados_covid_municipios_AC[1][ind_casosNovos] +\
                             dados_covid_municipios_AC[2][ind_casosNovos] +\
                             dados_covid_municipios_AC[3][ind_casosNovos] +\
                             dados_covid_municipios_AC[4][ind_casosNovos] +\
                             dados_covid_municipios_AC[5][ind_casosNovos] +\
                             dados_covid_municipios_AC[6][ind_casosNovos] +\
                             dados_covid_municipios_AC[7][ind_casosNovos] +\
                             dados_covid_municipios_AC[8][ind_casosNovos] +\
                             dados_covid_municipios_AC[9][ind_casosNovos] +\
                             dados_covid_municipios_AC[10][ind_casosNovos] +\
                             dados_covid_municipios_AC[11][ind_casosNovos] +\
                             dados_covid_municipios_AC[12][ind_casosNovos] +\
                             dados_covid_municipios_AC[13][ind_casosNovos] +\
                             dados_covid_municipios_AC[14][ind_casosNovos] +\
                             dados_covid_municipios_AC[15][ind_casosNovos] +\
                             dados_covid_municipios_AC[16][ind_casosNovos] +\
                             dados_covid_municipios_AC[17][ind_casosNovos] +\
                             dados_covid_municipios_AC[18][ind_casosNovos] +\
                             dados_covid_municipios_AC[19][ind_casosNovos] +\
                             dados_covid_municipios_AC[20][ind_casosNovos] +\
                             dados_covid_municipios_AC[21][ind_casosNovos]
print('\nCasos novos segundo a soma dos municipio do AC: ', total_casos_novos_municipios)
print('Casos novos segundo a contagem do estado do AC: ', dados_covid_estado_AC[ind_casosNovos])
print('As contagens são iguais? ', total_casos_novos_municipios == dados_covid_estado_AC[ind_casosNovos])

# obitos acumulados
total_obitos_ac_municipios = dados_covid_municipios_AC[0][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[1][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[2][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[3][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[4][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[5][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[6][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[7][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[8][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[9][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[10][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[11][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[12][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[13][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[14][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[15][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[16][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[17][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[18][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[19][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[20][ind_obitosAcumulado] +\
                             dados_covid_municipios_AC[21][ind_obitosAcumulado]
print('\nObitos acumulados segundo a soma dos municipio do AC: ', total_obitos_ac_municipios)
print('Obitos acumulados segundo a contagem do estado do AC: ', dados_covid_estado_AC[ind_obitosAcumulado])
print('As contagens são iguais? ', total_obitos_ac_municipios == dados_covid_estado_AC[ind_obitosAcumulado])

# obitos acumulados
total_obitos_novos_municipios = dados_covid_municipios_AC[0][ind_obitosNovos] +\
                             dados_covid_municipios_AC[1][ind_obitosNovos] +\
                             dados_covid_municipios_AC[2][ind_obitosNovos] +\
                             dados_covid_municipios_AC[3][ind_obitosNovos] +\
                             dados_covid_municipios_AC[4][ind_obitosNovos] +\
                             dados_covid_municipios_AC[5][ind_obitosNovos] +\
                             dados_covid_municipios_AC[6][ind_obitosNovos] +\
                             dados_covid_municipios_AC[7][ind_obitosNovos] +\
                             dados_covid_municipios_AC[8][ind_obitosNovos] +\
                             dados_covid_municipios_AC[9][ind_obitosNovos] +\
                             dados_covid_municipios_AC[10][ind_obitosNovos] +\
                             dados_covid_municipios_AC[11][ind_obitosNovos] +\
                             dados_covid_municipios_AC[12][ind_obitosNovos] +\
                             dados_covid_municipios_AC[13][ind_obitosNovos] +\
                             dados_covid_municipios_AC[14][ind_obitosNovos] +\
                             dados_covid_municipios_AC[15][ind_obitosNovos] +\
                             dados_covid_municipios_AC[16][ind_obitosNovos] +\
                             dados_covid_municipios_AC[17][ind_obitosNovos] +\
                             dados_covid_municipios_AC[18][ind_obitosNovos] +\
                             dados_covid_municipios_AC[19][ind_obitosNovos] +\
                             dados_covid_municipios_AC[20][ind_obitosNovos] +\
                             dados_covid_municipios_AC[21][ind_obitosNovos]
print('\nObitos novos segundo a soma dos municipio do AC: ', total_obitos_novos_municipios)
print('Obitos novos segundo a contagem do estado do AC: ', dados_covid_estado_AC[ind_obitosNovos])
print('As contagens são iguais? ', total_obitos_novos_municipios == dados_covid_estado_AC[ind_obitosNovos])
print('')

# i. Retorne o tamanho total da lista.
print('_'*80)
print('item i - tamanho total da lista')
print('Tamanho total da lista: ', len(lista_covid))
print('')

# j. Verifique qual é o maior valor numérico de óbitos novos e o menor valor numérico de
# óbitos novos.

print('_'*80)
print('item j - maior e menos valores de óbitos novos')
# usei list comprehension porque fazer a operação na mão ia ser muito gasto de linha
max_obitos = max(x[ind_obitosNovos] for x in lista_covid)
min_obitos = min(x[ind_obitosNovos] for x in lista_covid if x[ind_obitosNovos] > 0)
print('Maior valor numérico de óbitos novos: ', max_obitos)
print('Menor valor numérico de óbitos novos: ', min_obitos)
print('')

# k. Crie um dicionário de forma que seja possível encontrar os municípios associados a um
#estado específico e extrair os dados de casos novos em apenas um comando.

print('_'*80)
print('item k - criação de dicionário')
print('criando dicionário a partir da lista')
dict_covid = {}
dict_covid[lista_covid[0][ind_municipio]] = lista_covid[0]
dict_covid[lista_covid[1][ind_municipio]] = lista_covid[1]
dict_covid[lista_covid[2][ind_municipio]] = lista_covid[2]
dict_covid[lista_covid[3][ind_municipio]] = lista_covid[3]
dict_covid[lista_covid[4][ind_municipio]] = lista_covid[4]
dict_covid[lista_covid[5][ind_municipio]] = lista_covid[5]
dict_covid[lista_covid[6][ind_municipio]] = lista_covid[6]
dict_covid[lista_covid[7][ind_municipio]] = lista_covid[7]
dict_covid[lista_covid[8][ind_municipio]] = lista_covid[8]
dict_covid[lista_covid[9][ind_municipio]] = lista_covid[9]
dict_covid[lista_covid[10][ind_municipio]] = lista_covid[10]
dict_covid[lista_covid[11][ind_municipio]] = lista_covid[11]
dict_covid[lista_covid[12][ind_municipio]] = lista_covid[12]
dict_covid[lista_covid[13][ind_municipio]] = lista_covid[13]
dict_covid[lista_covid[14][ind_municipio]] = lista_covid[14]
dict_covid[lista_covid[15][ind_municipio]] = lista_covid[15]
dict_covid[lista_covid[16][ind_municipio]] = lista_covid[16]
dict_covid[lista_covid[17][ind_municipio]] = lista_covid[17]
dict_covid[lista_covid[18][ind_municipio]] = lista_covid[18]
dict_covid[lista_covid[19][ind_municipio]] = lista_covid[19]
dict_covid[lista_covid[20][ind_municipio]] = lista_covid[20]
dict_covid[lista_covid[21][ind_municipio]] = lista_covid[21]
dict_covid[lista_covid[22][ind_municipio]] = lista_covid[22]
dict_covid[lista_covid[23][ind_municipio]] = lista_covid[23]
dict_covid[lista_covid[24][ind_municipio]] = lista_covid[24]
dict_covid[lista_covid[25][ind_municipio]] = lista_covid[25]
dict_covid[lista_covid[26][ind_municipio]] = lista_covid[26]
dict_covid[lista_covid[27][ind_municipio]] = lista_covid[27]
dict_covid[lista_covid[28][ind_municipio]] = lista_covid[28]
dict_covid[lista_covid[29][ind_municipio]] = lista_covid[29]
dict_covid[lista_covid[30][ind_municipio]] = lista_covid[30]
dict_covid[lista_covid[31][ind_municipio]] = lista_covid[31]
dict_covid[lista_covid[32][ind_municipio]] = lista_covid[32]
dict_covid[lista_covid[33][ind_municipio]] = lista_covid[33]
dict_covid[lista_covid[34][ind_municipio]] = lista_covid[34]
dict_covid[lista_covid[35][ind_municipio]] = lista_covid[35]
dict_covid[lista_covid[36][ind_municipio]] = lista_covid[36]
dict_covid[lista_covid[37][ind_municipio]] = lista_covid[37]
dict_covid[lista_covid[38][ind_municipio]] = lista_covid[38]
dict_covid[lista_covid[39][ind_municipio]] = lista_covid[39]
dict_covid[lista_covid[40][ind_municipio]] = lista_covid[40]
dict_covid[lista_covid[41][ind_municipio]] = lista_covid[41]
dict_covid[lista_covid[42][ind_municipio]] = lista_covid[42]
dict_covid[lista_covid[43][ind_municipio]] = lista_covid[43]
dict_covid[lista_covid[44][ind_municipio]] = lista_covid[44]
dict_covid[lista_covid[45][ind_municipio]] = lista_covid[45]
dict_covid[lista_covid[46][ind_municipio]] = lista_covid[46]
dict_covid[lista_covid[47][ind_municipio]] = lista_covid[47]
dict_covid[lista_covid[48][ind_municipio]] = lista_covid[48]
dict_covid[lista_covid[49][ind_municipio]] = lista_covid[49]
dict_covid[lista_covid[50][ind_municipio]] = lista_covid[50]
dict_covid[lista_covid[51][ind_municipio]] = lista_covid[51]
dict_covid[lista_covid[52][ind_municipio]] = lista_covid[52]
dict_covid[lista_covid[53][ind_municipio]] = lista_covid[53]
dict_covid[lista_covid[54][ind_municipio]] = lista_covid[54]
dict_covid[lista_covid[55][ind_municipio]] = lista_covid[55]
dict_covid[lista_covid[56][ind_municipio]] = lista_covid[56]
dict_covid[lista_covid[57][ind_municipio]] = lista_covid[57]
dict_covid[lista_covid[58][ind_municipio]] = lista_covid[58]
dict_covid[lista_covid[59][ind_municipio]] = lista_covid[59]
dict_covid[lista_covid[60][ind_municipio]] = lista_covid[60]
dict_covid[lista_covid[61][ind_municipio]] = lista_covid[61]
dict_covid[lista_covid[62][ind_municipio]] = lista_covid[62]
dict_covid[lista_covid[63][ind_municipio]] = lista_covid[63]
dict_covid[lista_covid[64][ind_municipio]] = lista_covid[64]
dict_covid[lista_covid[65][ind_municipio]] = lista_covid[65]
dict_covid[lista_covid[66][ind_municipio]] = lista_covid[66]
dict_covid[lista_covid[67][ind_municipio]] = lista_covid[67]
dict_covid[lista_covid[68][ind_municipio]] = lista_covid[68]
dict_covid[lista_covid[69][ind_municipio]] = lista_covid[69]
dict_covid[lista_covid[70][ind_municipio]] = lista_covid[70]
dict_covid[lista_covid[71][ind_municipio]] = lista_covid[71]
dict_covid[lista_covid[72][ind_municipio]] = lista_covid[72]
dict_covid[lista_covid[73][ind_municipio]] = lista_covid[73]
dict_covid[lista_covid[74][ind_municipio]] = lista_covid[74]
dict_covid[lista_covid[75][ind_municipio]] = lista_covid[75]
print('')

# l. Extraia os dados de Teresina/PI apresentando os casos novos com um print.

print('_'*80)
print('item l - dados de Teresina a partir do dicionário')
print('Dados de Teresina - Pi a partir do dicionário:')
print('Região:            ', dict_covid['Teresina'][ind_regiao])
print('Estado:            ', dict_covid['Teresina'][ind_estado])
print('Município:         ', dict_covid['Teresina'][ind_municipio])
print('Data:              ', dict_covid['Teresina'][ind_data])
print('Casos Acumulados:  ', dict_covid['Teresina'][ind_casosAcumulado])
print('Casos Novos:       ', dict_covid['Teresina'][ind_casosNovos])
print('Óbitos Acumulados: ', dict_covid['Teresina'][ind_obitosAcumulado])
print('Óbitos Novos:      ', dict_covid['Teresina'][ind_obitosNovos])
print('')