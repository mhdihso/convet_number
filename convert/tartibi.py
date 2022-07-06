data = {
    "1f" : "اول",
    "1" : "یکم",
    "2" : "دوم",
    "3" : "سوم",
    "4" : "چهارم",
    "5" : "پنجم",
    "6" : "ششم",
    "7" : "هفتم",
    "8" : "هشتم",
    "9" : "نهم",
    "10" : "دهم",
    "11" : "یازدهم",
    "12" : "دوازدهم",
    "13" : "سیزدهم",
    "14" : "چهاردهم",
    "15" : "پانزدهم",
    "16" : "شانزدهم",
    "17" : "هفدهم",
    "18" : "هجدهم",
    "19" : "نوزدهم",
    "20" : "بیستم",
    "20f" : "بیست ",
    "30" : "سیم",
    "30f" : "سی ",
    "40" : "چهلم",
    "40f" : "چهل ",
    "50" : "پنجاهم",
    "50f" : "پنجاه ",
    "60" : "شصتم",
    "60f" : "شصت ",
    "70" : "هفتادم",
    "70f" : "هفتاد ",
    "80" : "هشتادم",
    "80f" : "هشتاد ",
    "90" : "نودم",
    "90f" : "نود ",
    "100" : "صدم",
    "200" : "دویستم",
    "300" : "سیصدم",
    "400" : "چهارصدم",
    "500" : "پانصدم",
    "600" : "ششصدم",
    "700" : "هفتصدم",
    "800" : "هشتصدم",
    "900" : "نهصدم",
    "100f" : "صد",
    "200f" : "دویست",
    "300f" : "سیصد",
    "400f" : "چهارصد",
    "500f" : "پانصد",
    "600f" : "ششصد",
    "700f" : "هفتصد",
    "800f" : "هشتصد",
    "900f" : "نهصد",
}

and_word = "و"

def numbers_less_than_100(number):
    number = str(number)
    if number == "1":
        return data["1f"]
    elif number == "2":
        return data["2"]
    elif number == "3":
        return data["3"]
    elif number == "4":
        return data["4"]
    elif number == "5":
        return data["5"]
    elif number == "6":
        return data["6"]
    elif number == "7":
        return data["7"]
    elif number == "8":
        return data["8"]
    elif number == "9":
        return data["9"]
    elif number == "10":
        return data["10"]
    elif number == "11":
        return data["11"]
    elif number == "12":
        return data["12"]
    elif number == "13":
        return data["13"]
    elif number == "14":
        return data["14"]
    elif number == "15":
        return data["15"]
    elif number == "16":
        return data["16"]
    elif number == "17":
        return data["17"]
    elif number == "18":
        return data["18"]
    elif number == "19":
        return data["19"]
    elif number == "20":
        return data["20"]
    elif number == "30":
        return data["30"]
    elif number == "40":
        return data["40"]
    elif number == "50":
        return data["50"]
    elif number == "60":
        return data["60"]
    elif number == "70":
        return data["70"]
    elif number == "80":
        return data["80"]
    elif number == "90":
        return data["90"]
    else:
        number = int(number)
        mod = number % 10 
        return data[f"{number - mod}f"] + " " + and_word + " " + data[str(number % 10)]


class Convert:
    def __init__(self, number):
        self.number = number


        
    def convert_number(self):
        if int(self) >= 999:
            return None
        str_number = str()
        try:
            number = str(self)
            str_number = data[number]
            return str_number
        except KeyError:
            if self <100:
                number = numbers_less_than_100(int(number))
                return number
            else:
                if self%100 == 1:
                    number = data["1"]
                else:
                    n = int(number)%100
                    number_ = numbers_less_than_100(int(n))
                n = int(number)%100
                bigger_number = data[str(int(number) - n)+"f"]

                return f"{bigger_number} {and_word} {number_}"


