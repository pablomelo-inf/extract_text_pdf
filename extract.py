import pdfplumber
import json
from extract_functions import *


def print_bold(text):
    return f"\033[1m{text}\033[0m"

def extract_text_from_pdf(pdf_path, from_page=1, to_page=31):
    """Extrai texto de um PDF em um intervalo de páginas."""

    font_question = 'IYOWBY+Arial-BoldMT'
    font_letter = 'NYXVTO+BundesbahnPiStd-1'

    with (pdfplumber.open(pdf_path) as pdf):
        fonts = {}
        for i, page in enumerate(pdf.pages):

            if i <= from_page or i >= to_page:
                continue

            side_left_page, side_right_page = crop_left(page), crop_right(page)
            words_page_left, words_page_right = extract_words_pdf(side_left_page), extract_words_pdf(side_right_page)

            words_page = words_page_left + words_page_right
            alternativa, letra, questoes_prova, numero_questao = '', '', {}, ''

            for indice, word in enumerate(words_page):
                word_text = word['text']

                if word['fontname'] not in fonts:
                    fonts[word['fontname']] = ''
                fonts[word['fontname']] = ''


                if word['size'] > 12:
                    continue

                if is_question(word, font_question):
                   numero_questao, questoes_prova = extract_question_number(questoes_prova, word_text.strip())
                   alternativa, letra = '', ''

                elif is_font_info(word):
                    questoes_prova = extract_font_information(numero_questao, questoes_prova, word_text)

                elif is_option_letter(word, font_letter):
                    letra = alternativa = word_text

                elif alternativa and not is_option_letter(word, font_letter):
                    questoes_prova = extract_alternativas(numero_questao, questoes_prova, word_text, letra.strip())
                    alternativa = ''

                else:
                    if numero_questao in questoes_prova:
                        if letra:
                            questoes_prova[numero_questao]['alternativas'][letra.strip()] += word_text
                        questoes_prova[numero_questao]['texto'] += word_text

                    #print('\n\t\t\t', print_bold('[FONTE]'),word['text'],print_bold('\t [ F: ' + word['fontname'] + ', SIZE: '+  str(word['size']) +' ]'), '\n')

            for index, value in questoes_prova.items():

                if 'QUEST' in index.strip() and is_complete_question(value['alternativas']):
                    print(json.dumps(value, ensure_ascii=False, indent=4))


        #print(fonts)
        #print(json.dumps(fonts, ensure_ascii=False, indent=4))

def main():
    pdf_path = './.exams/dia1_caderno1_azul_v2_2015_dia2.pdf'
    extract_text_from_pdf(pdf_path, 1)


if __name__ == "__main__":
    main()