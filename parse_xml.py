import xml.etree.ElementTree as ET
import pandas as pd
import os
import glob
import shutil

xml_path = 'C:/Users/valentin.palchenkov/Desktop/test_xml/'
worker_path = 'C:/Users/valentin.palchenkov/Desktop/worker_xml/'


def xml_mover():
    os.chdir(xml_path)
    for xml_name in glob.glob("1С_report_*.xml"):
        shutil.move(xml_name, worker_path)
        # сюда еще логирование надо запихнуть


def xml_reader(file_name):
    dom = ET.parse(file_name)
    records = dom.findall('record')

    column_names = ['period', 'factory', 'brand', 'thickness', 'volume']
    df = pd.DataFrame(columns=column_names)

    for rec in records:
        per = rec.find('period').text
        fact = rec.find('factory').text
        br = rec.find('brand').text
        thickn = rec.find('thickness').text
        vol = rec.find('volume').text

        row_as_df = pd.DataFrame([
            per, fact, br, thickn, vol
        ], columns=column_names)
        df.append(row_as_df, ignore_index=True)


def xml_to_csv():
    os.chdir(xml_path)
    for xml_name in glob.glob("1С_report_*.xml"):
        print(f'Open {xml_name} file...')
        xml_reader(xml_name)


if __name__ == '__main__':
    xml_to_csv()
