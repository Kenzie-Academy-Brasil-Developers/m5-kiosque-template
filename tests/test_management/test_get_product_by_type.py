import unittest

from management.product_handler import get_products_by_type


class TestGetProductByType(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        function_name = "get_product_by_type"
        cls.base_msg = f"Verifique se sua função `{function_name}` está %s."

    def test_can_get_product_by_type(self):
        """
        Testa se a função `get_product_by_type` retorna os produtos de determinado tipo corretamente [0 pts].
        """
        result = get_products_by_type("drink")
        expected = [
            {
                "_id": 32,
                "description": "Mix of rum, lemon juice, mint, sugar and sparking water",
                "price": 27.61,
                "rating": 4,
                "title": "Mojito",
                "type": "drink",
            },
            {
                "_id": 37,
                "description": "Homemade cola drink with lemon juice and 2 ice cubes",
                "price": 28.96,
                "rating": 5,
                "title": "Fresh Nuka-Cola",
                "type": "drink",
            },
        ]

        msg = self.base_msg % "retornando uma lista"
        self.assertIsInstance(result, list, msg)

        msg = self.base_msg % ("retornando corretamente os produtos encontrados",)
        self.assertListEqual(result, expected, msg)

    def test_get_product_by_type_with_non_existing_type(self):
        """
        Testa se a função `get_product_by_type` retorna uma lista vazia caso não exista nenhum produto do tipo [0 pts].
        """
        result = get_products_by_type("non_existing_type_10000")
        expected = []

        msg = self.base_msg % "retornando uma lista"
        self.assertIsInstance(result, list, msg)

        msg = (
            self.base_msg
            % "retornando uma lista vazia caso não existam produtos do tipo passado",
        )

        self.assertListEqual(result, expected, msg)

    def test_get_product_by_type_raises_type_error(self):
        """
        Testa se a função `get_product_by_type` levanta um TypeError caso o tipo do parâmetro passado não seja uma string [0 pts].
        """

        msg = self.base_msg % (
            "levantando um `TypeError` caso o parâmetro passado não seja uma string",
        )
        with self.assertRaises(TypeError, msg=msg) as err:
            get_products_by_type([1, 2, 3])

        msg = self.base_msg % ("retornando a mensagem apropriada com o TypeError",)
        self.assertEqual(*err.exception.args, "product type must be a str", msg=msg)
