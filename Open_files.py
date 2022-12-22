def open_file(file_name):
    line_count[file_name] = sum(1 for line in open(file_name))
    return line_count
open_file('1.txt')
open_file('2.txt')
open_file('3.txt')

def sorted_new(line):
    sort_dict = sorted(line.values())
    sorted_dict = {}
    for i in sort_dict:
        for k in line.keys():
            if line[k] == i:
                sorted_dict[k] = line[k]
                break
    return sorted_dict
    
def write_file(file1, file2, file3):
    sorted_dict=sorted_new(line_count)
    for key in sorted_dict.keys():
        # files=[file1, file2, file3]
        for i, x in enumerate([file1, file2, file3]):
            if key==x:
                with open(x) as f, open('result.txt', 'a') as res:
                    number_of_rows=sum(1 for _ in f)
                    res.write(f'Имя файла: {x}\nколичество строк:\n{f.read()}')
                    


write_file('1.txt', '2.txt', '3.txt')
