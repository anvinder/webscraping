import docx2txt
import re
import os
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
path = "C:\\Users\\xyz\\PycharmProjects\\beautifulsoup_udemy"

class linkedin_resume:
    def __init__(self):
        self.count_total_jd = 0
        self.read_file = "linkedin_result.txt"
        self.jd_result_file = open("linkedin_result.txt", 'r', errors='ignore', encoding='utf-8')
        # self.result_file = open("parsed_search_result.txt", 'r+', errors='ignore', encoding='utf-8')
        if os.path.isfile('parsed_search_result.txt'):
            self.result_file = open("parsed_search_result.txt", 'r+', errors='ignore', encoding='utf-8')
        else:
            Path('parsed_search_result.txt').touch()
            self.result_file = open("parsed_search_result.txt", 'r+', errors='ignore', encoding='utf-8')


        # self.match_file = open("match_result.txt", 'r+', errors='ignore', encoding='utf-8')
        if os.path.isfile('match_result.txt'):
            self.match_file = open("match_result.txt", 'r+', errors='ignore', encoding='utf-8')
        else:
            Path('match_result.txt').touch()
            self.match_file = open("match_result.txt", 'r+', errors='ignore', encoding='utf-8')

        # self.final_result_file = open("Final_parsed_search_result.txt", 'r+', errors='ignore', encoding='utf-8')
        if os.path.isfile('Final_parsed_search_result.txt'):
            pass
            #self.final_result_file = open("Final_parsed_search_result.txt", 'r+', errors='ignore', encoding='utf-8')
        else:
            Path('Final_parsed_search_result.txt').touch()
            #self.final_result_file = open("Final_parsed_search_result.txt", 'w+', errors='ignore', encoding='utf-8')

        self.resume = docx2txt.process("resume4.docx")
        self.list_hash = []
        self.list_http = []
        self.value_start = 0
        self.value_end = 0
        self.line_temp = ''
        self.temp_list_line_numbers = []
        self.single_string = ''
        self.position_regex = re.compile('(.*)AT')
        self.position = ''
        self.company_regex = re.compile('AT (.*),')
        self.company = ''
        self.link = ''

    def count_jd_in_result_file(self):
        for line_no, line in enumerate(self.jd_result_file):
            if line.startswith("##"):
                temp_line = next(self.jd_result_file)
                match_position = self.position_regex.search(temp_line)
                match_company_loc = self.company_regex.search(temp_line)
                if match_position is not None:
                    self.position = match_position.group(1)
                    self.result_file.writelines([self.position, ","])
                if match_company_loc is not None:
                    self.company = match_company_loc.group(1)
                    self.result_file.writelines([self.company, ","])
                self.result_file.writelines(["\n"])
                line_no += 1
                self.list_hash += [line_no]
            elif line.startswith("http"):
                line_no += 1
                self.list_http += [line_no]
        self.jd_result_file.seek(0)
        for i in range(0, 1):
            for j in range(0, 1):
                self.list_hash.extend(self.list_http)
                i += 1
        if len(self.list_hash) % 2 != 0:
            print("identifier missing (Either #### or https)")
        else:
            list_length = len(self.list_hash)
            half_list = int(list_length/2)
            self.jd_result_file.seek(0)
            for element in range(0, half_list):
                self.value_start = self.list_hash[element]
                later_half = half_list+element
                self.value_end = self.list_hash[later_half]
                for val in range(self.value_start, self.value_end):
                    self.temp_list_line_numbers += [val]
                    self.jd_result_file.seek(self.value_start)
                    for line_no, line in enumerate(self.jd_result_file):
                        if line_no in self.temp_list_line_numbers:
                            self.single_string += line
                text = [self.resume, self.single_string]
                cv = CountVectorizer()
                count_matrix = cv.fit_transform(text)
                matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
                matchPercentage = round(matchPercentage, 2)
                self.match_file.writelines([str(matchPercentage) + "% ", "\n"])
                print("Resume Match " + str(matchPercentage) + "% ")
                self.temp_list_line_numbers.clear()
        # num_lines = self.result_file.read().count('\n')

        self.result_file.seek(0)
        self.match_file.seek(0)
        with open("parsed_search_result.txt") as xh:
            with open('match_result.txt') as yh:
                with open("Final_parsed_search_result.txt", 'w') as zh:
                    xlines = xh.readlines()
                    print(len(xlines))
                    ylines = yh.readlines()
                    print(len(ylines))
                    for line1, line2 in zip(ylines, xlines):
                        zh.write("{} {}\n".format(line2.rstrip(), line1.rstrip()))
                    # for i in range(len(xlines)):
                    #     try:
                    #         line = xlines[i].strip() + ' ' + ylines[i]
                    #         zh.write(line)
                    #     except:
                    #         continue
        self.jd_result_file.close()
        self.result_file.close()
        self.match_file.close()
        # self.final_result_file.close()
        zh.close()

def main_func():
    obj_linkedin_resume = linkedin_resume()
    obj_linkedin_resume.count_jd_in_result_file()


if __name__ == "__main__":
    main_func()
   
