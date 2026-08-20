import os
import unittest
from store import KeyValueStore

class TestKeyValueStore(unittest.TestCase):
    def setUp(self):
        """Выполняется ПЕРЕД каждым тестом"""
        self.test_db_file = "test_db.json"
        #Создаем чистый экземпляр хранилища с чистым файлом
        self.store = KeyValueStore(db_file=self.test_db_file)

    def tearDown(self):
        """Выполняется ПОСЛЕ каждого теста"""
        # Удаляем тестовый файл с диска, если он существует
        if os.path.exists(self.test_db_file):
            os.remove(self.test_db_file)

    def test_set_and_get(self):
        """Тест сохранения и получения значения"""
        self.store.set('key1', 'value1')
        self.assertEqual(self.store.get('key1'), 'value1')

    def test_get_non_existent_key(self):
        """Тест получения несуществующего ключа"""
        # TODO: Проверь, что для несуществующего ключа возвращается 'Key not found'
        
        self.assertEqual(self.store.get('asdf'), 'Key not found')

    def test_exists(self):
        """Тест проверки существования ключа"""
        # TODO: Добавь ключ, проверь что exists() возвращает True, а для несуществующего — False
        
        self.store.set('key1', 'value1')
        self.assertTrue(self.store.exists('key1'))
        self.assertFalse(self.store.exists('asdf'))

    def test_delete(self):
        """Тест удаления ключа"""
        # TODO: Добавь ключ, удали его через delete(), проверь что метод вернул True, а повторное получение дает 'Key not found'
        
        self.store.set('key1', 'value1')
        self.assertTrue(self.store.delete('key1'))
        self.assertFalse(self.store.delete('non_existent_key'))
        self.assertEqual(self.store.get('key1'), 'Key not found')

    def test_get_all(self):
        """Тест получения всех элементов"""
        # TODO: Добавь пара ключей и проверь, что get_all() возвращает ожидаемый словарь
        
        self.store.set('key1', 'value1')
        self.store.set('key2', 'value2')
        self.store.set('key3', 'value3')

        expected_dict = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
        }

        self.assertDictEqual(self.store.get_all(), expected_dict)

if __name__ == '__main__':
    unittest.main()