
# PDF Exam Question Extractor

This project implements a feature to extract text questions from the PDF of the ENEM 2015 exam.

## Description

The goal of this repository is to provide a Python-based solution for extracting text questions from the ENEM 2015 exam PDF. The project utilizes `pdfplumber` for handling PDF parsing and extraction, and the extracted data can be saved in JSON format.

## Features

- Extracts text questions from the ENEM 2015 exam PDF.
- Parses the PDF and processes text to identify and separate questions.
- Saves extracted questions to a JSON file for easy access and manipulation.

## Installation

1. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

The project requires the following Python libraries:

- `pdfplumber`
- `json` (part of Python's standard library)

You can find the dependencies listed in the `requirements.txt` file.

## Usage

1. **Place the ENEM 2015 PDF in the project directory.**

2. **Run the extraction script:**

   ```bash
   python extract.py
   ```

3. **Output:**

   The script will generate a `json` containing the extracted questions.
   
   Example output:
   ```json
   [
      "QUESTÃO 95": {
        "texto": "QUESTÃO 95 Los guionistas estadounidenses introducen cada vez más el español en sus diálogosEn los últimos años, la realidad cultural y la presencia creciente de migrantes de origen latinoamericano en EE UU ha propiciado que cada vez más estadounidenses alternen el inglés y el español en un mismo discurso.Un estudio publicado en la revista Vial-Vigo International Journal of Applied Linguistics se centra en las estrategias que usan los guionistas de la versión original para incluir el español en el guión o a personajes de origen latinoamericano.Los guionistas estadounidenses suelen usar subtítulos en inglés cuando el español que aparece en la serie o película es importante para el argumento. Si esto no ocurre, y sólo hay interjecciones, aparece sin subtítulos. En aquellas conversaciones que no tienen relevancia se añade en ocasiones el subtítulo Speaks Spanish (habla en español).“De esta forma, impiden al público conocer qué están diciendo los dos personajes que hablan español”, explica la autora del estudio y profesora e investigadora en la Universidad Pablo de Olavide (UPO) de Sevilla. De acordo com o texto, nos filmes norte-americanos, nem todas as falas em espanhol são legendadas em inglês. Esse fato revela ada diversidade linguística nos Estados Unidos.séries e filmes produzidos nos Estados Unidos.as salas de cinema norte-americanas.roteiristas e tradutores norte-americanos.do espanhol na cultura norte-americana. QQp(dhOsYsEoaDcrqEoscuqAcNp",
        "alternativas": {
            "A": "assimetria no tratamento do espanhol como elemento da diversidade linguística nos Estados Unidos.",
            "B": "escassez de personagens de origem hispânica nas séries e filmes produzidos nos Estados Unidos.",
            "C": "desconsideração com o público hispânico que frequenta as salas de cinema norte-americanas.",
            "D": "falta de uma formação linguística específica para os roteiristas e tradutores norte-americanos.",
            "E": "carência de pesquisas científicas sobre a influência do espanhol na cultura norte-americana. QQp(dhOsYsEoaQDcrqEoscuqAcNpQuestões de 96 a 135"
        },
        "fonte": "Disponível em: www.agenciasinc.es. Acesso em: 23 ago. 2012 (adaptado).2015"
      },
      "QUESTÃO 96": {
        "texto": "QUESTÃO 96 O rap, palavra formada pelas iniciais de rhythm and poetry (ritmo e poesia), junto com as linguagens da dança (o break dancing) e das artes plásticas (o grafite), seria difundido, para além dos guetos, com o nome de cultura hip hop. O break dancing surge como uma dança de rua. O grafite nasce de assinaturas inscritas pelos jovens com sprays nos muros, trens e estações de metrô de Nova York. As linguagens do rap, do break dancing e do grafite se tornaram os pilares da cultura hip hop.Entre as manifestações da cultura hip hop apontadas no texto, o break se caracteriza como um tipo de dança que representa aspectos contemporâneos por meio de movimentosurbana.de protesto.culturais.",
        "alternativas": {
            "A": "retilíneos, como crítica aos indivíduos alienados.",
            "B": "improvisados, como expressão da dinâmica da vida urbana.",
            "C": "suaves, como sinônimo da rotina dos espaços públicos.",
            "D": "ritmados pela sola dos sapatos, como símbolo de protesto.",
            "E": "cadenciados, como contestação às rápidas mudanças culturais."
        },
        "fonte": "DAYRELL, J. A música entra em cena: o rap e o funk na socialização da juventude. Belo Horizonte: UFMG, 2005 (adaptado)."
      },
   ...
   ]
```
## Project Structure

- `extract_questions.py`: The main script to extract questions from the PDF.
- `requirements.txt`: A file listing the dependencies required for the project.
- `questions.json`: The output file containing the extracted questions (generated after running the script).



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
