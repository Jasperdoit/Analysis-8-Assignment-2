from database import Database
class Logger:
    def __init__(self):
        pass
    def display_log(test):
        t = Table(["No.", "Date", "Time", "Username", "Description of activity", "Additional Information", "Suspicious"])
        t.add_row(["1", "testtesttest", "test", "test", "test", "test", "test"])
        t.add_row(["2", "test", "test", "test", "test", "test", "test"])
        t.add_row(["3", "test", "test", "test", "test", "test", "test"])
        t.add_row(["4", "test", "test", "test", "test", "test", "test"])
        t.print_table()


class Table:
    def __init__(self, headers, border=' | ', bot_char='-'):
        self.headers = headers
        self.columns = len(headers)
        self.border = border
        self.bot_char = bot_char
        self.data = []
        self.max_widths = [len(str(header)) for header in headers]

    def add_row(self, row):
        if len(row) != self.columns:
            raise ValueError("Number of elements in the row doesn't match the number of columns.")

        self.data.append(row)
        for i, element in enumerate(row):
            self.max_widths[i] = max(self.max_widths[i], len(str(element)))

    def print_table(self):
        total_width = sum(self.max_widths) + len(self.border) * (self.columns - 1) + 7
        border_row = self.bot_char * total_width

        print(border_row)

        # Print the headers
        header_str = self.border.join(header.center(self.max_widths[i]) for i, header in enumerate(self.headers))
        header_row = f"{self.border} {header_str} {self.border}"
        print(header_row)

        print(border_row)

        # Print the table rows
        for row in self.data:
            row_str = self.border.join(str(element).center(self.max_widths[i]) for i, element in enumerate(row))
            row_row = f"{self.border} {row_str} {self.border}"
            print(row_row)

        print(border_row)