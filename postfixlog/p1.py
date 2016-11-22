#!/usr/bin/env python
import re
import threading
import MySQLdb
import datetime,time


###########################################################################################
def Gainid(log):
	#mail id re
	mailid = re.compile(r'\w{11}\:')
	list_id = []
	for line in log:
		m  = mailid.search(line)
		if m is not None:
			list_id.append(m.group().strip(':'))
		else:
			continue
	return list(set(list_id))

def HandleLog(log,mailid):
	mdict = {}
	tomail = ''
	fmail = ''
	for line in log:
		m = re.search(mailid,line)
		if m is not None:
			mailre = re.compile(r'[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+')
			timere = re.compile(r'^\w+\s+\d+\s\d{2}\:\d{2}:\d{2}')
			nt = timere.search(line)
			mtime = nt.group()
			n = mailre.search(line)
			if n is not None:
				f = re.search(r'from\=',line)
				t = re.search(r'to\=',line)
				if f is not None:
					fmail = n.group().strip('<')
				if t is not None:
					tmail = n.group().strip('<')
					statre = re.search(r'\(250',line)
					if statre is not None:
						status = "OK"
					if statre is None:
						statre = re.search(r'Sender address rejected',line)
						if statre is not None:
							status = "User unknown"
						if statre is None:
							statre = re.search(r'Recipient address rejected',line)
							if statre is not None:
								status = "User unknown"
							    if statre is None:
								    status = "other"
					print ("id: %s date :%s  |frdr: %s |  todr: %s | status: %s" % (mailid,mtime ,fmail,tmail,status))
					ttime = fromttime(mtime)
					sql = "insert into mailtest values('%s','%s','%s','%s','%s')" % (mailid,ttime ,fmail,tmail,status)
					insertmail(sql)
#					if tomail:
#						tomail = tomail+"(%s|%s)" % (tmail,status)
#					else:
#						tomail = "(%s|%s)" % (tmail,status)
		else:
			continue
#	mdict['time'] = mtime
#	if fmail:
#		mdict['from'] = fmail
#	else:
#		mdict['from'] = ''
#	mdict['to'] = tomail
#	mdict['id'] = mailid
#
#	print mdict
def fromttime(mtime):
	today = datetime.date.today()

	yer   =	 today.strftime("%Y")
	mtime =  yer + mtime
	ntime =  time.strptime(mtime,"%Y%b  %d %H:%M:%S")
	ttime =  time.strftime('%Y-%m-%d %H:%M:%S',ntime)
	return ttime
def insertmail(sql):
	try:
		conn=MySQLdb.connect(host='localhost',user='root',passwd='####',port=3306,db='dbname')
		cur = conn.cursor()
	cur.execute(sql)
		cur.close()
	conn.commit()
		conn.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0],e.args[1])


def main(logfile):
	#open file
	f = open(logfile,'r')
	log = f.readlines()
	f.close()

	#mail id
	mailid = Gainid(log)
	#HandleLog
	threads = {}
	for i in range(len(mailid)):
		HandleLog(log,mailid[i])
#	HandleLog(log,'850DA916966')


if __name__ == "__main__":
	today = datetime.date.today()
	oneday = datetime.timedelta(days=1)
	yesterday = today - oneday
	tommorrow = today + oneday
	#print yesterday
	zhi = yesterday.strftime("%Y%m%d")
	# logfile = "mail.log.%s" % zhi
    logfile = "maillog"

	main(logfile)
