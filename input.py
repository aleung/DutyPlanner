#!/usr/bin/env python

import datetime


iteration_begin_date = datetime.datetime(2012, 3, 19)

# days in each iterations
iteration_days = [7, 7, 7, 7, 7]

# exclude from schedule: (iteration_id, staff_name)
schedule_exclude = [
	(0, "GordonLi"),
	(0, "TomZhou"),
	(1, "TsaiSong"),
]

group_definition = {
	'competence_requirement' : {
		'MSC' : 0.85 ,
		'NGW' : 0.85 ,	
	},
	'roles' : [
		('Major', 2),
		('Backup', 1),
	]
}

staffs = {
	'TsaiSong' : {
		'competence' : {
			'MSC' : 0.9 ,
			'NGW' : 0.4 ,
		},
	},
	'GordonLi' : {
		'competence' : {
			'MSC' : 0.3 ,
			'NGW' : 0.6 ,
		},
	},
	'YanGao' : {
		'competence' : {
			'MSC' : 0.5 ,
			'NGW' : 0.8 ,
		},
	},
	'TomZhou' : {
		'competence' : {
			'MSC' : 0.9 ,
			'NGW' : 0.9 ,
		},
	},
	'JinLiangLi' : {
		'competence' : {
			'MSC' : 0.9 ,
			'NGW' : 0.9 ,
		},
	},
	# 'RyanWeng' : {
	# 	'competence' : {
	# 		'MSC' : 0.9 ,
	# 		'NGW' : 0.9 ,
	# 	},
	# },
	'KennyHuang' : {
		'competence' : {
			'MSC' : 0.9 ,
			'NGW' : 0.9 ,
		},
	},
	'KacyLiu' : {
		'competence' : {
			'MSC' : 0.9 ,
			'NGW' : 0.9 ,
		},
	},
	'DavidNong' : {
		'competence' : {
			'MSC' : 0.9 ,
			'NGW' : 0.9 ,
		},
	},
	'JessicaXie' : {
		'competence' : {
			'MSC' : 0.9 ,
			'NGW' : 0.9 ,
		},
	},
}

competence_areaes = ['MSC', 'NGW']

