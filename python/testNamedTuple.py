import collections

student = collections.namedtuple("student","student_id name birth age sex")

stus = []

stus.append(student("01","呉剣","1977/11/4","40","M"))
stus.append(student(2,"吴静希","1977/11/4",8,"F"))

print(stus)

print(stus[1]._asdict())