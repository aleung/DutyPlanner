#!/usr/bin/env python

import datetime


iteration_begin_date = datetime.datetime(2012, 4, 2)

# days in each iterations
iteration_days = [7, 7, 7, 7]

# exclude from schedule: (iteration_id, staff_name)
schedule_exclude = [
	(0, "YanGao"),
	(0, "JinLiangLi"),
	(0, "KennyHuang"),
	(0, "TomZhou"),
	(0, "DavidNong"),
	(0, "GordonLi"),
	(0, "JessicaXie"),
	(0, "TsaiSong"),
	(1, "KennyHuang"),
	(1, "TomZhou"),
	(1, "DavidNong"),
	(2, "KennyHuang"),
	(2, "TomZhou"),
	(2, "DavidNong"),
	(2, "YanGao"),
	(3, "KennyHuang"),
	(3, "TomZhou"),
	(3, "DavidNong"),
]

max_continuous_iterations = 2

group_definition = {
	'competence_requirement' : {
		'MSC' : 0.75 ,
		'NGW' : 0.75 ,	
	},
	'roles' : [
		('Major', 2),
		('Backup', 1),
	]
}

staffs = {
	'TsaiSong' : {
		'competence' : {
			'MSC' : 0.85 ,
			'NGW' : 0.85 ,
		},
	},
	'GordonLi' : {
		'competence' : {
			'MSC' : 0.85 ,
			'NGW' : 0.85 ,
		},
	},
	'YanGao' : {
		'competence' : {
			'MSC' : 0.75 ,
			'NGW' : 0.1 ,
		},
	},
	'TomZhou' : {
		'competence' : {
			'MSC' : 0.85 ,
			'NGW' : 0.75 ,
		},
	},
	'JinLiangLi' : {
		'competence' : {
			'MSC' : 0.7 ,
			'NGW' : 0.7 ,
		},
	},
	'RyanWeng' : {
		'competence' : {
			'MSC' : 0.7 ,
			'NGW' : 0.7 ,
		},
	},
	'KennyHuang' : {
		'competence' : {
			'MSC' : 0.65 ,
			'NGW' : 0.65,
		},
	},
	'KacyLiu' : {
		'competence' : {
			'MSC' : 0.7 ,
			'NGW' : 0.7 ,
		},
	},
	'DavidNong' : {
		'competence' : {
			'MSC' : 0.6 ,
			'NGW' : 0.6 ,
		},
	},
	'JessicaXie' : {
		'competence' : {
			'MSC' : 0.1 ,
			'NGW' : 0.7 ,
		},
	},
}

competence_areaes = ['MSC', 'NGW']

