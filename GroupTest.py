import unittest
from schedule import Group

class GroupTest(unittest.TestCase):
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
	}

	def test_get_competence(self):
		group = Group(self.staffs)
		group.set_member('TsaiSong', 'Major')
		group.set_member('GordonLi', 'Major')
		group.set_member('YanGao', 'Backup')
		self.assertEqual(0.9, group.get_competence('MSC'))
		self.assertEqual(0.8, group.get_competence('NGW'))
		self.assertEqual(0.6, group.get_role_competence('Major', 'NGW'))

	def test_duplicate_staff(self):
		group = Group(self.staffs)
		group.set_member('TsaiSong', 'Major')
		group.set_member('GordonLi', 'Major')
		self.assertRaises(ValueError, lambda : group.set_member('TsaiSong', 'Backup'))

if __name__ == '__main__':
    unittest.main()