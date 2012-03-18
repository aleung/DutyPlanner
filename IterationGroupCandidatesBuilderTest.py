import unittest
from schedule import Group, IterationGroupCandidatesBuilder

class IterationGroupCandidatesBuilderTest(unittest.TestCase):
	iterations_definition = [
		{
			'days' : 7,
			'pre_plan' : {
				'KennyHuang' : 'NA',
				'TomZhou' : 'NA',
				'DavidNong' : 'Backup',
			}
		},
		{
			'days' : 7,
			'pre_plan' : {
				'KennyHuang' : 'Major',
				'DavidNong' : 'NA',
			}
		},
	]

	def __prepare_groups(self):
		groups = []
		group0 = Group(None)
		group0.set_member('TsaiSong', 'Major')
		group0.set_member('GordonLi', 'Major')
		group0.set_member('TomZhou', 'Backup')
		groups.append(group0)
		group1 = Group(None)
		group1.set_member('KennyHuang', 'Major')
		group1.set_member('TomZhou', 'Major')
		group1.set_member('DavidNong', 'Backup')
		groups.append(group1)
		group2 = Group(None)
		group2.set_member('KennyHuang', 'Major')
		group2.set_member('Ryan', 'Major')
		group2.set_member('YanGao', 'Backup')
		groups.append(group2)
		group3 = Group(None)
		group3.set_member('TsaiSong', 'Major')
		group3.set_member('GordonLi', 'Major')
		group3.set_member('DavidNong', 'Backup')
		groups.append(group3)
		group4 = Group(None)
		group4.set_member('TsaiSong', 'Major')
		group4.set_member('DavidNong', 'Major')
		group4.set_member('GordonLi', 'Backup')
		groups.append(group4)
		return groups

	def test_build(self):
		groups = self.__prepare_groups()
		builder = IterationGroupCandidatesBuilder(groups)
		candidates_of_iterations = builder.build(self.iterations_definition)
		self.assertEqual(2, len(candidates_of_iterations))
		for candidates in candidates_of_iterations:
			print candidates
			self.assertEqual(1, len(candidates))

if __name__ == '__main__':
    unittest.main()