"""Markdown editor """

# Libraries
import os


class MarkdownEditor:
    def __init__(self):
        """Initialize the class attributes"""
        self.help = None
        self.plain_text = None
        self.bold_text = None
        self.italic_text = None
        self.inline_code = None
        self.link_label = None
        self.link_url = None
        self.header_level = None
        self.unordered_list = ""
        self.new_line = None
        self.ordered_list = ""
        self.user_text = ""

    def help_option(self):
        """Print the help option"""
        self.help = ('Available formatters: "plain" "bold" "italic" "header" "link" "inline-code" "ordered-list" '
                     '"unordered-list" "new-line" \nSpecial commands: "!help" "!done"')

    def plain_func(self) -> str:
        """Print the plain text"""
        self.plain_text = input('Text: ')
        self.user_text += self.plain_text
        return self.user_text

    def bold_func(self) -> str:
        """Print the bold text"""
        self.bold_text = input('Text: ')
        self.user_text += f'**{self.bold_text}**'
        return self.user_text

    def italic_func(self) -> str:
        """Print the italic text"""
        self.italic_text = input('Text: ')
        self.user_text += f'*{self.italic_text}*'
        return self.user_text

    def inline_func(self) -> str:
        """Print the inline code"""
        self.inline_code = input('Text: ')
        self.user_text += f'`{self.inline_code}`'
        return self.user_text

    def link_func(self) -> str:
        """Print the link text"""
        self.link_label = input('Label: ')
        self.link_url = input('URL: ')
        self.user_text += f'[{self.link_label}]({self.link_url})'
        return self.user_text

    def header_func(self) -> str:
        """Print the header text"""
        while True:
            level = input('Level: ')
            try:
                level = int(level)
            except ValueError:
                print('The level should be a number')
                continue
            if 1 < level > 6:
                print('The level should be within the range of 1 to 6')
            else:
                self.header_level = input('Text: ')
                self.user_text += f'{"#" * level} {self.header_level}\n'
                return self.user_text

    def unordered_func(self) -> str:
        """Print the unordered list"""
        while True:
            users_rows = input("Number of rows:")
            try:
                users_rows = int(users_rows)
            except ValueError:
                print("The value should be a number")
                continue
            if 0 < users_rows <= 100:
                for index in range(users_rows):
                    self.unordered_list = "* " + input(f"Row #{index + 1}:") + "\n"
                    self.user_text += self.unordered_list
                return self.user_text

    def ordered_func(self) -> str:
        """Print the ordered list"""
        while True:
            users_rows = input("Number of rows:")
            try:
                users_rows = int(users_rows)
            except ValueError:
                print("The value should be a number")
                continue
            if 0 < users_rows <= 100:
                for index in range(users_rows):
                    row = input(f"Row #{index + 1}:")
                    self.ordered_list += str(index + 1) + ". " + row + "\n"
                    self.user_text = self.ordered_list
                return self.user_text

    def new_line_func(self) -> str:
        """Print the new line"""
        self.new_line = "\n\n"
        self.user_text += self.new_line
        return self.user_text

    def write_file_func(self) -> None:
        """Write the file and save it. If the file does not exist, create it"""
        if not os.path.exists('output.md'):
            with open('output.md', 'x', encoding='utf-8'):
                pass
        with open('output.md', 'w', encoding='utf-8') as file:
            file.write(self.user_text)

    def menu(self):
        """Print the menu"""
        while True:
            user_input = input('Choose a formatter: ')
            if user_input == '!help':
                self.help_option()
                print(self.help)
            elif user_input == '!done':
                self.write_file_func()
                exit()
            elif user_input == 'plain':
                self.plain_func()
            elif user_input == 'bold':
                self.bold_func()
            elif user_input == 'italic':
                self.italic_func()
            elif user_input == 'inline-code':
                self.inline_func()
            elif user_input == 'link':
                self.link_func()
            elif user_input == 'header':
                self.header_func()
            elif user_input == 'unordered-list':
                self.unordered_func()
            elif user_input == 'ordered-list':
                self.ordered_func()
            elif user_input == 'new-line':
                self.new_line_func()
            else:
                print('Unknown formatting type or command')


# Main
if __name__ == '__main__':
    markdown_editor = MarkdownEditor()
    markdown_editor.menu()
