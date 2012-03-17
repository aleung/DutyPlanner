#!/usr/bin/env python

import datetime


iteration_begin_date = datetime.datetime(2012, 4, 2)

iterations_definition = [
	{
		'days' : 7,
		'pre_plan' : {
			'YanGao' : 'NA',
			'JinLiangLi' : 'NA',
			'KennyHuang' : 'NA',
			'TomZhou' : 'NA',
			'DavidNong' : 'NA',
			'GordonLi' : 'NA',
			'JessicaXie' : 'NA',
			'TsaiSong' : 'NA',
		}
	},
	{
		'days' : 7,
		'pre_plan' : {
			'KennyHuang' : 'NA',
			'TomZhou' : 'NA',
			'DavidNong' : 'NA',
		}
	},
	{
		'days' : 7,
		'pre_plan' : {
			'KennyHuang' : 'NA',
			'TomZhou' : 'NA',
			'DavidNong' : 'NA',
		}
	},
	{
		'days' : 7,
		'pre_plan' : {
			'KennyHuang' : 'NA',
			'TomZhou' : 'NA',
			'DavidNong' : 'NA',
		}
	},
]

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

