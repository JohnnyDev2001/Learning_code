from unittest import TestCase, main
from app import RomeuEJulieta, RomeusEJulietas

class TestRomeuEJulieta(TestCase):
    '''def test_exist_romeu_e_julieta(self):
        RomeuEJulieta()'''

    def test_rej_deve_retornar_queijo_quando_input_for_multiplo_de_3(self):
        '''RomeuEJulieta(3) -> 'Queijo'\n'''
        valores_entrada = [3, 6, 9]
        valor_esperado = 'Queijo'
        for valor in valores_entrada:
            with self.subTest(valor=valor):
                self.assertEqual(RomeuEJulieta(valor), valor_esperado)

    def test_rej_deve_retornar_goiabada_quando_input_for_multiplo_de_5(self):
        '''RomeuEJulieta(5) -> 'Goiabada'\n'''
        valores_entrada = [5, 10, 20]
        valor_esperado = 'Goiabada'
        for valor in valores_entrada:
            with self.subTest(valor=valor):
                self.assertEqual(RomeuEJulieta(valor), valor_esperado)

    def test_rej_deve_retornar_romeu_e_julieta_quando_input_for_15(self):
        '''RomeuEJulieta(15) -> 'Romeu e Julieta'\n'''
        valores_entrada = 15
        valor_esperado = 'Romeu e Julieta'
        self.assertEqual(RomeuEJulieta(valores_entrada), valor_esperado)
    
    def test_rsejs_deve_retornar_queijo_goiabada_romeu_e_julieta_quando_input_for_todos_os_multiplos(self):
        valores_entrada = [3, 5, 15]
        valores_esperados = ["Queijo","Goiabada","Romeu e Julieta"]
        self.assertEqual(RomeusEJulietas(valores_entrada), valores_esperados)
        


main()

