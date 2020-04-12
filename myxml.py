from xml.dom import minidom
import xml.etree.ElementTree as ET
import numpy as np

def downloadSquareFromXML():
    tree = ET.parse('square.xml')#стучится к моейм xml
    root = tree.getroot()#вынимает корневой элемент
    N = int(root.find('N').text)
    square = np.zeros(N**2, dtype=int)#создается квадрат прямой линией, сначала заполняет нулями 
    for i in range(0, N**2):
        square[i] = int(root.find('a' + str(i)).text)#пробегается по всем тегам а и вынимает элементы (если весь массив в одну строчку нумпайтустринг, то ошибка кодировки и дофига непонятных символов)
    square = np.reshape(square, (N, N))#пересобирает строчку ипреобразовываетв квадратрую матрицу (по строкам)
    return N, square

def saveSquareInXml(N, square):
    root = ET.Element('square')#он создает рут
    N_elem = ET.SubElement(root, 'N')#добавляет в него элемент н
    N_elem.text = str(N)#записывает это значение 
    sq = square.reshape(N**2)#преобразовывает массив в строку 
    for i in range(0, N**2): #и пробигаясь по всей строке записывает элементы, 
        array_elem = ET.SubElement(root, 'a' + str(i))#записывает теги 
        array_elem.text = str(sq[i])
    filename = 'square.xml'
    xml_string = ET.tostring(root).decode()#преобразовывает и декодирует чтобы сохранить в файл

    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()#парсит строку и записывает правильно в файл
    with open(filename, 'w') as xml_file:
        xml_file.write(xml_prettyxml)#записал [ml в файл и автоматически закрыл
