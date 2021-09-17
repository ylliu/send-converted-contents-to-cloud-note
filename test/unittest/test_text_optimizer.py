import unittest

from app.TextOptimizer import TextOptimizer


class TextOptimizerTest(unittest.TestCase):
    def test_should_replace_common_spoken_words(self):
        text_expected = "我今天出门没带钥匙，，我回来才发现，没拿钥匙，进不了门，这样看，" \
                        "我最好找开锁公司，我想起来了还有一个备用钥匙在门边"

        origin_text = "嗯我那个呃那个呃就是啊今天出门没带钥匙哈，是吧，然后就是这个这个呢我就回来才发现，那个那么那那没拿钥匙，进不了门，这样看的话，" \
                      "我最好找开锁公司吧，哦噢我想起来了还有一个备用钥匙在门边"
        text_optimizer = TextOptimizer(origin_text)
        self.assertEqual(text_expected, text_optimizer.replace_common_spoken_words())

    def test_should_remove_redundant_punctuation(self):
        text_expected = "我今天，出门没带钥匙。"
        origin_text = "我今天，，出门没带钥匙。。？"
        text_optimizer = TextOptimizer(origin_text)
        self.assertEqual(text_expected, text_optimizer.remove_redundant_punctuation())
