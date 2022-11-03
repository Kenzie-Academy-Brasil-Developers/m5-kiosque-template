import unittest

from management.product_handler import get_product_by_id


class TestGetProductById(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        function_name = "get_product_by_id"
        cls.base_msg = f"Verifique se sua função `{function_name}` está %s."

    def test_can_get_product_by_id(self):
        """
        Testa se a função `get_product_by_id` retorna o produto existente corretamente [0 pts].
        """
        result = get_product_by_id(32)
        expected = {
            "_id": 32,
            "description": "Mix of rum, lemon juice, mint, sugar and sparking water",
            "price": 27.61,
            "rating": 4,
            "title": "Mojito",
            "type": "drink",
        }

        msg = self.base_msg % "retornando um dicionário"
        self.assertIsInstance(result, dict, msg)

        msg = self.base_msg % ("retornando corretamente um produto encontrado",)
        self.assertDictEqual(result, expected, msg)

    def test_get_product_by_id_with_non_existing_id(self):
        """
        Testa se a função `get_product_by_id` retorna um dicionário vazio caso o id do produto não seja encontrado no menu [0 pts].
        """
        result = get_product_by_id(1000000000000000)
        expected = {}

        msg = self.base_msg % "retornando um dicionário"
        self.assertIsInstance(result, dict, msg)

        msg = (
            self.base_msg
            % "retornando um dicionário vazio caso o id passado não seja encontrado",
        )

        self.assertDictEqual(result, expected, msg)

    def test_get_product_by_id_raises_type_error(self):
        """
        Testa se a função `get_product_by_id` levanta um TypeError caso o tipo do parâmetro passado não seja um inteiro [0 pts].
        """

        msg = self.base_msg % (
            "levantando um `TypeError` caso o parâmetro passado não seja um inteiro",
        )
        with self.assertRaises(TypeError, msg=msg) as err:
            get_product_by_id([1, 2, 3])

        msg = self.base_msg % ("retornando a mensagem apropriada com o TypeError",)
        self.assertEqual(*err.exception.args, "product id must be an int", msg=msg)
