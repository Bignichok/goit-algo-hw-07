class Comment:
    def __init__(self, text, author) -> None:
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self, reply):
        if reply in self.replies:
            reply.text = "Цей коментар було видалено."
            reply.is_deleted = True

    def display(self, level=0):
        indent = '  ' * level
        if self.is_deleted:
            print(f"{indent}[Видалено] {self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")
        
        for reply in self.replies:
            reply.display(level + 1)

root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")
reply2_1 = Comment("Відповідь на другу відповідь", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)
reply2.add_reply(reply2_1)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

root_comment.display()

root_comment.remove_reply(reply1)

root_comment.display()
