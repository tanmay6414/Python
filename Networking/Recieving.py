import poplib
from email import parser

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('mssatav@mitaoe.ac.in')
pop_conn.pass_('TECHNOGENIC')
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
messages = ["\n".join(mssg[1]) for mssg in messages]
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
    print(message)
