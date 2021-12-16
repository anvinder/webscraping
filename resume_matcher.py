import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
path = "C:\\Users\\qqq\\PycharmProjects"

class linkedin_resume:
    def __init__(self):
        self.count_total_jd = 0
        self.read_file = "linkedin_result.txt"
        self.jd_result_file = open("linkedin_result.txt", 'r', errors='ignore', encoding='utf-8')
        self.resume = docx2txt.process("resume4.docx")
        self.list_hash = []
        self.list_http = []
        self.value_start = 0
        self.value_end = 0
        self.line_temp = ''
        self.temp_list_line_numbers = []
        self.single_string = ''

    def count_jd_in_result_file(self):
        for line_no, line in enumerate(self.jd_result_file):
            if line.startswith("#"):
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
        if len(self.list_hash)%2 != 0:
            print("identifier missing (Either #### or https)")
        else:
            list_length = len(self.list_hash)
            half_list = int(list_length/2)
            self.jd_result_file.seek(0)
            for element in range(0, half_list):
                self.value_start = self.list_hash[element]
                later_half = half_list+element
                self.value_end = self.list_hash[later_half]
                # print(self.value_start, self.value_end)
                # self.jd_result_file.seek(0)

                for val in range(self.value_start, self.value_end):
                    self.temp_list_line_numbers += [val]
                    #print(self.temp_list_line_numbers)
                    self.jd_result_file.seek(self.value_start)
                    for line_no, line in enumerate(self.jd_result_file):
                        if line_no in self.temp_list_line_numbers:
                            self.single_string += line
                text = [self.resume, self.single_string]
                cv = CountVectorizer()
                count_matrix = cv.fit_transform(text)
                matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
                matchPercentage = round(matchPercentage, 2)
                print("Resume Match " + str(matchPercentage) + "% ")
                self.temp_list_line_numbers.clear()


def main_func():
    obj_linkedin_resume = linkedin_resume()
    obj_linkedin_resume.count_jd_in_result_file()


if __name__ == "__main__":
    main_func()
