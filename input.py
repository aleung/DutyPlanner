#!/usr/bin/env python

import datetime


iteration_begin_date = datetime.date(2012, 4, 2)

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
			'TsaiSong' : 'Backup',
			'KacyLiu' : 'Main',
		}
	},
	{
		'days' : 7,
		'pre_plan' : {
			'JinLiangLi' : 'NA',
			'KennyHuang' : 'NA',
			'TomZhou' : 'NA',
			'DavidNong' : 'NA',
			'YanGao' : 'Main',
		}
	},
	{
		'days' : 7,
		'pre_plan' : {
			'KennyHuang' : 'NA',
			'TomZhou' : 'NA',
			'DavidNong' : 'NA',
			'YanGao' : 'NA',
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
		'MGW' : 0.75 ,	
	},
	'roles' : {
		'Main' : {
			'persons' : 2,
			'competence_requirement' : {
				'MSC' : 0.6 ,
				'MGW' : 0.6 ,	
			}			
		},
		'Backup' : {
			'persons' : 1,
			'competence_requirement' : {
				'MSC' : 0.6 ,
				'MGW' : 0 ,	
			}			
		}
	}
}

staffs = {
	'TsaiSong' : {
		'competence' : {
			'MSC' : 0.85 ,
			'MGW' : 0.85 ,
		},
	},
	'GordonLi' : {
		'competence' : {
			'MSC' : 0.85 ,
			'MGW' : 0.85 ,
		},
	},
	'YanGao' : {
		'competence' : {
			'MSC' : 0.75 ,
			'MGW' : 0.1 ,
		},
	},
	'TomZhou' : {
		'competence' : {
			'MSC' : 0.85 ,
			'MGW' : 0.75 ,
		},
	},
	'JinLiangLi' : {
		'competence' : {
			'MSC' : 0.7 ,
			'MGW' : 0.7 ,
		},
	},
	'RyanWeng' : {
		'competence' : {
			'MSC' : 0.7 ,
			'MGW' : 0.7 ,
		},
	},
	'KennyHuang' : {
		'competence' : {
			'MSC' : 0.65 ,
			'MGW' : 0.65,
		},
	},
	'KacyLiu' : {
		'competence' : {
			'MSC' : 0.7 ,
			'MGW' : 0.7 ,
		},
	},
	'DavidNong' : {
		'competence' : {
			'MSC' : 0.6 ,
			'MGW' : 0.6 ,
		},
	},
	'JessicaXie' : {
		'competence' : {
			'MSC' : 0.1 ,
			'MGW' : 0.7 ,
		},
	},
}

competence_areaes = ['MSC', 'MGW']

