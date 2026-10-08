import requests
from html.parser import HTMLParser

class doc_parser(HTMLParser):
    table = False
    table_content: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        if tag == "table":
            self.table = True

    def handle_endtag(self, tag: str):
        if tag == "table":
            self.table = False

    def handle_data(self, data: str):
        if self.table:
            self.table_content.append(data)

def decode_url(url: str):
    response = requests.get(url)

    parser = doc_parser()
    parser.feed(response.text)

    return parser.table_content

def parse_table(table: list[str]):
    coord_list: list[list[str]] = [[]]
    count = 1
    row = 0
    length: int = len(table)
    grid: list[list[str]] = [[]]

    for i in range(2, length):
        if i > 2:
            if (count < 3):
                if (count == 1):
                    grid[row].append(table[i])
                else:
                    coord_list[row].append(table[i])
                count += 1
            else:
                if (i != length-1):
                    grid.append([])
                    coord_list.append([])
                count = 1
                grid[row].append(table[i])
                row += 1

    return (grid, coord_list)

def convert_string_to_int(grid: list[list[str]]):
    new_grid: list[list[int]] = [[]]
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i].append(int(grid[i][j]))
        if (i != len(grid)-1):
            new_grid.append([])
    
    return new_grid

def convert_x_y_grid(int_grid: list[list[int]]):
    x_list: list[int] = []
    y_list: list[int] = []

    for lst in int_grid:
        x_list.append(lst[0])
        y_list.append(lst[1])

    return (x_list,y_list)

def main():
    URL = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"

    table: list[str] = decode_url(URL)
    grid, char_list = parse_table(table)
    int_grid: list[list[int]] = convert_string_to_int(grid)
    drawing = convert_x_y_grid(int_grid)

    print(drawing)

    i = 0
    count = 0
    count1 = 0
    for x in range(3):
        for y in range(3):
            if (x == drawing[0][count]):
                if (y == drawing[1][count1]):
                    print(char_list[i])
                count1 += 1
                i += 1
        count += 1


main()