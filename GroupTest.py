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
		group.set_member('Major-1', 'TsaiSong')
		group.set_member('Major-2', 'GordonLi')
		group.set_member('Backup', 'YanGao')
		self.assertEqual(0.9, group.get_competence('MSC'))
		self.assertEqual(0.8, group.get_competence('NGW'))

	def test_duplicate_staff(self):
		group = Group(self.staffs)
		group.set_member('Major-1', 'TsaiSong')
		group.set_member('Major-2', 'GordonLi')
		self.assertRaises(ValueError, lambda : group.set_member('Backup', 'TsaiSong'))

if __name__ == '__main__':
    unittest.main()