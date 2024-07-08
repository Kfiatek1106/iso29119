from iso29119 import FinalResult
from iso29119.test_case import TestCase, TestCases
from reportlab.lib.colors import black, red, green, darkorange, lightgrey
from reportlab.platypus import Table, PageBreak, Paragraph, SimpleDocTemplate, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, landscape, portrait
import datetime


HEADING_1 = "Heading1"
HEADING_2 = "Heading2"
HEADING_3 = "Heading3"

PAGE_SIZE: tuple = A4

PAGE_WIDTH, PAGE_HEIGHT = PAGE_SIZE
PAGE_MARGIN: int = 25


LAYOUT_PORTRAIT = 'portrait'
LAYOUT_LANDSCAPE = 'landscape'


def add_header(text: str, heading: str = HEADING_1) -> Paragraph:
    style = getSampleStyleSheet()
    return Paragraph(text, style[heading])


def add_page_number(number: int):
    style = getSampleStyleSheet()
    return Paragraph(number, style['normal'])


def test_result_colour_font(table_style: list, record: str, col: int, row: int):

    if record == FinalResult.PASS.value:
        colour = green

    elif record == FinalResult.FAIL.value:
        colour = red

    elif record == FinalResult.ATTENTION.value:
        colour = darkorange

    else:
        colour = black

    table_style.append(('TEXTCOLOR', (col, row), (col, row), colour))


class PdfReport:

    def __init__(self, name: str = 'pdf_report', path: str = '/tmp/', margin: int = PAGE_MARGIN):
        self.__doc: SimpleDocTemplate
        self.__name: str = name
        self.__path: str = path
        self.__margin: int = margin

        self.__stories = []

    def __create_simple_doc_template(self) -> None:

        def frame_portrait(margin: int, show_boundary: int = 1):
            width, height = PAGE_WIDTH, PAGE_HEIGHT
            width = width - (margin * 2)
            height = height - (margin * 2)
            layout_id = 'portrait_frame '

            return Frame(x1=margin, y1=margin, width=width, height=height, id=layout_id, showBoundary=show_boundary)

        def frame_landscape(margin: int, show_boundary: int = 1):
            width, height = PAGE_WIDTH, PAGE_HEIGHT
            width = height - (margin * 2)
            height = width - (margin * 2)
            layout_id = 'landscape_frame '

            return Frame(x1=margin, y1=margin, width=width, height=height, id=layout_id, showBoundary=show_boundary)

        def frame_left(margin: int, show_boundary: int = 1):
            width, height = PAGE_WIDTH, PAGE_HEIGHT
            width = (width - (margin * 2)) / 2
            height = height - (margin * 2)
            layout_id = 'left_frame '

            return Frame(x1=margin, y1=margin, width=width, height=height, id=layout_id, showBoundary=show_boundary)

        def frame_right(margin: int, show_boundary: int = 1):
            width, height = PAGE_WIDTH, PAGE_HEIGHT
            width = (width - (margin * 2)) / 2
            height = height - (margin * 2)
            layout_id = 'right_frame '

            return Frame(x1=width, y1=margin, width=width, height=height, id=layout_id, showBoundary=show_boundary)

        def frame_page_number(margin: int, show_boundary: int = 2):
            width, height = PAGE_WIDTH, PAGE_HEIGHT
            width = (width - (margin * 2)) / 2
            height = height - (margin * 2)
            layout_id = 'page_number_frame '

            return Frame(x1=width, y1=margin, width=width, height=height, id=layout_id, showBoundary=show_boundary)

        portrait_frame = frame_portrait(PAGE_MARGIN)
        landscape_frame = frame_landscape(PAGE_MARGIN)
        left_frame = frame_left(PAGE_MARGIN)
        right_frame = frame_right(PAGE_MARGIN)

        page_number_frame = frame_page_number(self.__margin)

        portrait_page = PageTemplate(id=LAYOUT_PORTRAIT,
                                     frames=[portrait_frame, page_number_frame],
                                     pagesize=portrait(PAGE_SIZE))

        landscape_page = PageTemplate(id=LAYOUT_LANDSCAPE,
                                      frames=landscape_frame,
                                      pagesize=landscape(PAGE_SIZE))

        name = self.__path + f'{self.__name}_{datetime.datetime.now().strftime("%Y_%m_%d %H:%M:%S")}.pdf'
        self.__doc = SimpleDocTemplate(name,
                                       pagesize=PAGE_SIZE,
                                       rightMargin=PAGE_MARGIN,
                                       leftMargin=PAGE_MARGIN,
                                       topMargin=PAGE_MARGIN,
                                       bottomMargin=PAGE_MARGIN)

        self.__doc.addPageTemplates([portrait_page, landscape_page])

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            self.__name = value

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, value: str) -> None:
        if isinstance(value, str):
            self.__path = value

    @property
    def margin(self) -> int:
        return self.__margin

    @margin.setter
    def margin(self, value: int) -> None:
        if isinstance(value, int):
            self.__margin = value

    def add_info_table(self):
        pass

    def add_summary_table(self, header: str = "", name: str = "", test_cases: list[TestCase] = None,
                          iter_from: int = 0, total_records_in_table: int = 10) -> None:

        pages = []
        item: TestCases
        row: int = 0

        table = []
        table_style = []

        table_width = (PAGE_WIDTH - PAGE_MARGIN * 2) - 0.05

        col_1_width = table_width * 0.05
        col_2_width = table_width * 0.60
        col_3_width = table_width * 0.15
        col_4_width = table_width * 0.10

        for item in test_cases:
            if row == 0:
                table.append(['ID', 'Name', 'Test Result', 'In Place'])
                table_style.append(('LINEABOVE', (0, 0), (3, 0), 1, black))
                table_style.append(('LINEBELOW', (0, 0), (3, 0), 1, black))
                table_style.append(('BACKGROUND', (0, 0), (3, 0), lightgrey))
                table_style.append(('TEXTCOLOR', (0, 0), (3, 0), black))

            row += 1
            table.append([str(iter_from), str(item.name), str(item.result), str(item.in_place)])
            test_result_colour_font(table_style=table_style, record=item.result, col=2, row=row)
            iter_from += 1

            if (row >= total_records_in_table) or (row == len(test_cases)):
                pages.append(add_header(f'{header}'))
                pages.append(add_header(f'Summary: {name}', HEADING_2))
                pages.append(Table(data=table,
                                   colWidths=[col_1_width, col_2_width, col_3_width, col_4_width],
                                   style=table_style))
                pages.append(PageBreak())
                row = 0

        self.__stories.extend(pages)

    def add_details_table(self, header: str = "", name: str = "", test_cases: list[TestCase] = None,
                          iter_from: int = 0, total_test_cases_per_page: int = 5) -> None:
        pages = []
        item: TestCases

        table = []
        table_style = []
        item_per_page = 0

        total_table_width = (PAGE_WIDTH - PAGE_MARGIN * 2) - 0.05
        col_1_width = total_table_width * 0.2
        col_2_width = total_table_width * 0.8

        for item in test_cases:

            if isinstance(item, TestCases):
                pass # self.__pdf_iso29119_details_table()

            elif isinstance(item, TestCase):

                if item_per_page == 0:
                    pages.append(PageBreak())
                    pages.append(add_header(f'{header}'))
                    pages.append(add_header(f'Details: {name}', HEADING_2))

                # Create first
                table.append(['ID', str(iter_from)])
                table.append(["Name", str(item.name)])
                table.append(["Expected value", str(item.expected)])
                table.append(["Actual value", str(item.actual)])
                table.append(["Test Result", str(item.result)])
                table.append(["Issue", str(item.issue)])

                table_style.append(('LINEABOVE', (0, 0), (0, 5), 1, black))
                table_style.append(('LINEBELOW', (0, 0), (0, 5), 1, black))
                table_style.append(('BACKGROUND', (0, 0), (0, 5), lightgrey))
                table_style.append(('TEXTCOLOR', (0, 0), (0, 5), black))

                test_result_colour_font(table_style=table_style, record=item.result, col=1, row=4)

                pages.append(Table(data=table,
                                   colWidths=[col_1_width, col_2_width],
                                   #rowHeights=[10, 10, 10, 10, 10, 10],
                                   style=table_style))

                item_per_page += 1
                iter_from += 1

                if item_per_page >= total_test_cases_per_page:
                    item_per_page = 0
            else:
                pass

        self.__stories.extend(pages)

    def build(self) -> None:
        self.__create_simple_doc_template()
        if len(self.__stories) > 0:
            self.__doc.build(self.__stories)
        self.__stories = []
