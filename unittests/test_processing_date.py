import unittest
from app.main import processing_date

class TestProcessingDateFunction(unittest.TestCase):

    def test_payload_a(self):
        payload = {'JobName': 'a'}
        resultado = processing_date(payload)
        self.assertIsInstance(resultado, str)
        self.assertRegex(resultado, r'\d{8}')

    def test_payload_b(self):
        payload = {'JobName': 'b'}
        resultado = processing_date(payload)
        self.assertIsInstance(resultado, list)
        self.assertEqual(len(resultado), 1)
        self.assertIsInstance(resultado[0], str)
        self.assertRegex(resultado[0], r'\d{8}')

    def test_payload_invalido(self):
        payload = {'JobName': 'c'}
        resultado = processing_date(payload)
        self.assertEqual(resultado, "Payload inválido. Insira a variável JobName de forma correta.")

    def test_payload_nulo(self):
        payload = None
        resultado = processing_date(payload)
        self.assertEqual(resultado, "Exception nao mapeada 'NoneType' object is not subscriptable")

    def test_payload_sem_jobname(self):
        payload = {'OutroNome': 'a'}
        resultado = processing_date(payload)
        self.assertEqual(resultado, "Exception nao mapeada 'JobName' not in payload")

    def test_excecao_formato_data(self):
        payload = {'JobName': 'a'}
        with unittest.mock.patch('datetime.datetime.now') as mock_now:
            mock_now.side_effect = ValueError("Formato de data inválido")
            resultado = processing_date(payload)
        self.assertEqual(resultado, "Exception nao mapeada Formato de data inválido")

if __name__ == '__main__':
    unittest.main()
