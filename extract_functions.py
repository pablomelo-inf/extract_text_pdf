def extract_words_pdf(page):
    """Extrai palavras de uma página PDF com configurações específicas."""

    return page.extract_words(
        x_tolerance=50,
        x_tolerance_ratio=None,
        y_tolerance=3,
        keep_blank_chars=True,
        use_text_flow=False,
        line_dir="ttb",
        char_dir="ltr",
        line_dir_rotated="ttb",
        char_dir_rotated="ltr",
        extra_attrs=['fontname', 'size', 'y0'],
        split_at_punctuation=False,
        expand_ligatures=True
    )

def crop_left(file_pdf_page):
    """Recorta a metade esquerda de uma página PDF."""

    return file_pdf_page.crop(
        (
            0,
            0.1 * float(file_pdf_page.height),
            0.51 * float(file_pdf_page.width),
            0.93 * float(file_pdf_page.height)
        ))

def crop_right(file_pdf_page):
    """Recorta a metade direita de uma página PDF."""

    return file_pdf_page.crop(
        (
            0.5 * float(file_pdf_page.width),
            0.01 * float(file_pdf_page.height),
            file_pdf_page.width,
            0.93 * float(file_pdf_page.height)
        ))

def is_complete_question(options: dict[str, str]) -> bool:
    """Verifica se todas as opções da questão estão presentes."""

    return all(options.get(option, '') != '' for option in ['A', 'B', 'C', 'D', 'E'])

def is_font_info(word: dict) -> bool:
    """Verifica se uma informação de fonte / referencia."""

    return 6 <= word['size'] <= 7.50

def is_question(word: dict, font) -> bool:
    """Verifica se a palavra é uma questão."""

    return word['fontname'] == font and 10 <= word['size'] <= 10.50 and 'QUEST' in word['text']

def is_option_letter(word: dict, letter) -> bool:
    """Verifica se a palavra é uma letra de opção."""

    return word['fontname'] == letter

#def init_questoes_prova():

def extract_font_information(numero_questao: str, questoes_prova: dict, word_text: str) -> dict:

    if numero_questao not in questoes_prova:
        questoes_prova[numero_questao] = {'texto': '', 'alternativas': {}, 'fonte': ''}

    questoes_prova[numero_questao]['fonte'] += word_text

    return questoes_prova

def extract_question_number(questoes_prova: dict, word_text: str)-> dict:
    numero_questao = word_text.strip()
    if numero_questao not in questoes_prova:
        questoes_prova[numero_questao] = {'texto': '', 'alternativas': {}, 'fonte': ''}

    questoes_prova[numero_questao]['texto'] += word_text + ' '
    return numero_questao, questoes_prova

def extract_alternativas(numero_questao, questoes_prova, word_text, auxletra):

    if auxletra not in questoes_prova[numero_questao]['alternativas']:
        questoes_prova[numero_questao]['alternativas'][auxletra] = ''

    questoes_prova[numero_questao]['alternativas'][auxletra] += word_text

    return questoes_prova