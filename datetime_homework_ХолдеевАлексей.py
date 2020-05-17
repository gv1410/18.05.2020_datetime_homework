import re
import datetime

    
def reader(filename_logs, pattern_data):

    with open(filename_logs) as fp:
        
        log = fp.read()

        ip_list = re.findall(pattern_data, log)

        return ip_list

def main():

    reg_ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-'
    reg_date_pattern = r'\d{2}\/\w{3}\/\d{4}'
    reg_ip_data_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-\s\[\d{2}\/\w{3}\/\d{4}'

    nomber_of_request_date = reader('apache_logs.txt', reg_date_pattern)
    nomber_of_unique_request_date = reader('apache_logs.txt', reg_ip_data_pattern)
    list_of_data = list(set(nomber_of_request_date))
    list_unique_date = list(set(nomber_of_unique_request_date))

    browsers = ('Opera', 'Firefox', 'Safari', 'Chrome')

    number_of_request_ip = reader('apache_logs.txt', reg_ip_pattern)

    print('Число уникальных запросов к серверу равно: ' + str(len(set(number_of_request_ip))))    
    print('Число запросов к серверу равно: ' + str(len(number_of_request_ip)))

    
    for i in browsers:
        number_of_request_browser = reader('apache_logs.txt', i)
        print('Число обращений от браузера ' + i + ': ' + str(len(number_of_request_browser)))

    for date in list_of_data:
        unique_request_from_data_list = reader('apache_logs.txt', date)
        unique_request_from_data = len(unique_request_from_data_list)
        b = re.compile(date)
        selected_files = list(filter(b.search, list_unique_date))
        print(str(datetime.datetime.strptime(date, '%d/%b/%Y')) + ' total request  ' + str(unique_request_from_data) + ' unique_request ' + str(len(selected_files)))
    
    

if __name__ == "__main__":
    main()