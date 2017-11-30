#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Project 3
# Lab Section 206
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: python documentation, zyante exercises 1-13
#-------------------------------------------------------------------------------
# Comments and assumptions:
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
#1
def read_file(filename):
	#{(name,gender):{year:(count,rank),year:(count,rank)}}
	#new dictionary empty
	unranked_base = {}
	#working list empty
	work_list = []
	#open a file with as f
	with open(filename) as f:
		#read f as f
		f = f.read()
		#split f at each \n
		f = f.split("\n")
		#each value in list f 
		for line in f:
			#split f again for each "
			f = line.split("\"")
			#for each value in f
			for j in f:
				#if j is a comma
				if j == ',':
					#get rid of it
					f.remove(j)
				#if j is a space
				if j == '':
					#get rid of that too
					f.remove(j)
			#exclude blank lines
			if len(f)>1:
				#exculde first line of words
				if f[3] == 'COUNT':
					#keep going
					continue
				#check for repeat names
				elif (f[2],f[1]) in unranked_base:
					#make new innertup of count,rank and add to name
					#get f[2],f[1] from unranked, set to existing name
					existing_name = unranked_base.get((f[2],f[1]))
					#make f[3],None count,rank, set to innertup
					innertup = (int(f[3]),None)
					#make f[0] with innertup to dictionary
					innerdb = {int(f[0]):innertup}
					#update existing name with innerdb
					existing_name.update(innerdb)
				#otherwise
				else:
					#make new tup of f[2],f[1], name,gender
					outertup = (f[2],f[1])
					#make innertup of f[3],none, count,rank
					innertup = (int(f[3]),None)
					#make innerdb f[0] and innertup
					innerdb = {int(f[0]):innertup}
					#make outerdb outertup and innertup
					outerdb = {outertup:innerdb}
					#update unranked database with new value
					unranked_base.update(outerdb)
	#return filled unranked database
	return unranked_base
#2	
def add_name(db, name, gender, year, count):
	#{(name,gender):{year:(count,rank),year:(count,rank)}}
	#pack name,gender into tup key1
	key1 = (name,gender)
	#if key1 in db
	if key1 in db:
		#grab value of db[key1] and make valdict
		valdict = db[key1]
		#update valdict with dictionary of year, count,rank
		valdict.update({year:(count,None)})
	#otherwise
	else:
		#make count,rank to wipval tuple
		wipval = (count, None)
		#make value1 dictionary of year,wipval
		value1 = {year:wipval}
		#value2 to key1,value1 dictionary
		value2 = {key1:value1}
		#update db with value2
		db.update(value2)
#3
def find_all_years(db):
	#empty list years
	years = []
	#for each value in dictionary db
	for value in db.values():
		#for key in value dictionary
		for key in value.keys():
			#make key int, then make workkey
			workkey = int(key)
			#check if workkey not already in years
			if workkey not in years:
				#append to years list
				years.append(workkey)
	#sort years
	sortyear = sorted(years)
	#return sortyear list
	return sortyear
#4
def new_names(db, gender, old_year, new_year):
	#new empty list l
	l = []
	#for each key, value in db
	for key,value in db.items():
		#unpack tuple key to key1,val1
		key1,val1 = key
		#if val1 is gender
		if val1 == gender:
			#and if oldyear not in value and newyear in value
			if old_year not in value and new_year in value:
				#add key1 to list l
				l.append(key1)
	#sort l
	lsort = sorted(l)
	#return lsort
	return lsort
#5
def rank_names_for_one_year(db, year):
	#{(name,gender):{year:(count,rank),year:(count,rank)}}
	#male work list
	m_work_list = []
	#female work list
	f_work_list = []
	#for every key,vlaue in db
	for key,value in db.items():
		#unpack key to name,gender
		name,gender = key
		#if year is in value
		if year in value:
			#get value[year], set it to tup
			tup = value.get(year)
			#if male
			if gender == "MALE":
				#add tup to male list
				m_work_list.append(tup)
			#if female
			elif gender == "FEMALE":
				#add tup to female list
				f_work_list.append(tup)
	#sorting lists
	#sort male list
	m_work_list.sort(reverse=True)
	#sort female list
	f_work_list.sort(reverse=True)
	#male conversions
	#for each index in range of mlist
	for i in range(len(m_work_list)):
		#unpack mlist[i] as count,rank
		count,rank = m_work_list[i]
		#if len of mlist is 1
		if len(m_work_list) == 1:
			#make rank 1
			rank = 1
		#otherwise
		else:
			#unpack mlist[i-1] as count1,rank1
			count1,rank1 = m_work_list[i-1]
			#if count same as count1
			if count == count1:
				#if i is 0
				if i == 0:
					#rank is i+1
					rank = i+1
				#otherwise
				else:
					#rank = rank1
					rank = rank1
			#otherwise
			else:
				#rank = i+1
				rank = i+1
		#repack count,rank into mlist
		m_work_list[i] = (count,rank)
	#female conversions
	#for each index in range of flist
	for l in range(len(f_work_list)):
		#unpack flist[l] as count,rank
		count,rank = f_work_list[l]
		#if len of flist is 1
		if len(f_work_list) == 1:
			#rank is 1
			rank = 1
		#otherwise
		else:
			#unpack flist[i-1] as count1,rank1
			count1,rank1 = f_work_list[l-1]
			#if count same as count1
			if count == count1:
				#if l is 0
				if l == 0:
					#rnak is l+1
					rank = l+1
				#otherwise
				else:
					#rank = rank1
					rank = rank1
			#otherwise
			else:
				#rank = l+1
				rank = l+1
		#repack count,rank in flist
		f_work_list[l] = (count,rank)
	#pushing new vals
	#for key and value of db
	for key,value in db.items():
		#unpack key as name,gender
		name,gender = key
		#if year in the value key
		if year in value:
			#get value[year] as tup
			tup = value.get(year)
			#if male
			if gender == "MALE":
				#unpack tup to oldcount,oldrank
				oldcount,oldrank = tup
				#for each value in mlist
				for j in m_work_list:
					#pack newcount,newrank as j
					newcount,newrank = j
					#if oldcount same as newcount
					if oldcount == newcount:
						#just copy/paste tup
						tup = j
						#update value dictionary with year,tup
						value.update({year:tup})
			#otherwise if female
			elif gender == "FEMALE":
				#unpack tup as oldcount,oldrank
				oldcount,oldrank = tup
				#for each value in flist
				for k in f_work_list:
					#pack newcount,newrank as k
					newcount,newrank = k
					#if oldcount same as newcount
					if oldcount == newcount:
						#copy/paste tup as k
						tup = k
						#update value dictionary with year,tup
						value.update({year:tup})
#6
def rank_names(db):
	#{(name,gender):{year:(count,rank),year:(count,rank)}}
	#use find_all_years function with arguments db, set as years
	years = find_all_years(db)
	#for each year in years list
	for year in years:
		#use rank_names_for_one_year with arguments db, year
		rank_names_for_one_year(db, year)
#7
def popularity_by_name(rdb, name, gender):
	#{(name,gender):{year:(count,rank),year:(count,rank)}}
	#empty list popular list
	popular_list = []
	#for each key,value in rdb
	for key,value in rdb.items():
		#make keymatch a tuple name,gender
		keymatch = (name,gender)
		#if keymatch is same as the key
		if keymatch == key:
			#for each year and tupval in value
			for year,tup in value.items():
				#unpack tup as count,rank
				count,rank = tup
				#make tupset year,rank
				tupset = (year,rank)
				#add tupset to popularlist
				popular_list.append(tupset)
	#sort popular list
	sorted(popular_list)
	#return popular list
	return popular_list
#8
def popularity_by_year(rdb, gender, year, top=10):
	#{(name,gender):{year:(count,rank),year:(count,rank)}}
	#empty list popular list
	popular_list = []
	#for each key,value in rdb
	for key,value in rdb.items():
		#unpack key as name,keygender
		name,keygender = key
		#if keygender same as gender
		if keygender == gender:
			#keyyear,tup in value dictionary
			for keyyear,tup in value.items():
				#unpack tup as count,rank
				count,rank = tup
				#if keyyear is same as year
				if keyyear == year:
					#pack tupset as rank,name
					tupset = (rank,name)
					#add tupset to popularlist
					popular_list.append(tupset)
	#sort popular list
	popular_list.sort()
	#if top is greater than or equal to length of poplist
	if top >= len(popular_list):
		#return all of poplist
		return popular_list
		#otherwise
	else:
		#make tupset popularlist[top]
		tupset = popular_list[top]
		#unpack tupset as rank,name
		rank,name = tupset
		#make tupset popularlist[top-1]
		tupset1 = popular_list[top-1]
		#unpack tupset1 as rank1,name1
		rank1,name1 = tupset1
		#if rank same as rank1
		if rank == rank1:
			#top increase by 1
			top += 1
		#toplist becomes spliced copy of poplist from 0 to top
		top_list = popular_list[0:top]
		#return top list
		return top_list
#9
def always_popular_names(rdb, gender, years=None, top=10):
	#{(name,gender):{year:(count,rank),year:(count,rank)}}
	#empty list poplist
	popular_list = []
	#checkkeylist as empty list
	key_check_list = []
	#if years is none
	if years == None:
		#use find_all_years with arguments rdb as years
		years = find_all_years(rdb)
	#for key,value in rdb
	for key,value in rdb.items():
		#unpack key as name,gender1
		name,gender1 = key
		#if gender1 not same as gender
		if gender1 != gender:
			#keep going
			continue
		#cc as counter at 0
		cc = 0
		#for key1,value1 in value dictonary
		for key1,value1 in value.items():
			#all_in to True
			all_in = True
			#unpack value1 as count,rank
			count,rank = value1
			#if key1 not in list of years
			if key1 not in years:
				#if cc is greater or same as len of years list
				if cc >= len(years):
					#all_in stays true
					all_in = True
					#reset cc
					cc = 0
					#break loop
					break
				#otherwise if cc less than len of years
				elif cc < len(years):
					#add key1 to keychecklist
					key_check_list.append(key1)
					#all_in is false
					all_in = False
					#cc reset
					cc = 0
					#break looop
					break
				#otherwise rank greater than top
				elif rank > top:
					#add key1 to keychecklist
					key_check_list.append(key1)
					#all_in is falst
					all_in = False
					#cc reset
					cc = 0
					#break loop
					break
			#otherwise if key1 is in list years and rank is bigger than top
			elif key1 in years and rank > top:
				#add key1 to keychecklist
				key_check_list.append(key1)
				#all_in is false
				all_in = False
				#break loop
				break
			#otherwise
			else:
				#add key1 to keychecklist
				key_check_list.append(key1)
				#add 1 to cc
				cc += 1
		#if all_in is still True at this point
		if all_in == True:
			#check length of keychecklsit is same as years
			if key_check_list == years:
				#add name to poplist if so
				popular_list.append(name)
				#empty keychecklist
				key_check_list = []
			#otherwise
			else:
				#straight up empty keychecklist
				key_check_list = []
		#otherwise
		else:
			#empty keychecklist
			key_check_list = []
	#sort poplist
	popular_list.sort()
	#return poplist
	return popular_list
#10
def increasing_rank_names(rdb, gender, old_year, new_year):
	#{(name,gender):{year:(count,rank),year:(count,rank)}}
	#empty list years
	years = []
	#epty list ans
	ans = []
	#for key,value in rdb
	for key,value in rdb.items():
		#for year,tup in value dictionary
		for year, tup in value.items():
			#add year to years list
			years.append(year)
		#unpack key to name,gender1
		name,gender1 = key
		#if gender1 not gender
		if gender1 != gender:
			#forget and move on
			continue
		#otherwise
		else:
			#if oldyear in years and newyear in years
			if old_year in years and new_year in years:
				#get value[oldyear] as old_tup
				old_tup = value.get(old_year)
				#get value[newyear] as new_tup
				new_tup = value.get(new_year)
				#unpack old_tup to count1,rank1
				count1,rank1 = old_tup
				#unpack new_tup as count2,rank2
				count2,rank2 = new_tup
				#if rank1 is bigger than rank2
				if rank1 > rank2:
					#add name to anslist
					ans.append(name)
				#empty yearslist
				years = []
			#otherwise
			else:
				#empty yearslist
				years = []
	#sort anslist
	ans.sort()
	#return anslist
	return ans

