import unittest
from translators.ast_translator import ASTTranslator

class TestASTTranslator(unittest.TestCase):
    def test_translate_sysdate(self):
        translator = ASTTranslator()
        result = translator.translate("SELECT SYSDATE FROM DUAL;")
        self.assertIn("GETDATE", result)

if __name__ == '__main__':
    unittest.main()
