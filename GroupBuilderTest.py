import unittest
from schedule import Group, GroupBuilder

class GroupBuilderTest(unittest.TestCase):
	staffs = {
		'TsaiSong' : {
			'competence' : {
				'MSC' : 0.7 ,
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
				'NGW' : 0.1 ,
			},
		},
	}

	group_definition = {
		'competence_requirement' : {
			'MSC' : 0.8 ,
			'NGW' : 0.8 ,	
		},
		'roles' : {
			'Main' : {
				'persons' : 2,
				'competence_requirement' : {
					'MSC' : 0.6 ,
					'NGW' : 0.6 ,	
				}
			},
			'Backup' : {
				'persons' : 1,
				'competence_requirement' : {
					'MSC' : 0.6 ,
					'NGW' : 0 ,	
				}
			}
		}
	}

	def test_build(self):
		builder = GroupBuilder(self.staffs, self.group_definition)
		groups = builder.build()
		for group in groups:
			print 'Group %s, MSC %f, NGW %f' % (group.get_members(), group.get_competence('MSC'), group.get_competence('NGW'))
		self.assertEqual(2, len(groups))

if __name__ == '__main__':
    unittest.main()