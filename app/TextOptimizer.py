class TextOptimizer(object):
    def __init__(self, origin_text):
        self.origin_text = origin_text

    def replace_common_spoken_words(self):
        common_spoken_words = ["嗯", "呃", "啊", "哈", "就是", "这个", "是吧", "那个", "那么",
                               "那", "然后", "的话", "吧", "就", "呢", "噢", "哦","唉",
                               "完了之后","是？"]
        for common_word in common_spoken_words:
            self.origin_text = str(self.origin_text).replace(common_word, "")
            # print(self.origin_text)
        return self.origin_text

    # remove_redundant_punctuation method should be called after replace_common_spoken_words
    def remove_redundant_punctuation(self):
        self.origin_text = str(self.origin_text).replace("，，", "，")
        self.origin_text = str(self.origin_text).replace("。。", "。")
        self.origin_text = str(self.origin_text).replace("？", "")
        return self.origin_text

    def optimize(self):
        self.replace_common_spoken_words()
        return self.remove_redundant_punctuation()
